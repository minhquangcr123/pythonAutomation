@echo on
@REM Start application - Tran Minh Quang 
ECHO Start application - Tran Minh Quang 
COLOR 

setlocal enabledelayedexpansion

@REM Running application

:enterSource
SET /p source_path="Enter your directory you want to copy list file: "

:enterDest
SET /p dest_path="Enter your destination path: "

IF DEFINED source_path (
    IF NOT EXIST source_path (
        SET source_path=D:\PROJECT\Intergrator\mono_radar_for_int\build
    )
) ELSE (
    SET source_path=D:\PROJECT\Intergrator\mono_radar_learning\build
)

IF DEFINED dest_path (
    IF NOT EXIST dest_path (
        SET dest_path=D:\Tool\PDV\PDV_Gen\Inputs
    )
) ELSE (
    SET dest_path=D:\Tool\PDV\PDV_Gen\Inputs
)

:start
python copyFile.py %source_path% %dest_path%
IF %ERRORLEVEL%==0 start "" "%dest_path%"
pause

goto:enterDest
