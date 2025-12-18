# JSON Schema: `dados.json`

## Resumo

- **Tipo raiz:** `object`
- **Campos únicos:** 77

## Estrutura

```
root: object
  finpet: array
    finpet[*]: object
      anticipate_value: integer
      authorization_number: string <numeric_string>
      bank: string
      bank_agency: string <numeric_string>
      beneficiary: string
      beneficiary_document: string <phone>
      beneficiary_type: string
      beneficiary_value: integer|number
      client_name: string
      client_phone: string
      collection_id: string
      collection_name: string
      cpf: string <phone>
      created: string <datetime_iso>
      currency: string
      date_estimated: string <datetime_iso>
      date_received: string <datetime_iso>
      deposit_account: string
      deposit_value: integer|number
      discounted_value: integer|number
      due_date: string <datetime_iso>
      expand: object
      fee: number
      gross_value: integer|number
      has_chargeback: boolean
      has_contract_applied: boolean
      id: string
      id_t: string
      installment_number: string
      installment_value: integer|number
      is_blocked: boolean
      last_four_card_digits: string <numeric_string>
      merchant: string
      merchant_document: string <phone>
      merchant_user_email: string <email>
      not_anticipatable: boolean
      nsu: string <numeric_string>
      payed_value: integer|number
      payment_brand: string
      plan_type: string
      processor: string
      product: string
      receipt_id: string
      retention_reason: string
      retention_value: integer|number
      separated_payment_value: integer|number
      status: string
      transaction_date: string <datetime_iso>
      transaction_number: string <numeric_string>
      transaction_value: integer|number
      type: string
      updated: string <datetime_iso>
      ur_external_reference: string
      user_name: string
      value: integer|number
  releases: array
    releases[*]: object
      collection_id: string
      collection_name: string
      created: string <datetime_iso>
      data: string <datetime_iso>
      descricao: string
      expand: object
      forma_pagamento: string
      fornecedor: string <phone>
      id: string
      id_r: string <numeric_string>
      origem: string
      parcela: string
      status: string
      tipo: string
      updated: string <datetime_iso>
      valor: integer|number
      vencimento: string <datetime_iso>
```

## Campos

### `root`

- **Tipo:** object
- **Ocorrências:** 1

### `root.finpet`

- **Tipo:** array
- **Ocorrências:** 1
- **Tamanho:** 7112 - 7112 items

### `root.finpet[]`

- **Tipo:** object
- **Ocorrências:** 7112

### `root.finpet[].anticipate_value`

- **Tipo:** integer
- **Ocorrências:** 7112
- **Range:** 0 → 0
- **Exemplos:** `0`

### `root.finpet[].authorization_number`

- **Tipo:** string
- **Formato:** numeric_string
- **Ocorrências:** 7112
- **Comprimento:** 6 - 6 chars
- **Exemplos:** `571150`, `064012`, `001989`

### `root.finpet[].bank`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 4 - 35 chars
- **Exemplos:** `Banco Cooperativo do Brasil S.A.`, `Santander`, `Banco do Brasil`

### `root.finpet[].bank_agency`

- **Tipo:** string
- **Formato:** numeric_string
- **Ocorrências:** 7112
- **Comprimento:** 4 - 6 chars
- **Exemplos:** `3214`, `0289`, `0269-0`

### `root.finpet[].beneficiary`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 13 - 67 chars
- **Exemplos:** `Oftalmologia Veterinaria Mamede E Tasso LTDA FINPET`, `CANCELADO F A Molezini Atividades Veterinarias`, `Ivan Ricardo Martinez Padua`

### `root.finpet[].beneficiary_document`

- **Tipo:** string
- **Formato:** phone
- **Ocorrências:** 7112
- **Comprimento:** 11 - 14 chars
- **Exemplos:** `14371342000122`, `34430190000107`, `23325617816`

