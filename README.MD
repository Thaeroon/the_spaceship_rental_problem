# the_spaceship_rental_problem

## usage

### installation
go to the root of the package (where pyproject.toml is)
```bash
python3 -m pip install .
```

### run
```bash
python3 -m the_spaceship_rental_problem
```

### test

```bash
curl -d '[{"name": "Contract1", "start": 0, "duration": 5, "price": 10},{"name": "Contract2", "start": 3, "duration": 7, "price": 14},{"name": "Contract3", "start": 5, "duration": 9, "price": 8},{"name": "Contract4", "start": 5, "duration": 8, "price": 7}]' -H "Content-Type: application/json" -X POST http://localhost:8080/spaceship/optimize
```

## sharing the package
### packaging
```bash
python3 -m pip install --upgrade build
python3 -m build
```
the packaged files will be in `dist`

### installation
```bash
python3 -m pip install the_spaceship_rental_problem-1.0.0-py3-none-any.whl
```

## tests
just run pytest at package root
```bash
pytest
```