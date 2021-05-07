from sqlalchemy import Column, String, Integer
from base import Base


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(256))
    url = Column('url', String(256))
    image = Column('image', String(256))
    cooking_time = Column('cooking_time', String(256))

    def __init__(self, name, image, url, cooking_time):
        self.name = name
        self.image = image
        self.url = url
        self.cooking_time = cooking_time

    def __repr__(self):
        return self.name