#!/usr/bin/env python3
"""
JSON Schema Generator
Gera um esquema detalhado da estrutura de um arquivo JSON.
IMPORTANTE: Detecta os tipos exatamente como estão no JSON, sem nenhuma conversão.
"""

import json
import sys
from pathlib import Path
from typing import Any
from collections import Counter


def get_type_name(value: Any) -> str:
    """
    Retorna o nome do tipo de um valor.

    IMPORTANTE: Esta função detecta o tipo REAL do valor após o parsing do JSON.
    Não há nenhuma conversão - o tipo retornado é exatamente o que está no JSON:

    No JSON          | Em Python      | Tipo retornado
    -----------------|----------------|---------------
    null             | None           | "null"
    true/false       | bool           | "boolean"
    42               | int            | "integer"
    3.14             | float          | "float"
    "texto"          | str            | "string"
    "123"            | str            | "string" (NÃO converte para número!)
    "2.5"            | str            | "string" (NÃO converte para número!)
    []               | list           | "array"
    {}               | dict           | "object"
    """
    if value is None:
        return "null"

    # IMPORTANTE: Verificar bool ANTES de int, pois bool é subclasse de int em Python
    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, int):
        return "integer"

    if isinstance(value, float):
        return "float"

    if isinstance(value, str):
        # Retorna "string" independente do conteúdo
        # "123", "2.5", "true", "null" são TODOS strings se estiverem entre aspas no JSON
        return "string"

    if isinstance(value, list):
        return "array"

    if isinstance(value, dict):
        return "object"

    # Fallback para tipos não esperados
    return type(value).__name__


def analyze_array(arr: list, depth: int = 0) -> dict:
    """Analisa a estrutura de um array."""
    if not arr:
        return {"type": "array", "length": 0, "items": "empty"}

    # Coleta tipos únicos dos elementos
    type_counts = Counter()
    sample_structures = {}
    sample_values = {}

    for item in arr:
        item_type = get_type_name(item)
        type_counts[item_type] += 1

        # Guarda uma amostra da estrutura para cada tipo
        if item_type not in sample_structures:
            if item_type == "object":
                sample_structures[item_type] = analyze_structure(item, depth + 1)
            elif item_type == "array":
                sample_structures[item_type] = analyze_array(item, depth + 1)
            else:
                sample_structures[item_type] = {"type": item_type}
                # Guarda um exemplo do valor para tipos primitivos
                sample_values[item_type] = repr(item)

    # Se todos os itens são do mesmo tipo
    if len(type_counts) == 1:
        item_type = list(type_counts.keys())[0]
        result = {
            "type": "array",
            "length": len(arr),
            "items": sample_structures[item_type],
        }
        if item_type in sample_values:
            result["sample_value"] = sample_values[item_type]
        return result

    # Se há tipos misturados
    return {
        "type": "array",
        "length": len(arr),
        "mixed_types": True,
        "type_distribution": dict(type_counts),
        "items_by_type": sample_structures,
        "sample_values": sample_values,
    }


def analyze_structure(data: Any, depth: int = 0) -> dict:
    """Analisa recursivamente a estrutura de um objeto JSON."""
    data_type = get_type_name(data)

    if data_type == "object":
        if not data:
            return {"type": "object", "properties": {}, "keys_count": 0}

        properties = {}
        for key, value in data.items():
            value_type = get_type_name(value)

            if value_type == "object":
                properties[key] = analyze_structure(value, depth + 1)
            elif value_type == "array":
                properties[key] = analyze_array(value, depth + 1)
            else:
                # Para tipos primitivos, guarda também um exemplo do valor
                properties[key] = {"type": value_type, "sample_value": repr(value)}

        return {"type": "object", "keys_count": len(data), "properties": properties}

    elif data_type == "array":
        return analyze_array(data, depth)

    else:
        return {"type": data_type, "sample_value": repr(data)}


