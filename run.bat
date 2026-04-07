@echo off
call .venv\Scripts\activate
pytest .\testCases\test_001_AccountRegistration.py --browser edge
pause