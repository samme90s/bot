FROM python:3.12.3-slim

WORKDIR /code/

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Adds all files from `src/` to `code/` in the image.
COPY ./src/ /code/

CMD ["python", "main.py"]
