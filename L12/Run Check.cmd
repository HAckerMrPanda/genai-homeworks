@echo off
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0Run-Check.ps1" %*
set "check_exit=%ERRORLEVEL%"
pause
exit /b %check_exit%
