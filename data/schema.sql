DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    oauth TEXT,
    profile TEXT,
    admin BOOLEAN,
    name TEXT,
    last_login TEXT,
    UNIQUE(oauth)
);

DROP TABLE IF EXISTS users_repositories;
CREATE TABLE users_repositories (
    users_id INTEGER,
    repository TEXT,
    UNIQUE(users_id, repository)
);
