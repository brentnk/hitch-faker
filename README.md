# hitch-faker
Faking miniquiz sql_hitch data
solutions(probably) ./sql_hitch.sql

```bash
> python sql_hitch_fake.py -u 5000 -t 50000
```
Creates a file ```user_trip.data.sql``` to insert the data into a Postgres database.

Use psql to create a database 
```bash
psql -c 'create database hitchminiquiz;'
```
Setup schema
```bash
psql -d hitchminiquiz -f ./setup_schema.sql
```
Create fake data
```bash
python sql_hitch_fake.py --user-count <int> --trip-count <int>
```
Populate db
```bash
psql -d hitchminiquiz -f ./user_trip.data.sql
```

### TODO
These fields are currently blank:
- client_rating
- driver_rating
- estimated_eta
- actual_eta
- admin emails (...@hitch.com)
