CREATE DATABASE recipes;
USE recipes;

CREATE TABLE IF NOT EXISTS recipes (
    id                  bigserial PRIMARY KEY,
    recipes_name        varchar(256) NOT NULL,
    cooking_time        int NOT NULL,
    description         text,
    portion             varchar(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS ingredients (
    id                  bigserial PRIMARY KEY,
    name                varchar(128) NOT NULL,
    measurements_id     bigint REFERENCES measurements(id) ON DELETE CASCADE,
    PRIMARY KEY (measurements_id)

);

CREATE TABLE IF NOT EXISTS ingredientsrecipes (
    id                  bigserial PRIMARY KEY,
    ingredient_id       bigint REFERENCES ingredients(id) ON DELETE CASCADE,
    recipe_id           bigint REFERENCES recipes(id) ON DELETE CASCADE,
    amount              decimal(10,5) NOT NULL,
    PRIMARY KEY (ingredient_id, recipe_id)
);

CREATE TABLE IF NOT EXISTS measurements (
    id                  bigserial PRIMARY KEY,
    unit                varchar(38),
    amount              int NOT NULL,
    metric_unit         varchar(38)
);

INSERT INTO 
    measurements (id, unit, amount, metric_unit)
VALUES
    (1,'ч.л.', 10, 'г'),
    (2,'ст.л.', 25,'г'),
    (3,'щепотка', 2, 'г'),
    (4,'стакан', 200,'мл'),
    (5,'по вкусу', 2,'г'),
    (6,'на кончике ножа', 1,'г');