import logging
import json
from json import JSONEncoder
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

from factory.main import object_factory
from config.main import (
    ConfigException,
    Config,
)

LOG = logging.getLogger(__name__)


class ConfigEncoder(JSONEncoder):
    """
    Helper Config class for JSON encoder
    """
    def default(self, o):
        return o.__dict__


class ConfigJson(Config):
    """
    Config JSON class
    """

    __CONFIG_FILE = 'config/.config.json'

    def __init__(self):
        super().__init__()
        try:
            with open(self.__CONFIG_FILE, 'r', encoding='utf-8') as cf:
                self.config = json.load(cf)
                self.config_file = self.__CONFIG_FILE
                LOG.debug(f'Config file: {self.config_file}')
                LOG.debug(f'Config loaded: {self.config}')
        except FileNotFoundError:
            raise ConfigException(f'Config file not found: {self.__CONFIG_FILE}')

    def as_dict(self):
        return self.config

    def as_object(self):
        return json.loads(json.dumps(self.config, indent=4, cls=ConfigEncoder), object_hook=lambda d: Namespace(**d))


# Register JSON config creator
object_factory.register_format(object_format='json', object_creator=ConfigJson)
