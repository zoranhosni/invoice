from controller.main import AppController
from factory.main import ObjectBuilder


CONFIG_FORMAT = 'json'


class InvoiceController(AppController):
    """
    Invoice Controller Instance
    """
    def __init__(self):
        super().__init__()
        self.config = ObjectBuilder(object_format=CONFIG_FORMAT).build().as_object()


    def run(self):
        pass
    
    def release(self):
        self.config = None

    def exit(self):
        self.release()
        exit(0)