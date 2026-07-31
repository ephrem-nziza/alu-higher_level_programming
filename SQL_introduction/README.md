# SQL - Introduction

Scripts covering the basics of MySQL: creating and deleting databases,
creating tables, and performing DDL/DML operations such as INSERT,
UPDATE, DELETE, SELECT, subqueries, and aggregate functions.

## Tasks

| File | Description |
| --- | --- |
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if missing |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database |
| `4-first_table.sql` | Creates `first_table` (id INT, name VARCHAR(256)) |
| `5-full_table.sql` | Prints the full description of `first_table` |
| `6-list_values.sql` | Lists all rows of `first_table` |
| `7-insert_value.sql` | Inserts a row (id=89, name="Best School") into `first_table` |
| `8-count_89.sql` | Counts records with id = 89 in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and inserts initial records |
| `10-top_score.sql` | Lists score and name from `second_table`, ordered by score |
| `11-best_score.sql` | Lists score and name where score >= 10, ordered by score |
| `12-no_cheating.sql` | Updates Bob's score to 10, using only the name field |
| `13-change_class.sql` | Removes records with score <= 5 |
| `14-average.sql` | Computes the average score |
| `15-groups.sql` | Counts records per score, sorted by count descending |
| `16-no_link.sql` | Lists score and name where name is not null, ordered by score |

## Requirements

- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
- All files start with a comment describing the task
- Every query is preceded by a comment
- All SQL keywords are uppercase
- All files end with a new line
