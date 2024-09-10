from datetime import datetime


class Invoice:

    def __init__(
            self,
            invoice_id: str,
            issue_date: datetime,
            items: list
        ) -> None:
        
        self.invoice_id = invoice_id
        self.issue_date = issue_date
        self.items = items
    
    def total(self) -> float:
        pass