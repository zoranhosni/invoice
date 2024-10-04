from typing import List
from controller.main import AppController
from database.product import (
    Product,
    get_rows,
    get_columns,
)


class ProductController(AppController):
    """
    Invoice Controller Instance
    """
    def __init__(self):
        super().__init__()
    
    def get_columns(self):
        columns = get_columns()
        columns = [column.replace('_', ' ').capitalize() for column in columns]
        return columns

    def get_rows(self) -> List[Product] :
        return get_rows(db_path=self.db_path)
    