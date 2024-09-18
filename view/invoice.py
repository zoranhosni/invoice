from typing import List
from flet import (
    Row,
    DataTable,
    DataColumn,
    DataRow,
    DataCell,
    Text,
    TextField,
    border
)
from controller.invoice import InvoiceController


class InvoiceView(DataTable):

    def __init__(self, controller: InvoiceController, *args, **kwargs) -> None:
        self.controller = controller
        super().__init__(*args, **kwargs)

        columns = self.controller.get_columns()
        print(f'Columns: {columns}')

        rows = self.controller.get_rows()
        print(f'Rows: {rows}')

        ids = [item.id for item in rows]
        print(f'IDs: {ids}')

        issue_dates = [item.issue_date for item in rows]
        print(f'Issue dates: {issue_dates}')

        #self.columns = [DataColumnView(label=column, numeric=True if column.lower() == 'id' else False) for column in columns]
        self.columns = [
            DataColumn(Text(column.upper(), size=12, color="black")) for column in columns
        ]
        self.last_row = DataRow(
            cells=[
                DataCell(Text("ID will be updated automatically")),
                DataCell(TextField(hint_text="Enter Issue Date here", expand=True)),
            ]
        )
        self.rows = [
            DataRow(
                cells=[
                    DataCell(Text(item)) for item in rows 
                ]
            )
        ] if len(rows) > 0 else [self.last_row]

        self.rows += [self.last_row] if len(rows) > 0 else []

        self.expand = True
        self.border_radius = 8
        self.border = border.all(2, "#ebebeb")
        self.horizontal_lines = border.BorderSide(1, "#ebebeb")
    

    def build(self):
        return Row(
            controls=[
                self,
            ],
            expand=True,
        )

