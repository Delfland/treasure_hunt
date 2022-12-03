DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE games(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    user_id INT NOT NULL REFERENCES users(id)
);

CREATE TABLE locations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    clue VARCHAR(255),
    user_id INT NOT NULL REFERENCES users(id),
    game_id INT NOT NULL REFERENCES games(id)
);