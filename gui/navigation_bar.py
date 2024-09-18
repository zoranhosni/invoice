from flet import (
    UserControl,
    NavigationBar,
    NavigationDestination,
    icons,
    RouteChangeEvent,
    Page,
    DataTable,
    DataColumn,
    Text,
)
from view.invoice import InvoiceView


class AppNavigationBar(NavigationBar):
    
    def __init__(self, controller, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller
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
        print(self.selected_index)
        if self.selected_index == 0:
            view = InvoiceView(controller=self.controller)
            self.page.add(view)
            # self.page.add(
            #     DataTable(
            #         columns=[
            #             DataColumn(Text("First name")),
            #             DataColumn(Text("Last name")),
            #             DataColumn(Text("Age"), numeric=True),
            #         ],
            #     )
            # )
            
        

