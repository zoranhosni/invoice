from flet import (
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

        ids = [row.id for row in rows]
        print(f'IDs: {ids}')

        issue_dates = [row.issue_date for row in rows]
        print(f'Issue dates: {issue_dates}')

        self.columns = [
            DataColumn(Text(column, size=12, color="black")) for column in columns
        ]

        self.last_row = DataRow(
            cells=[
                DataCell(Text("")),
                DataCell(TextField(hint_text="Enter Issue date here", expand=True)),
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
