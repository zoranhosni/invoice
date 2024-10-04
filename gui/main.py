from flet import (
    Page,
    CrossAxisAlignment
)
from gui.navigation_bar import AppNavigationBar


class MainApp:
    """
    Main application class
    """

    def __init__(self, page: Page):

        self.page = page
        self.page.title = "Invoice App"
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.update()
        self.create_interface()
    
    def create_interface(self):
        self.page.navigation_bar = AppNavigationBar(page=self.page)
        self.page.update()
