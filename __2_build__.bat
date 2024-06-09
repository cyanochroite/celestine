rmdir /s /q dist
mkdir dist
python celestine -a clean
python -m build --outdir dist
python -m twine check --strict dist/*
