# Extração de APIs (Bitcoin & NASA)

Este repositório contém scripts Python simples para extrair dados de APIs públicas (Coinbase e NASA) e salvar medições de preço do BTC usando TinyDB.

**Conteúdo**
- **Descrição:** Coleção de scripts para demonstração de extração de APIs e persistência simples.
- **Principais arquivos:** [API_Bitcoin_1.py](API_Bitcoin_1.py), [API_Bitcoin_2.py](API_Bitcoin_2.py), [API_Bitcoin_3.py](API_Bitcoin_3.py), [API_Nasa.py](API_Nasa.py), [db.json](db.json)

**Requisitos**
- **Python:** 3.8+ recomendado
- **Pacotes:** `requests`, `tinydb`

Instalar dependências:

```bash
pip3 install requests tinydb
```

**Descrição dos scripts**
- [API_Bitcoin_1.py](API_Bitcoin_1.py): Faz uma requisição simples à API pública da Coinbase (endpoint de preços spot) e imprime o JSON de resposta.

- [API_Bitcoin_2.py](API_Bitcoin_2.py): Implementa um pequeno fluxo ETL:
	- `extrair()` — busca os dados da API Coinbase.
	- `trasnsformar()` — extrai `valor`, `criptomoeda`, `moeda` e adiciona `timestamp`.
	- `load()` — persiste o registro em [db.json](db.json) usando TinyDB.
	- Uso: executa uma única extração e salva o resultado.

- [API_Bitcoin_3.py](API_Bitcoin_3.py): Variante do ETL que executa em loop contínuo a cada 5 segundos, salvando sucessivas leituras em [db.json](db.json). Use com cuidado para não exceder limites de requisições.

- [API_Nasa.py](API_Nasa.py): Exemplo de requisição ao endpoint NEO Feed da NASA usando a `DEMO_KEY`. Substitua a chave por sua `NASA_API_KEY` para uso real.

**Formato do banco (db.json)**
O arquivo [db.json](db.json) é usado pelo TinyDB. Cada documento salvo tem a forma:

```json
{
	"valor": "<string>",
	"criptomoeda": "BTC",
	"moeda": "USD",
	"timestamp": "YYYY-MM-DDTHH:MM:SS.ssssss"
}
```

Exemplo de visualização rápida do conteúdo: abra [db.json](db.json) com um editor de texto.

**Como executar**

Executar uma única requisição (imprime JSON):

```bash
python3 API_Bitcoin_1.py
python3 API_Nasa.py
```

Executar ETL único (salva uma entrada em db.json):

```bash
python3 API_Bitcoin_2.py
```

Executar ETL em loop (salva repetidamente a cada 5s):

```bash
python3 API_Bitcoin_3.py
```

**Boas práticas e observações**
- Substitua a `DEMO_KEY` da NASA por uma chave real armazenada em variável de ambiente para produção.
- Evite rodar loops sem controle por longos períodos para não sobrecarregar a API.
- `tinydb` grava dados em JSON localmente; use um banco mais robusto para produção.

**Licença & Autor**
- Autor: (adicione seu nome aqui)
- Licença: sem licença especificada — adicione uma conforme necessário.

Se quiser, eu posso:
- adicionar instruções para usar uma `NASA_API_KEY` via variável de ambiente;
- criar um `requirements.txt` ou script de envio/commit automático.
