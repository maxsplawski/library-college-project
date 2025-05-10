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

### Exporting books

If the `6` command is chosen, then all books are exported to a `csv` file in a destination declared by
`EXPORT_DESTINATION` variable in `settings.py`.

## Running tests

```
python -m unittest tests/test_cli_view§.py
```