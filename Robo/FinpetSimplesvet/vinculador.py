import numpy as np
from numba import njit
from matchers import preprocessar_finpet, preprocessar_releases, calcular_comparacoes


@njit(cache=True)
def _match_loop(
    fp_arr: np.ndarray, rel_arr: np.ndarray, auth_match: np.ndarray, min_score: int
) -> np.ndarray:
    """Loop crÃ­tico O(n*m) otimizado com JIT."""
    n_fp = fp_arr.shape[0]
    n_rel = rel_arr.shape[0]

    resultado = np.full((n_fp, 2), -1, dtype=np.int32)
    usados = np.zeros(n_rel, dtype=np.bool_)

    for i in range(n_fp):
        if fp_arr[i, 5] == 0:
            continue

        melhor_idx = -1
        melhor_score = 0

        for j in range(n_rel):
            if usados[j]:
                continue

            if fp_arr[i, 5] != rel_arr[j, 4]:
                continue

            score = 0

            # Parcela
            if fp_arr[i, 0] > 0 and rel_arr[j, 0] > 0:
                if fp_arr[i, 0] == rel_arr[j, 0] and fp_arr[i, 1] == rel_arr[j, 1]:
                    score += 1

            # Valor
            if abs(fp_arr[i, 2] - rel_arr[j, 2]) <= 1:
                score += 1

            # Data
            if rel_arr[j, 3] > 0:
                if fp_arr[i, 3] == rel_arr[j, 3] or fp_arr[i, 4] == rel_arr[j, 3]:
                    score += 1

            # Auth
            if auth_match[i, j]:
                score += 1

            if score > melhor_score:
                melhor_score = score
                melhor_idx = j

        resultado[i, 0] = melhor_idx
        resultado[i, 1] = melhor_score

        if melhor_idx >= 0 and melhor_score >= min_score:
            usados[melhor_idx] = True

    return resultado


def _criar_auth_match(auths_fp: list, auths_rel: list) -> np.ndarray:
    """Cria matriz de match de auth (auths_rel é lista de listas)."""
    n_fp, n_rel = len(auths_fp), len(auths_rel)
    match = np.zeros((n_fp, n_rel), dtype=np.bool_)

    for i, a1 in enumerate(auths_fp):
        if not a1:
            continue
        for j, candidates in enumerate(auths_rel):
            if a1 in candidates:
                match[i, j] = True

    return match


def finpet_simplesvet(finpet: list, releases: list, min_score: int = 3) -> list:
    """Vincula finpet com releases."""
    fp_arr, auths_fp = preprocessar_finpet(finpet)
    rel_arr, auths_rel = preprocessar_releases(releases)
    auth_match = _criar_auth_match(auths_fp, auths_rel)

    matches = _match_loop(fp_arr, rel_arr, auth_match, min_score)

    resultados = []
    for i, fp in enumerate(finpet):
        idx, score_jit = matches[i]

        if idx >= 0 and score_jit >= min_score:
            rel = releases[idx]
            score_real, comp = calcular_comparacoes(fp, rel)
            resultados.append(
                {"finpet": fp, "release": rel, "score": score_real, "comparacoes": comp}
            )
        else:
            resultados.append(
                {"finpet": fp, "release": None, "score": 0, "comparacoes": {}}
            )

    return resultados


def resumo_vinculacao(resultados: list) -> dict:
    vinculados = [r for r in resultados if r["release"]]
    scores = [r["score"] for r in vinculados]
    return {
        "total": len(resultados),
        "vinculados": len(vinculados),
        "nao_vinculados": len(resultados) - len(vinculados),
        "score_medio": sum(scores) / len(scores) if scores else 0,
    }
