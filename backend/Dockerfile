FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml README.md ./
COPY app ./app

RUN pip install poetry==1.8.4 && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

ENTRYPOINT [ "uvicorn" ]
