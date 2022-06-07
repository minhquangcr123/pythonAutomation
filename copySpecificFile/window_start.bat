@echo on
@REM Start application - Tran Minh Quang 
ECHO Start application - Tran Minh Quang 
COLOR 

@REM Running application
@REM SET /p source_path="Enter your directory you want to copy list file: "
@REM SET /p dest_path="Enter your destination path: "

@REM IF DEFINED source_path (
@REM     IF NOT EXIST source_path (
@REM         SET source_path=D:\PROJECT\Intergrator\mono_radar_for_int\build
@REM     )
@REM ) ELSE (
@REM     SET source_path=D:\PROJECT\Intergrator\mono_radar_learning\build
@REM )

@REM IF DEFINED source_path (
@REM     IF NOT EXIST dest_path (
@REM         SET dest_path=D:\Tool\PDV\PDV_Gen\Inputs
@REM     )
@REM ) ELSE (
@REM     SET dest_path=D:\PROJECT\Competences\pythonAutomation\copySpecificFile\forCopyTo
@REM )

@REM python copyFile.py %source_path% %dest_path%
@REM IF %ERRORLEVEL%==0 start "" "%dest_path%"
