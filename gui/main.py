from flet import (
    Page,
    NavigationBar,
    NavigationDestination,
    icons,
)
from controller.invoice import InvoiceController
from gui.navigation_bar import AppNavigationBar


class MainApp:
    """
    Main application class
    """

    def __init__(self, controller: InvoiceController, page: Page):

        self.page = page
        self.controller = controller
        self.page.title = "Invoice App"
        # self.navigation_bar = AppNavigationBar()
        self.page.update()
        self.create_interface()
    
    def create_interface(self):
        self.page.navigation_bar = NavigationBar(
            destinations=[
                NavigationDestination(label="Invoices", icon=icons.BUSINESS),
                NavigationDestination(label="Products", icon=icons.PRODUCTION_QUANTITY_LIMITS)
            ]
        )
        # self.page.navigation_bar = AppNavigationBar()
        self.page.update()
