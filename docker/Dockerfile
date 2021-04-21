FROM python:3.8-slim

ENV PATH $PATH:/root/.local/bin
ENV PYTHONUNBUFFERED TRUE

RUN --mount=target=/local_wheels,source=wheels \
    pip3 install --no-compile --user /local_wheels/*.whl

ENTRYPOINT ["slackutils"]
