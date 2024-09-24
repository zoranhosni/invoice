from flet import (
    NavigationBar,
    NavigationDestination,
    icons,
    RouteChangeEvent,
    Page,
)
from view.invoice import InvoiceView
from view.product import ProductView
from controller.invoice import InvoiceController
from controller.product import ProductController


class AppNavigationBar(NavigationBar):
    
    def __init__(self, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.destinations = [
            NavigationDestination(
                icon=icons.INVENTORY, label="Invoices"
            ),
            NavigationDestination(
                icon=icons.PRODUCTION_QUANTITY_LIMITS, label="Products"
            )
        ]
        self.on_change=self.navigation_change
        self.selected_index = 0
        self.bgcolor="blue"

    def navigation_change(self, e: RouteChangeEvent) -> None:
        self.selected_index = e.control.selected_index
        print(f'Selected index: {self.selected_index}')

        # Remove last view
        self.page.controls.pop() if self.page.controls else None
        view = None

        if self.selected_index == 0:
            view = InvoiceView(controller=InvoiceController())        
            
        elif self.selected_index == 1:
            view = ProductView(controller=ProductController())
        
        self.page.add(view)
