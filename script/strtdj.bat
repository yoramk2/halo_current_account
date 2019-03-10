echo off
echo START DJANGO WITH HALO : halo_current_account
set arg1=8000
IF %1.==. GOTO No1
set arg1=%1
rem echo DJANGO2
:No1
shift
shift
rem echo DJANGO3
set HALO_STAGE=loc
set HALO_TYPE=loc
set HALO_FUNC_NAME=halo_current_account
set HALO_APP_NAME=bian_service_domains
python manage.py runserver --noreload %arg1%
:End