from sqlalchemy import Column, String, Integer, Table, DateTime, ForeignKey
from base import Base
from sqlalchemy.orm import relationship, backref


association_table = Table('recipe_ingredients', Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('recipe_id', Integer, ForeignKey(
                              'recipe.id', ondelete="CASCADE")),
                          Column('ingredient_id', Integer, ForeignKey(
                              'ingredient.id', ondelete="CASCADE"))
                          )


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(256))
    url = Column('url', String(256))
    image = Column('image', String(256))
    ingredients = relationship(
        "Ingredient",
        secondary=association_table,
        back_populates="recipes",
        cascade="all, delete",
    )
    cooking_time = Column('cooking_time', String(256))
    history = relationship("History", backref="recipe", passive_deletes=True)

    # def __init__(self, name, image, url, ingredients, cooking_time):
    #     self.name = name
    #     self.image = image
    #     self.url = url
    #     self.ingredients = ingredients
    #     self.cooking_time = cooking_time

    def __repr__(self):
        return self.name


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(256))
    description = Column('description', String(256))
    recipes = relationship(
        "Recipe",
        secondary=association_table,
        back_populates="ingredients",
        passive_deletes=True
    )

    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description

    def __repr__(self):
        return self.name


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    recipe_id = Column('recipe_id', Integer, ForeignKey(
        "recipe.id", ondelete='CASCADE'))
    user_id = Column('user_id', Integer)
    date = Column('date', DateTime)
    choise = Column('choise', Integer)

    # def __init__(self, name, description):
    #     self.name = name
    #     self.description = description

    def __repr__(self):
        return self.choise
