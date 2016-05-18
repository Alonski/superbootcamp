import logging

logger = logging.getLogger(__name__)


def foo():
    logger.debug("Entered foo!")
    logger.critical("OH NO!")
    return 123


def bar():
    return 456

print("mymodule ended")
