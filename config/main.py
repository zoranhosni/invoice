import logging

LOG = logging.getLogger(__name__)


class ConfigException(Exception):
    """
    Base Config Exception class
    """
    pass


class Config(object):
    """
    Base Config class configured as a singleton class
    """

    __CONFIG_FILE = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        pass

    def as_dict(self, *args, **kwargs):
        pass

    def as_object(self, *args, **kwargs):
        pass
