FROM themattrix/tox-base

RUN apt-get update && apt-get install -y git-core mercurial

# Update pyenv for access to newer Python releases.
RUN cd /.pyenv \
    && git fetch \
    && git checkout v1.2.8

ENV = PYPY3_VERSION=pypy3.6-5.10.1

# install a newer version op pypy and pypy3 that doesn't have troubles
RUN pyenv install "$PYPY_VERSION"
RUN pyenv install "$PYPY3_VERSION"

# only install certain versions for tox to use
RUN pyenv versions
RUN pyenv global system 3.6.6 3.7.0 "$PYPY_VERSION" "$PYPY3_VERSION"

ENV PYTHONDONTWRITEBYTECODE = 1  # prevent *.pyc files

WORKDIR /code
COPY . .
CMD tox
