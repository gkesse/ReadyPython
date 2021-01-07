@echo off
::===============================================
set "PATH=C:\MinGW\bin;%PATH%"
set "PATH=C:\Python38;%PATH%"
set "PATH=C:\Python38\Scripts;%PATH%"
::===============================================
set "GPROJECT_ROOT=C:\Users\Admin\Downloads\Programs"
set "GPROJECT_PATH=%GPROJECT_ROOT%\ReadyPython"
set "GPROJECT_SRC=%GPROJECT_PATH%\code\app\src"
::===============================================
set "GSEPARATOR=\"
set "GDATA_PATH=%GPROJECT_PATH%\data"
set "GSQLITE_DB_PATH=%GDATA_PATH%\sqlite\config.dat"
set "GVIDEO_PATH=%GDATA_PATH%\video"
::===============================================
set "GGIT_URL=https://github.com/gkesse/ReadyPython.git"
set "GGIT_NAME=ReadyPython"
::===============================================
set "GPIP_PACKAGE_NAME="
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pip"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pafy"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% youtube-dl"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% db-sqlite3"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% wheel"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pyinstaller"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pyqt5"
::===============================================
