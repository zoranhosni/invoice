import config.config_json  # to register JSON config creator
from factory.main import ObjectBuilder
from flet import app

CONFIG_FORMAT = 'json'


class AppController(object):
    """
    Main Application Controller Class
    """
    def __init__(self):
        self.config = ObjectBuilder(object_format=CONFIG_FORMAT).build().as_object()
        self.db_path=self.config.database.path

    def run(self):
        # Start GUI
        from gui.main import MainApp
        app(target=lambda page: MainApp(page=page))

    def exit(self):
        self.release()
        exit(0)

