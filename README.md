# Cortana

## Usage

This section explains how to interact with Cortana.

**IMPORTANT** -- All files and bash commands are executed from the root directory of the project.

Create a `.env` file with the following content.
Do not commit this file.

```conf
DISC_APP_KEY  = ""
NGROK_API_KEY = ""
```

### Docker

Run using:

```bash
docker compose -f docker-compose.yml up -d --force-recreate
```

## Development

This will install all the required dependencies:

```bash
pip install -r requirements.txt
```

Run using:

```bash
python ./src/main.py
```

## Useful links

- [ngrok->api-endpoints](https://ngrok.com/docs/api/resources/endpoints/)
