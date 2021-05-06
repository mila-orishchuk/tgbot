from entities import BaseEntity


class Measurement(BaseEntity):
    unit: str
    amount: int
    metric_unit: str

    def __init__(self, data: dict):
        self.unit = data['unit']
        self.amount = data['amount']
        self.metric_unit = data['metric_unit']
