rmdir /s /q dist

python -m pip install --upgrade pip
python -m pip install --upgrade build
python -m pip install --upgrade twine

python -m build
python -m twine check --strict dist/*
python -m twine upload --repository testpypi dist/*

python -m pip uninstall celestine --yes
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps celestine
python -m celestine
