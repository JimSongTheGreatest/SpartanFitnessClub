FROM openjdk:8-slim
FROM python:3.10.4-slim-bullseye

RUN groupadd --gid 1000 pn && useradd --uid 1000 --gid pn --shell /bin/bash --create-home pn
ENV POETRY_HOME=/usr/local
RUN \
  pip install -U pip && pip install pipenv && \
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - && \
  rm -rf /var/lib/apt/lists/*

RUN apt update && apt -y install git git-lfs

ENV JAVA_HOME=/usr/local/openjdk-8
COPY --from=openjdk:8-slim $JAVA_HOME $JAVA_HOME
ENV PATH="${JAVA_HOME}/bin:${PATH}"

CMD ["/bin/bash"]
