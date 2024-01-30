FROM python:3.9-alpine3.13
LABEL maintainer="jackkower.com"

ENV PYTHONBUFFERED 1

COPY /requirements.txt /tmp/
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
COPY requirements.dev.txt /tmp/
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.dev.txt && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
RUN /py/bin/flake8 --version

# CMD ["flake8", "."]


ENV PATH="/py/bin:$PATH"

USER django-user