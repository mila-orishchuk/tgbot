class BaseEntity:
    id: int

    def __init__(self, data: dict):
        if 'id' in data:
            self.id = data['id']