### `root.finpet[].beneficiary_type`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 21 - 21 chars
- **Exemplos:** `PAYMENT_TYPE_MERCHANT`, `PAYMENT_TYPE_SUPPLIER`

### `root.finpet[].beneficiary_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 5181.62
- **Exemplos:** `811.26`, `435.29`, `352.87`

### `root.finpet[].client_name`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 2 - 41 chars
- **Exemplos:** `RENATA G BOCCHI`, `ROSSANA REINEHR`, `CLIENT_NOT_INFORMED`

### `root.finpet[].client_phone`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 0 - 15 chars
- **Exemplos:** ``, `(69) 9388-3737`, `(16) 99400-8755`

### `root.finpet[].collection_id`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 16 - 16 chars
- **Exemplos:** `a7b3c9d2e5f8g1h4`

### `root.finpet[].collection_name`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 6 - 6 chars
- **Exemplos:** `finpet`

### `root.finpet[].cpf`

- **Tipo:** string
- **Formato:** phone
- **Ocorrências:** 7112
- **Comprimento:** 0 - 11 chars
- **Exemplos:** ``, `99540770220`, `37131996807`

### `root.finpet[].created`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 7112
- **Comprimento:** 19 - 19 chars
- **Exemplos:** `2025-12-11 11:18:19`, `2025-12-11 11:18:20`, `2025-12-11 11:18:21`

### `root.finpet[].currency`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 3 - 3 chars
- **Exemplos:** `BRL`

### `root.finpet[].date_estimated`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 7112
- **Comprimento:** 24 - 24 chars
- **Exemplos:** `2025-06-16 00:00:00.000Z`, `2025-06-17 00:00:00.000Z`, `2025-06-18 00:00:00.000Z`

### `root.finpet[].date_received`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 7112
- **Comprimento:** 0 - 24 chars
- **Exemplos:** `2025-06-16 00:00:00.000Z`, `2025-06-15 00:00:00.000Z`, `2025-06-17 00:00:00.000Z`

### `root.finpet[].deposit_account`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 6 - 13 chars
- **Exemplos:** `53790-0`, `013012707-4`, `33868-0`

### `root.finpet[].deposit_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 5181.62
- **Exemplos:** `811.26`, `435.29`, `352.87`

### `root.finpet[].discounted_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 350.86
- **Exemplos:** `26.74`, `10.21`, `10.13`

### `root.finpet[].due_date`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 7112
- **Comprimento:** 24 - 24 chars
- **Exemplos:** `2025-06-16 00:00:00.000Z`, `2025-06-17 00:00:00.000Z`, `2025-06-18 00:00:00.000Z`

### `root.finpet[].expand`

- **Tipo:** object
- **Ocorrências:** 7112

### `root.finpet[].fee`

- **Tipo:** number
- **Ocorrências:** 7112
- **Range:** 1.1 → 3.69
- **Exemplos:** `3.19`, `2.29`, `2.79`

### `root.finpet[].gross_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0.62 → 7583.86
- **Exemplos:** `811.26`, `435.29`, `352.87`

### `root.finpet[].has_chargeback`

- **Tipo:** boolean
- **Ocorrências:** 7112
- **Exemplos:** `False`, `True`

### `root.finpet[].has_contract_applied`

- **Tipo:** boolean
- **Ocorrências:** 7112
- **Exemplos:** `False`

### `root.finpet[].id`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 16 - 16 chars
- **Exemplos:** `dac2aucbz62ctvks`, `wlzwde8ua0uvzli5`, `xebn0x7nb3hlz9sy`

### `root.finpet[].id_t`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 12 - 14 chars
- **Exemplos:** `MjAwNDQyNjYw`, `MjA3Mjk0Mzkw`, `MjEwODkyNDQw`

### `root.finpet[].installment_number`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 3 - 5 chars
- **Exemplos:** `7/10`, `5/6`, `4/5`

### `root.finpet[].installment_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 1 → 7668.21
- **Exemplos:** `838`, `445.5`, `363`

