# API de Upload e Download

API REST desenvolvida em Python com Flask para enviar, listar e baixar arquivos.

## Tecnologias
- Python 3
- Flask
- SQLite
- Gunicorn (servidor de produção)
- Render (hospedagem)

## Requisitos
- Python 3.10 ou superior
- pip

## Executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
   cd SEU-REPOSITORIO
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Inicie a API:
   ```bash
   python app.py
   ```
5. Acesse `http://localhost:5000/` ou `http://localhost:5000/health`.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Informações básicas da API |
| GET | `/health` | Verificação de saúde |
| POST | `/upload` | Envia um arquivo |
| GET | `/uploads` | Lista os arquivos registrados |
| GET | `/download/<filename>` | Baixa um arquivo enviado |

### Enviar arquivo

Faça uma requisição `POST` para `/upload` usando `multipart/form-data`, com o campo `file`.

Exemplo com cURL:

```bash
curl -X POST http://localhost:5000/upload \
  -F "file=@./exemplo.pdf"
```

A API responde com os dados do arquivo e uma URL de download.

### Listar arquivos

```bash
curl http://localhost:5000/uploads
```

### Baixar arquivo

Use o nome armazenado retornado no upload:

```bash
curl -OJ http://localhost:5000/download/NOME_DO_ARQUIVO
```

## Configurações

As configurações podem ser definidas por variáveis de ambiente:

| Variável | Padrão | Finalidade |
|---|---|---|
| `PORT` | `5000` | Porta local |
| `UPLOAD_FOLDER` | `uploads` | Pasta dos arquivos |
| `DATABASE_PATH` | `instance/uploads.db` | Caminho do banco SQLite |
| `MAX_CONTENT_LENGTH` | `16777216` | Limite de upload em bytes (16 MB) |

## Publicação no Render

O arquivo `render.yaml` configura o serviço web, o comando de inicialização com Gunicorn, a rota de health check e um disco persistente para os arquivos e o banco SQLite.

1. Envie o projeto para um repositório GitHub.
2. No Render, escolha **New + → Blueprint** (ou crie um **Web Service** conectado ao repositório).
3. Se usar Blueprint, o Render lê as configurações do `render.yaml`.
4. Aguarde o deploy terminar.
5. Abra a URL pública gerada e teste `/health`, `/upload`, `/uploads` e `/download/<filename>`.

> Observação: o disco persistente configurado no `render.yaml` depende de um plano do Render que ofereça Persistent Disk. Se o plano escolhido não permitir disco, configure armazenamento externo ou aceite que arquivos e banco local podem ser perdidos em reinicializações/redeploys. Confirme os recursos e custos atuais no painel do Render.

## Observações de segurança

- Os nomes dos arquivos armazenados são gerados aleatoriamente para evitar colisões.
- O nome original é sanitizado antes de ser usado.
- O limite padrão de upload é 16 MB.
- Para uso público real, recomenda-se autenticação, controle de tipos de arquivo, limites de taxa e armazenamento de objetos.

## Autor
Preencha com seu nome e turma antes de entregar.
