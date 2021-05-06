-- This SQL script creates an empty database to store information about recipes, ingredients, measurements.

CREATE TABLE IF NOT EXISTS recipes (
    id                  INTEGER PRIMARY KEY,
    recipes_name        VARCHAR(256) NOT NULL,
    cooking_time        INTEGER NOT NULL,
    url                 VARCHAR(256) NOT NULL,
    img                 VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS ingredients (
    id                  INTEGER PRIMARY KEY,
    name                VARCHAR(128) NOT NULL,
    description         TEXT,
    -- measurements_id     INTEGER REFERENCES measurements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ingredientsrecipes (
    id                  INTEGER PRIMARY KEY,
    ingredient_id       INTEGER REFERENCES ingredients(id) ON DELETE CASCADE,
    recipe_id           INTEGER REFERENCES recipes(id) ON DELETE CASCADE,
    amount              decimal(10,5) NOT NULL,
    UNIQUE (ingredient_id, recipe_id)
);

CREATE TABLE IF NOT EXISTS measurements (
    id                  INTEGER PRIMARY KEY,
    unit                VARCHAR(38),
    amount              INTEGER NOT NULL,
    metric_unit         VARCHAR(38)
);

CREATE TABLE IF NOT EXISTS history (
    id                  INTEGER PRIMARY KEY,
    user_id             INTEGER,
    recipe_id           INTEGER REFERENCES recipes(id) ON DELETE CASCADE,
    date                DATETIME,
    choise              INTEGER
);

INSERT INTO 
    measurements (unit, amount, metric_unit)
VALUES
    ('ч.л.', 10, 'г'),
    ('ст.л.', 25,'г'),
    ('щепотка', 2, 'г'),
    ('стакан', 200,'мл'),
    ('по вкусу', 2,'г'),
    ('на кончике ножа', 1,'г'),
    ('кг', 1000, 'г'),
    ('л', 1000, 'мл');
    