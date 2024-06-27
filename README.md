# Raspi

## Development

Run using:

```bash
pip install -r requirements.txt &&
python ./src/main.py
```

## Usage

**IMPORTANT** -- All commands are executed from the root directory of the project.

```bash
touch .env
```

Copy the following content into the file and update the values with correct credentials:

```conf
# .env
#
# ******************** IMPORTANT! ********************
# *** This file should never be version controlled ***
# ****************************************************

DISC_APP_KEY  = ""
NGROK_API_KEY = ""
```

### Docker

**IMPORTANT** -- Make sure the `.env` is located in the same directory as the `docker-compose.yml` file.

Run using:

```bash
# This ensures that the latest images are pulled and the containers are recreated.
sudo docker compose pull &&
sudo docker compose -f docker-compose.yml up -d --force-recreate &&
sudo docker system prune -a --volumes -f
```
