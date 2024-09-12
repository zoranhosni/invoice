from flet import (
    Page
)


class MainApp:

    def __init__(self, db_session, page: Page):

        self.page = page
        self.db_session = db_session

        self.page.title = "Invoice App"

        self.create_interface()
    
    def create_interface(self):
        self.page.update()

