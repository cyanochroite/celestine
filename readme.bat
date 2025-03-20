move .\README.rst .\scripts\index.rst
move .\documentation\conf.py .\scripts\conf.py
move .\documentation\favicon.ico .\scripts\favicon.ico
move .\documentation\celestine.svg .\scripts\celestine.svg
python -m sphinx scripts doc
move .\scripts\celestine.svg .\documentation\celestine.svg
move .\scripts\favicon.ico .\documentation\favicon.ico
move .\scripts\conf.py .\documentation\conf.py
move .\scripts\index.rst .\README.rst
start .\doc\index.html
