@echo off
::===============================================
set "PATH=C:\MinGW\bin;%PATH%"
set "PATH=C:\Users\Admin\AppData\Local\Programs\Python\Python39;%PATH%"
::===============================================
set "GPROJECT_ROOT=C:\Users\Admin\Downloads\Programs"
set "GPROJECT_PATH=%GPROJECT_ROOT%\ReadyPython"
set "GPROJECT_SRC=%GPROJECT_PATH%\code\app\src"
::===============================================
set "GSEPARATOR=\"
set "GDATA_PATH=%GPROJECT_PATH%\data"
set "GSQLITE_DB_PATH=%GDATA_PATH%\sqlite\config.dat"
set "GVIDEO_PATH=%GDATA_PATH%\video"
set "GSTYLE_PATH=%GDATA_PATH%\css\style.css"
set "GFONT_PATH=%GDATA_PATH%\font"
set "GIMG_PATH=%GDATA_PATH%\img"
::===============================================
set "GGIT_URL=https://github.com/gkesse/ReadyPython.git"
set "GGIT_NAME=ReadyPython"
::===============================================
set "GPIP_PACKAGE_NAME="
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pafy"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% youtube-dl"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pyqt5"
set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% QtAwesome"
::set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% db-sqlite3"
::set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% wheel"
::set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% pyinstaller"
::set "GPIP_PACKAGE_NAME=%GPIP_PACKAGE_NAME% sip"
::===============================================
