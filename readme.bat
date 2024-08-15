move .\README.rst .\scripts\index.rst
move .\documentation\conf.py .\scripts\conf.py
move .\documentation\favicon.ico .\scripts\favicon.ico
move .\documentation\logo.png .\scripts\logo.png
python -m sphinx scripts doc
move .\scripts\logo.png .\documentation\logo.png
move .\scripts\favicon.ico .\documentation\favicon.ico
move .\scripts\conf.py .\documentation\conf.py
move .\scripts\index.rst .\README.rst
start .\doc\index.html
