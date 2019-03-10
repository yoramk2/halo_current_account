echo off
set arg1=dev
IF %1.==. GOTO No1
set arg1=%1
set filename=%arg1%_sls_settings.json
set filename=%filename:-=_%
copy %filename% serverless.yml
echo SERVERLESS DEPLOY to %arg1%
serverless deploy