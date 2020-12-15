@echo off
::===============================================
set "PATH=C:\MinGW\bin;%PATH%"
set "PATH=C:\Python27;%PATH%"
set "PATH=C:\Users\Admin\Downloads\Programs\ReadyPython\win\dist\main;%PATH%"
::===============================================
set "GPROJECT_ROOT=C:\Users\Admin\Downloads\Programs"
set "GPROJECT_PATH=%GPROJECT_ROOT%\ReadyPython"
::===============================================
set "GBIN_PATH=%GPROJECT_PATH%\win\bin\gp_python.exe"
set "GDATA_PATH=%GPROJECT_PATH%\data"
set "GSQLITE_DB_PATH=%GDATA_PATH%\sqlite\config.dat"
set "GAUDIO_PATH=%GDATA_PATH%\audio"
set "GVIDEO_PATH=%GDATA_PATH%\video"
set "GSEPARATOR=\"
set "GSTYLE_PATH=%GDATA_PATH%\css\style.css"
set "GFONT_PATH=%GDATA_PATH%\font"
set "GIMG_PATH=%GDATA_PATH%\img"
set "GPDF_PATH=%GDATA_PATH%\pdf\config.pdf"
set "GCMD_PATH=%GDATA_PATH%\cmd\script.bat"
::===============================================
set "GGIT_URL=https://github.com/gkesse/ReadyPython.git"
set "GGIT_NAME=ReadyPython"
::===============================================
set "GPIP_PACKAGE_NAME=pafy"
set "GPIP_PACKAGE_NAME=youtube-dl"
set "GPIP_PACKAGE_NAME=db-sqlite3"
::===============================================
set "GYOUTUBE_VIDEO_NAME=Jungle Jail - ESMA 2007"
set "GYOUTUBE_VIDEO_PATH=%GVIDEO_PATH%\%GYOUTUBE_VIDEO_NAME%"
::===============================================
