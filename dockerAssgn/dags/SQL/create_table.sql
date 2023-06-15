-- drop table if exists execution_table;
CREATE TABLE IF NOT EXISTS execution_table (
  id SERIAL PRIMARY KEY,
  exectime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);