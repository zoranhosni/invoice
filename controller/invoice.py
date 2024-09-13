from controller.main import AppController
from factory.main import ObjectBuilder
from flet import app
import database.db_manager
import config.config_json  # to register JSON config creator


CONFIG_FORMAT = 'json'


class InvoiceController(AppController):
    """
    Invoice Controller Instance
    """
    def __init__(self):
        super().__init__()
        self.config = ObjectBuilder(object_format=CONFIG_FORMAT).build().as_object()
        self.db_manager = database.db_manager.DBManager(db_path=self.config.database.path)


    def run(self):
        # Start GUI
        from gui.main import MainApp
        app(target=lambda page: MainApp(controller=self, page=page))
    
    def release(self):
        self.db_session = None

    def exit(self):
        self.release()
        exit(0)