### `root.finpet[].is_blocked`

- **Tipo:** boolean
- **Ocorrências:** 7112
- **Exemplos:** `False`

### `root.finpet[].last_four_card_digits`

- **Tipo:** string
- **Formato:** numeric_string
- **Ocorrências:** 7112
- **Comprimento:** 0 - 4 chars
- **Exemplos:** `2030`, `7078`, `5463`

### `root.finpet[].merchant`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 51 - 51 chars
- **Exemplos:** `Oftalmologia Veterinaria Mamede E Tasso LTDA FINPET`

### `root.finpet[].merchant_document`

- **Tipo:** string
- **Formato:** phone
- **Ocorrências:** 7112
- **Comprimento:** 14 - 14 chars
- **Exemplos:** `14371342000122`

### `root.finpet[].merchant_user_email`

- **Tipo:** string
- **Formato:** email
- **Ocorrências:** 7112
- **Comprimento:** 22 - 22 chars
- **Exemplos:** `fabriciovm@hotmail.com`

### `root.finpet[].not_anticipatable`

- **Tipo:** boolean
- **Ocorrências:** 7112
- **Exemplos:** `True`

### `root.finpet[].nsu`

- **Tipo:** string
- **Formato:** numeric_string
- **Ocorrências:** 7112
- **Comprimento:** 6 - 12 chars
- **Exemplos:** `500527`, `466256`, `000042`

### `root.finpet[].payed_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 5181.62
- **Exemplos:** `811.26`, `435.29`, `352.87`

### `root.finpet[].payment_brand`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 3 - 18 chars
- **Exemplos:** `Visa`, `MasterCard`, `MasterCard Maestro`

### `root.finpet[].plan_type`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 23 - 23 chars
- **Exemplos:** `FULL_STANDARD_PLAN_TYPE`

### `root.finpet[].processor`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 10 - 10 chars
- **Exemplos:** `PagService`

### `root.finpet[].product`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 3 - 6 chars
- **Exemplos:** `POS`, `INVITE`

### `root.finpet[].receipt_id`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 12 - 14 chars
- **Exemplos:** `MjAwNDQyNjYw`, `MjA3Mjk0Mzkw`, `MjEwODkyNDQw`

### `root.finpet[].retention_reason`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 0 - 36 chars
- **Exemplos:** ``, `Retenção sobre Split Finpet`, `MONTHLY_PAYMENT`

### `root.finpet[].retention_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 339.7
- **Exemplos:** `0`, `152.54`, `65.44`

### `root.finpet[].separated_payment_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 5233.29
- **Exemplos:** `0`, `259.76`, `402.04`

### `root.finpet[].status`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 4 - 17 chars
- **Exemplos:** `PAID`, `SCHEDULED_PAYMENT`, `UNPAID`

### `root.finpet[].transaction_date`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 7112
- **Comprimento:** 24 - 24 chars
- **Exemplos:** `2024-11-14 00:00:00.000Z`, `2025-01-15 00:00:00.000Z`, `2025-02-13 00:00:00.000Z`

### `root.finpet[].transaction_number`

- **Tipo:** string
- **Formato:** numeric_string
- **Ocorrências:** 7112
- **Comprimento:** 19 - 19 chars
- **Exemplos:** `4867838524111451721`, `5009044725011551721`, `5082004225021351721`

### `root.finpet[].transaction_value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 1 → 9610
- **Exemplos:** `8380`, `2673`, `1815`

### `root.finpet[].type`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 8 - 8 chars
- **Exemplos:** `MERCHANT`, `SUPPLIER`

### `root.finpet[].updated`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 7112
- **Comprimento:** 19 - 19 chars
- **Exemplos:** `2025-12-11 19:46:05`, `2025-12-11 19:46:06`, `2025-12-11 19:46:07`

