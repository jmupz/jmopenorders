# -*- coding: utf-8 -*-
from ..core.logger import logger


def hello(name: str = "World") -> str:
    logger.debug("executing hello command")

    return "Hello, {:s}!".format(name)  # TODO: use f-string for python 3.6+