def format_schema(schema: dict, indent: int = 0) -> str:
    """Formata o esquema em uma string legível."""
    lines = []
    prefix = "  " * indent

    schema_type = schema.get("type", "unknown")

    if schema_type == "object":
        keys_count = schema.get("keys_count", 0)
        lines.append(f"{prefix}object ({keys_count} chaves)")

        properties = schema.get("properties", {})
        for key, value in properties.items():
            value_type = value.get("type", "unknown")

            if value_type == "object":
                lines.append(f"{prefix}  ├─ {key}: object")
                nested = format_schema(value, indent + 2)
                if nested:
                    lines.append(nested)
            elif value_type == "array":
                array_info = format_array_info(value)
                lines.append(f"{prefix}  ├─ {key}: {array_info}")
                if value.get("items") and isinstance(value["items"], dict):
                    if value["items"].get("type") == "object":
                        nested = format_schema(value["items"], indent + 2)
                        if nested:
                            lines.append(nested)
            else:
                sample = value.get("sample_value", "")
                sample_str = f" (ex: {sample})" if sample else ""
                lines.append(f"{prefix}  ├─ {key}: {value_type}{sample_str}")

    elif schema_type == "array":
        array_info = format_array_info(schema)
        lines.append(f"{prefix}{array_info}")

        if schema.get("items") and isinstance(schema["items"], dict):
            if schema["items"].get("type") == "object":
                nested = format_schema(schema["items"], indent + 1)
                if nested:
                    lines.append(nested)

    else:
        sample = schema.get("sample_value", "")
        sample_str = f" (ex: {sample})" if sample else ""
        lines.append(f"{prefix}{schema_type}{sample_str}")

    return "\n".join(lines)


def format_array_info(schema: dict) -> str:
    """Formata informações de um array."""
    length = schema.get("length", "?")
    items = schema.get("items")

    if items == "empty":
        return f"array[{length}] (vazio)"

    if schema.get("mixed_types"):
        types = list(schema.get("type_distribution", {}).keys())
        return f"array[{length}] (tipos mistos: {', '.join(types)})"

    if isinstance(items, dict):
        item_type = items.get("type", "unknown")
        if item_type == "object":
            keys_count = items.get("keys_count", "?")
            return f"array[{length}] de objects ({keys_count} chaves cada)"
        elif item_type == "array":
            return f"array[{length}] de arrays"
        else:
            sample = schema.get("sample_value", "")
            sample_str = f" (ex: {sample})" if sample else ""
            return f"array[{length}] de {item_type}{sample_str}"

    return f"array[{length}]"


def generate_schema_report(data: Any, filename: str = "input") -> str:
    """Gera um relatório completo do esquema."""
    schema = analyze_structure(data)

    report = []
    report.append("=" * 60)
    report.append("ESQUEMA JSON - ESTRUTURA DETALHADA")
    report.append("=" * 60)
    report.append(f"\nArquivo: {filename}")
    report.append(f"Tipo raiz: {schema.get('type', 'unknown')}")
    report.append("\n" + "-" * 60)
    report.append("ESTRUTURA:")
    report.append("-" * 60 + "\n")

    formatted = format_schema(schema)
    report.append(formatted)

    report.append("\n" + "-" * 60)
    report.append("ESQUEMA COMPLETO (JSON):")
    report.append("-" * 60 + "\n")
    report.append(json.dumps(schema, indent=2, ensure_ascii=False))

    return "\n".join(report)


def main():
    # Verifica argumentos da linha de comando
    if len(sys.argv) < 2:
        print("Uso: python json_schema_generator.py <arquivo.json> [arquivo_saida.txt]")
        print("\nExemplo:")
        print("  python json_schema_generator.py dados.json")
        print("  python json_schema_generator.py dados.json esquema.txt")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    # Define arquivo de saída
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.with_suffix(".schema.txt")

    # Verifica se o arquivo de entrada existe
    if not input_file.exists():
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
        sys.exit(1)

    # Carrega o JSON
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro: JSON inválido - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        sys.exit(1)

    # Gera o relatório do esquema
    report = generate_schema_report(data, input_file.name)

    # Salva o arquivo de saída
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"✓ Esquema gerado com sucesso!")
        print(f"  Arquivo de saída: {output_file}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        sys.exit(1)

    # Também imprime no console
    print("\n" + report)


if __name__ == "__main__":
    main()
