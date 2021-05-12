from model.models import Recipe, Ingredient, History
from base import Session, engine, Base


# generate database schema
Base.metadata.create_all(engine)

# create a new session
# session = Session()

# create recipe
# recipe = Recipe("The Bourne Identity", "sdaghdc", "jhdh", 123)

# persists data
# session.add(recipe)

# commit and close session
# session.commit()
# session.close()