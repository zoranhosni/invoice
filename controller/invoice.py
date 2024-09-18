from typing import List
from controller.main import AppController
from factory.main import ObjectBuilder
from flet import app
from database.invoice import (
    Invoice,
    get_rows,
    get_columns,
)
import config.config_json  # to register JSON config creator


CONFIG_FORMAT = 'json'


class InvoiceController(AppController):
    """
    Invoice Controller Instance
    """
    def __init__(self):
        super().__init__()
        self.config = ObjectBuilder(object_format=CONFIG_FORMAT).build().as_object()
        self.db_path=self.config.database.path


    def run(self):
        # Start GUI
        from gui.main import MainApp
        app(target=lambda page: MainApp(controller=self, page=page))
    
    def get_columns(self):
        return get_columns(db_path=self.db_path)

    def get_rows(self) -> List[Invoice] :
        return get_rows(db_path=self.db_path)
    
    def release(self):
        self.db_session = None

    def exit(self):
        self.release()
        exit(0)
    