from flet import (
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Text,
    TextField,
    border
)
from controller.product import ProductController


class ProductView(DataTable):

    def __init__(self, controller: ProductController, *args, **kwargs) -> None:
        self.controller = controller
        super().__init__(*args, **kwargs)

        columns = self.controller.get_columns()
        print(f'Columns: {columns}')
        
        rows = self.controller.get_rows()
        print(f'Rows: {rows}')
        
        ids = [row.id for row in rows]
        print(f'IDs: {ids}')
        
        names = [row.name for row in rows]
        print(f'Names: {names}')
        
        prices = [row.price for row in rows]
        print(f'Prices: {prices}')
        
        self.columns = [
            DataColumn(Text(column, size=12, color="black")) for column in columns
        ]
        
        self.last_row = DataRow(
            cells=[
                DataCell(Text("")),
                DataCell(TextField(hint_text="Enter product name here", expand=True)),
                DataCell(TextField(hint_text="Enter product price here", expand=True)),
                DataCell(TextField(hint_text="Enter invoice id here", expand=True)),
            ]
        )
        
        self.rows = [
            DataRow(
                cells=[
                    DataCell(Text(row)) for row in rows 
                ]
            )
        ] if len(rows) > 0 else []
        
        self.rows.append(self.last_row)
        print(f'Table rows: {self.rows}')
        
        self.expand = True
        self.border_radius = 8
        self.border = border.all(2, "#ebebeb")
        self.horizontal_lines = border.BorderSide(1, "#ebebeb")
        self.vertical_lines = border.BorderSide(1, "#ebebeb")
        