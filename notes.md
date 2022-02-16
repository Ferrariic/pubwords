## Dependencies
```
py -m pip install --upgrade build
py -m pip install --upgrade twine
```

## Uploading to PyPi Test
```
py -m build
py -m twine upload --repository testpypi dist/*
```

## Uploading to PyPi Main
```
py -m build
twine upload dist/*
```