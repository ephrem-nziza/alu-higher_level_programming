# SQL - More queries

Scripts covering MySQL user management and privileges, table
constraints (NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY),
and retrieving data from multiple tables using JOIN, LEFT JOIN, and
subqueries.

## Tasks

| File | Description |
| --- | --- |
| `0-privileges.sql` | Lists privileges of user_0d_1 and user_0d_2 |
| `1-create_user.sql` | Creates user_0d_1 with all privileges |
| `2-create_read_user.sql` | Creates hbtn_0d_2 and user_0d_2 with SELECT only |
| `3-force_name.sql` | Creates force_name (name can't be null) |
| `4-never_empty.sql` | Creates id_not_null (id defaults to 1) |
| `5-unique_id.sql` | Creates unique_id (id defaults to 1, unique) |
| `6-states.sql` | Creates hbtn_0d_usa and the states table |
| `7-cities.sql` | Creates the cities table with a foreign key to states |
| `8-cities_of_california_subquery.sql` | Cities of California, via subquery (no JOIN) |
| `9-cities_by_state_join.sql` | Cities with their state name, via JOIN |
| `10-genre_id_by_show.sql` | Shows with at least one genre linked |
| `11-genre_id_all_shows.sql` | All shows and their genre_id (NULL if none) |
| `12-no_genre.sql` | Shows without a genre linked |
| `13-count_shows_by_genre.sql` | Number of shows per genre, sorted descending |
| `14-my_genres.sql` | All genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows and their linked genres (NULL if none) |

## Requirements

- Ubuntu 20.04 LTS, MySQL 8.0 (8.0.25)
- All files start with a comment describing the task
- Every query is preceded by a comment
- All SQL keywords are uppercase
- All files end with a new line
