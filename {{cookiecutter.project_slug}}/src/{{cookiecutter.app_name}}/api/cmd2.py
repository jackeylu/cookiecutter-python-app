""" Implement the cmd2 command.

"""
from ..core.config import YamlConfig
from ..core.logger import logger


def main(name, config: YamlConfig):
    """ Execute the command.
    
    """
    logger.debug("executing cmd2 command")
    print("Hello, {:s}!".format(name))
    return
