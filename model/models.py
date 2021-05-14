from sqlalchemy import Column, String, Integer, Table, DateTime, ForeignKey
from base import Base
from sqlalchemy.orm import relationship, backref


recipes_ingredients_table = Table('recipes_ingredients', Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('recipe_id', Integer, ForeignKey(
                              'recipe.id', ondelete="CASCADE")),
                          Column('ingredient_id', Integer, ForeignKey(
                              'ingredient.id', ondelete="CASCADE"))
                          )

recipes_categories_table = Table('recipes_categories', Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('recipe_id', Integer, ForeignKey(
                              'recipe.id', ondelete="CASCADE")),
                          Column('category_id', Integer, ForeignKey(
                              'category.id', ondelete="CASCADE"))
                          )


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(256))
    url = Column('url', String(256), unique=True)
    image = Column('image', String(256))
    cooking_time = Column('cooking_time', String(256))
    ingredients = relationship(
        "Ingredient",
        secondary=recipes_ingredients_table,
        back_populates="recipes",
        cascade="all, delete",
    )
    categories = relationship(
        "Category",
        secondary=recipes_categories_table,
        back_populates="recipes",
        cascade="all, delete",
    )

    history = relationship("History", backref="recipe", passive_deletes=True)

    def __repr__(self):
        return self.name


class Ingredient(Base):
    __tablename__ = 'ingredient'

    id = Column(Integer, primary_key=True)
    name = Column('name', String(256))
    description = Column('description', String(256))
    recipes = relationship(
        "Recipe",
        secondary=recipes_ingredients_table,
        back_populates="ingredients",
        passive_deletes=True
    )

    def __repr__(self):
        return self.name


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    url = Column('url', String(256))
    name = Column('name', String(256))
    recipes = relationship(
        "Recipe",
        secondary=recipes_categories_table,
        back_populates="categories",
        cascade="all, delete",
    )
    
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

    def __repr__(self):
        return self.choise
