@echo on
@REM Start application - Tran Minh Quang 
ECHO Start application - Tran Minh Quang 
COLOR 
echo. & echo %* %0 %1 %~1 %~dp0 

set getOption=yes
If "%getOption%" equ  "yes" (
   set /P option=Enter option: 
   echo Option read: %option%
)

Set "_var=first"
Set "_var=second" & Echo %_var%

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

@REM python copySpecificFile/copyFile.py %source_path% %dest_path%
@REM IF %ERRORLEVEL%==0 start "" "%dest_path%"
