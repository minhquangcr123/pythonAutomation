@echo on
@REM Call with argument:  %hardware%
@REM Start application - Tran Minh Quang 
ECHO Start application - Tran Minh Quang 
COLOR 


setlocal enabledelayedexpansion

@REM Running application
@REM

:start
python copyFile.py -h
python copyFile.py --config copyFile.ini

