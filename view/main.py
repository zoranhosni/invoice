from typing import List
from flet import (
    UserControl,
)


class View(UserControl):

    def __init__(self):
        super().__init__()

        self.data_table = DataTable()

    def build(self):
        pass
