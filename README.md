# Relatório Operacional de Pré-Decolagem (Atividade Integradora)

Um programa para interpretar dados de telemetria em uma planilha e decidir se a nave está **pronta para decolar** ou se a **decolagem deve ser abortada**.

---

## Como Instalar / Rodar

1. Baixar o arquivo `.ipynb` (Interactive Python Notebook)  
2. Ter o Python instalado localmente ou importar no Google Colab  
3. Executar o arquivo  

---

## Como Usar

### Gerar Dados de Telemetria (Opcional)

Você pode pedir para uma IA gerar uma planilha CSV com dados de telemetria usando o prompt abaixo (substituindo os valores entre `{}`):

<details>
<summary>Clique para expandir o prompt</summary>

```
Aja como um engenheiro de dados especializado em sistemas aeroespaciais, com foco em simulação de telemetria da nave Starship.

Seu objetivo é gerar um dataset sintético em formato CSV que represente dados de telemetria realistas da Starship durante duas fases críticas: pré-decolagem e ignição dos motores.

Contexto:
A Starship utiliza propelentes criogênicos (metano e oxigênio líquido), motores Raptor e opera sob condições extremas de temperatura e pressão. O dataset será utilizado para simulações e testes de sistemas, portanto deve refletir comportamentos físicos plausíveis com base nessas características.

Instruções:
- Gere um dataset com no mínimo 201 linhas.
- Simule progressão temporal com timestamps sequenciais.
- Inclua duas fases:
  1. Pré-decolagem (sistemas estáveis, preparação)
  2. Ignição (mudanças bruscas em temperatura, pressão e consumo)
- Os dados devem evoluir de forma lógica e consistente.
- Evite valores aleatórios sem coerência física.

Colunas obrigatórias do CSV (usar exatamente estes nomes):
- Timestamp
- Temperatura interna e externa
- Integridade estrutural
- Níveis de energia
- Pressão dos tanques
- Status dos módulos críticos

Regras para os dados:

- temp_interna:
  - Tipo float
  - Deve variar entre {MIN_TEMP_INTERNA}°C e {MAX_TEMP_INTERNA}°C

- temp_externa:
  - Tipo float
  - Pré-decolagem: entre {MIN_TEMP_EXTERNA}°C e {MAX_TEMP_EXTERNA}°C

- integridade_estrutural:
  - Tipo booleano ({OK_INTEGRIDADE_ESTRUTURAL} para intacto e {FALHA_INTEGRIDADE_ESTRUTURAL} para falha)

- nivel_bateria:
  - Tipo float (percentual)
  - Próximo de 100% na pré-decolagem
  - Deve pelo menos {MIN_NIVEL_ENERGIA}% na ignição

- pressao_tanques:
  - Tipo float
  - Pré-decolagem: entre {MIN_PRESSAO_TANQUES} e {MAX_PRESSAO_TANQUES} bar
  - Ignição: aumento para aproximadamente 6.2 bar para alimentar os motores Raptor

- modulos_criticos:
  - Tipo booleano ({OK_MODULOS_CRITICOS} para OK e {FALHA_MODULOS_CRITICOS} para falha)

Regras adicionais:
- Deve haver uma transição clara entre pré-decolagem e ignição
- Os valores devem refletir o comportamento realista da Starship
- Use números decimais quando apropriado
- Mantenha consistência entre variáveis (ex: aumento de pressão antes da ignição, queda leve de bateria, aumento de consumo)

Formato da saída:
- Retorne apenas o CSV
- Inclua cabeçalho na primeira linha
- Use vírgula como separador
- Não inclua explicações, comentários ou qualquer texto fora do CSV
```

</details>

---

### Importar Dados

Executar o arquivo `.ipynb` e importar um arquivo CSV contendo as colunas:

```
timestamp,temperatura_interna,temperatura_externa,integridade_estrutural,nivel_energia,pressao_tanques,modulos_criticos
```

---

## Explicação do Código

### Bloco 1 — Definição de Limites

Define as faixas seguras para operação da nave:

- Temperatura interna e externa (mínimo e máximo aceitável)
- Integridade estrutural (OK ou Falha)
- Nível mínimo de energia da bateria
- Pressão segura dos tanques
- Status dos módulos críticos

Esses valores funcionam como faixas seguras que serão usadas para validar os dados antes da decolagem.

---

### Bloco 2a — Entrada Manual

Permite ao usuário inserir valores manualmente para teste:

- O programa solicita cada valor (temperatura interna, externa, integridade, energia, pressão e módulos)
- Realiza validações para garantir que os dados sejam válidos
- Caso haja erro, exibe mensagem e solicita nova entrada

---

### Bloco 2b — Entrada via CSV

Automatiza a entrada de dados com arquivo CSV:

- Utiliza um dataset com cenários variados
- Leitura feita com pandas
- Permite simular diversas condições reais rapidamente

---

### Bloco 3a — Validação Manual

Valida os dados inseridos pelo usuário:

- Compara cada variável com os limites definidos
- Caso algum valor esteja fora da faixa segura → Decolagem Abortada
- Caso tudo esteja correto → Pronto para Decolar

---

### Bloco 3b — Validação em Lote (CSV)

Valida automaticamente os dados do CSV:

- Percorre cada linha do arquivo
- Aplica as mesmas regras da validação manual

Resultados gerados:

- `resultado_final`: indica se foi aprovado ou abortado
- `motivo`: explica a falha, se houver

---

### Bloco 4a — Saída (Manual)

Exibe o resultado final com base nos dados inseridos manualmente.

---

### Bloco 4b — Saída (CSV)

Exibe o resultado final com base nos dados do arquivo CSV.

---

## Tecnologias

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)  
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

---

## Objetivo

Simular um sistema de checagem de segurança pré-lançamento, garantindo que a nave só decole sob condições ideais.