### `root.finpet[].ur_external_reference`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 36 - 42 chars
- **Exemplos:** `14371342000122_20250616_VCC_14371342000122`, `14371342000122_20250616_MCC_14371342000122`, `34430190000107_20250616_MCC_34430190000107`

### `root.finpet[].user_name`

- **Tipo:** string
- **Ocorrências:** 7112
- **Comprimento:** 23 - 23 chars
- **Exemplos:** `Fabricio Villela Mamede`

### `root.finpet[].value`

- **Tipo:** integer, number
- **Ocorrências:** 7112
- **Range:** 0 → 7583.86
- **Exemplos:** `811.26`, `435.29`, `352.87`

### `root.releases`

- **Tipo:** array
- **Ocorrências:** 1
- **Tamanho:** 28120 - 28120 items

### `root.releases[]`

- **Tipo:** object
- **Ocorrências:** 28120

### `root.releases[].collection_id`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 13 - 13 chars
- **Exemplos:** `pbc_953728200`

### `root.releases[].collection_name`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 8 - 8 chars
- **Exemplos:** `releases`

### `root.releases[].created`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 28120
- **Comprimento:** 19 - 19 chars
- **Exemplos:** `2025-12-14 17:10:54`, `2025-12-14 17:10:55`, `2025-12-14 17:10:56`

### `root.releases[].data`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 28120
- **Comprimento:** 0 - 24 chars
- **Exemplos:** `2025-10-15 00:00:00.000Z`, `2025-10-16 00:00:00.000Z`, `2025-10-17 00:00:00.000Z`

### `root.releases[].descricao`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 3 - 502 chars
- **Exemplos:** `Água/saerp`, `Seguro Clinica - Seguro clinica`, `COMBUSTIVEL`

### `root.releases[].expand`

- **Tipo:** object
- **Ocorrências:** 28120

### `root.releases[].forma_pagamento`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 0 - 0 chars
- **Exemplos:** ``

### `root.releases[].fornecedor`

- **Tipo:** string
- **Formato:** phone
- **Ocorrências:** 28120
- **Comprimento:** 0 - 80 chars
- **Exemplos:** `SAERP`, `A MAIS AFINIDADESBoleto`, `POSTO MONTE CARLO LTDABoleto`

### `root.releases[].id`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 15 - 15 chars
- **Exemplos:** `ty0imyuhef2dli3`, `na0oriu8up32y9g`, `72xur1b48ulvl3l`

### `root.releases[].id_r`

- **Tipo:** string
- **Formato:** numeric_string
- **Ocorrências:** 28120
- **Comprimento:** 9 - 9 chars
- **Exemplos:** `300982841`, `311387555`, `312556125`

### `root.releases[].origem`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 0 - 3 chars
- **Exemplos:** ``, `VEN`, `COM`

### `root.releases[].parcela`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 0 - 8 chars
- **Exemplos:** `...`, `11 de 13`, `3 de 8`

### `root.releases[].status`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 1 - 1 chars
- **Exemplos:** `V`, `P`, `A`

### `root.releases[].tipo`

- **Tipo:** string
- **Ocorrências:** 28120
- **Comprimento:** 7 - 7 chars
- **Exemplos:** `despesa`, `receita`

### `root.releases[].updated`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 28120
- **Comprimento:** 19 - 19 chars
- **Exemplos:** `2025-12-14 17:10:54`, `2025-12-14 17:10:55`, `2025-12-14 17:10:56`

### `root.releases[].valor`

- **Tipo:** integer, number
- **Ocorrências:** 28120
- **Range:** -481745.32 → 481745.32
- **Exemplos:** `-366.5`, `-110.35`, `-684.71`

### `root.releases[].vencimento`

- **Tipo:** string
- **Formato:** datetime_iso
- **Ocorrências:** 28120
- **Comprimento:** 24 - 24 chars
- **Exemplos:** `2025-10-15 00:00:00.000Z`, `2025-10-16 00:00:00.000Z`, `2025-10-17 00:00:00.000Z`
