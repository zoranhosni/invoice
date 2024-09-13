from flet import (
    Page
)
from controller.invoice import InvoiceController

class MainApp:
    """
    Main application class
    """

    def __init__(self, controller: InvoiceController, page: Page):

        self.page = page
        self.controller = controller

        self.page.title = "Invoice App"

        self.create_interface()
    
    def create_interface(self):
        self.page.update()

