""" Implement the cmd1 command.

"""
from ..core.config import YamlConfig
from ..core.logger import logger


def main(name, config: YamlConfig):
    """ Execute the command.
    
    :param name: name to use in greeting
    """
    logger.debug("executing cmd1 command")
    print("Hello, {:s}!".format(name))
    return
