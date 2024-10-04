from typing import List
from controller.main import AppController
from database.invoice import (
    Invoice,
    get_rows,
    get_columns,
)


class InvoiceController(AppController):
    """
    Invoice Controller Instance
    """
    def __init__(self):
        super().__init__()
    
    def get_columns(self):
        columns = get_columns()
        columns = [column.replace('_', ' ').capitalize() for column in columns]
        return columns

    def get_rows(self) -> List[Invoice] :
        return get_rows(db_path=self.db_path)
    