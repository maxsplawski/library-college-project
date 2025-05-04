# Library College Project

## Running the app
```
python main.py
```

### Populating the database with test data
Set the `INSERT_TESTDATA` variable in `settings.py` to `True`.

### The `admin` user
If the database is populated with test data, an `admin` user with email - `admin@example.com`
and password - `password`, is created.

## Running tests
```
python -m unittest tests/test_cli.py
```