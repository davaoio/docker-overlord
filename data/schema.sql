DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    oauth TEXT,
    profile TEXT,
    admin BOOLEAN,
    name TEXT,
    last_login TEXT,
    repos TEXT,
    UNIQUE(oauth)
);

DROP TABLE IF EXISTS deployed_repository;
CREATE TABLE deployed_repository (
    repository TEXT,
    image_tag TEXT,
    released TEXT,
    locked TEXT,
    config TEXT,
    UNIQUE(repository)
);

DROP TABLE IF EXISTS configs;
CREATE TABLE configs (
    id INTEGER PRIMARY KEY,
    repository TEXT,
    version TEXT,
    config TEXT,
    created_on TEXT,
    UNIQUE(repository, version)
);
