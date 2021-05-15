from model.models import Recipe, Ingredient, History, Category
from base import Session, engine, Base


# generate database schema
Base.metadata.create_all(engine)

categories = [
    Category(url='zavtrak', name='Завтрак'),
    Category(url='chto-prigotovit-na-obed-i-uzhin', name='Обед'),
    Category(url='chto-prigotovit-na-obed-i-uzhin', name='Ужин'),
    Category(url='chto-prigotovit-na-poldnik', name='Перекус'),
]
session = Session()
session.bulk_save_objects(categories)
session.commit()
