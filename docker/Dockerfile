FROM python:3.12.1-slim-bookworm as builder

ENV PATH $PATH:/root/.local/bin
ENV PYTHONUNBUFFERED TRUE

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN --mount=target=/local_wheels,source=wheels \
    pip3 install --no-compile --user /local_wheels/*.whl

FROM python:3.12.1-slim-bookworm

COPY --from=builder /root/.local /root/.local

ENV PATH $PATH:/root/.local/bin
ENV PYTHONUNBUFFERED TRUE

ENTRYPOINT ["slackutils"]
