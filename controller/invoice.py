from controller.main import AppController
from factory.main import ObjectBuilder
from database.db_manager import DBManager
from flet import app
import config.config_json


CONFIG_FORMAT = 'json'


class InvoiceController(AppController):
    """
    Invoice Controller Instance
    """
    def __init__(self):
        super().__init__()
        self.config = ObjectBuilder(object_format=CONFIG_FORMAT).build().as_object()
        self.db_session = DBManager(db_path=self.config.database.path).connect()


    def run(self):
        # Start GUI
        from gui.main import MainApp
        app(target=lambda page: MainApp(db_session=self.db_session, page=page))
    
    def release(self):
        self.db_session = None

    def exit(self):
        self.release()
        exit(0)