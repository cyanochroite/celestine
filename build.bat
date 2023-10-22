rmdir /s /q
python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m pip install --upgrade twine
python -m build
python -m twine check --strict dist/*
