import logging

LOG = logging.getLogger(__name__)


class ObjectFactory(object):
    """
    Object factory class
    """

    def __init__(self):
        self._creators = {}

    def register_format(self, object_format, object_creator):
        self._creators[object_format] = object_creator
        LOG.debug(f'Format {object_format} registered by {object_creator}')

    def get_creator(self, object_format):
        creator = self._creators.get(object_format, None)
        if creator is None:
            raise ValueError(f'Format {object_format} is not supported by the Object Factory')
        return creator


object_factory = ObjectFactory()


class ObjectBuilder(object):
    """
    Object builder class
    """
    
    def __init__(self, object_format):
        self._creator = object_factory.get_creator(object_format=object_format)
        self._format = object_format

    def build(self, *args, **kwargs):
        LOG.debug(f'Object build creator: {self._creator}')
        return self._creator(*args, **kwargs)
