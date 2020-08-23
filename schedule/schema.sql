-- Flask To-Do Database Schema
--
-- This file will drop and recreate all tables necessary for
-- the application and can be run with the `flask init-db`
-- command in your terminal.

-- Drop existing tables
DROP TABLE IF EXISTS schedule;
-- Add query to drop users table here

-- Add query to create users table here

-- To-Do Items
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id bigserial PRIMARY KEY,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE schedule (
    id bigserial PRIMARY KEY,
    author_id INTEGER,
    years bigserial,
    months text,
    days text,
    date bigserial,
    shift  varchar(225),
    description varchar(140) NOT NULL,
    FOREIGN KEY (author_id) REFERENCES users (id)

    -- Add Foreign Key to users table here
);
