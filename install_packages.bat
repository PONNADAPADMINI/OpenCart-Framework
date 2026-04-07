@echo off
call .venv\Scripts\activate
echo Installing project dependencies...
pip install -r requirements.txt
echo Installation completed!
pause