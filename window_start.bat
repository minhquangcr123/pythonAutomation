@echo off
@REM Start application - Tran Minh Quang 
ECHO Start application - Tran Minh Quang 
COLOR 
echo. & echo %* %0 %1 %~1 %~dp0 



@REM Running application
SET /p source_path="Enter your directory you want to copy list file: "
SET /p dest_path="Enter your destination path: "

IF DEFINED source_path (
    IF NOT EXIST source_path (
        SET source_path=D:\PROJECT\Intergrator\mono_radar_learning\build
    )
) ELSE (
    SET source_path=D:\PROJECT\Intergrator\mono_radar_learning\build
)

IF DEFINED source_path (
    IF NOT EXIST dest_path (
        SET dest_path=D:\PROJECT\Competences\pythonAutomation\copySpecificFile\forCopyTo
    )
) ELSE (
    SET dest_path=D:\PROJECT\Competences\pythonAutomation\copySpecificFile\forCopyTo
)

python copySpecificFile/main.py %source_path% %dest_path%
IF %ERRORLEVEL%==0 start "" "%dest_path%"
