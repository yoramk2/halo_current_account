echo off
set arg1=dev
IF %1.==. GOTO No1
set arg1=%1
echo ZAPPA DEPLOY to %arg1% (MUST BE IN VENV - venv\scripts\activate)
zappa deploy %arg1%