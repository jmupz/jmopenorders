FROM themattrix:tox-base

RUN apt-get update  \
    && apt-get install -y git-core mercurial --no-install-recommends \
    && apt-get clean \
    && rm -rf  /var/lib/apt/lists/* \
    && rm -rf /tmp/* /var/tmp/*

# Update pyenv for access to newer Python releases.
RUN cd /.pyenv \
    && git fetch \
    && git checkout v1.2.8

ENV PYPY3_VERSION=pypy3.6-5.10.1

# install a newer version op pypy and pypy3 that doesn't have troubles
RUN pyenv install "$PYPY_VERSION"
RUN pyenv install "$PYPY3_VERSION"

# only install certain versions for tox to use
RUN pyenv versions
RUN pyenv global system 3.6.6 3.7.0 "$PYPY_VERSION" "$PYPY3_VERSION"

# prevent *.pyc files
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code
COPY . .
CMD tox

EXPOSE 80/udp
