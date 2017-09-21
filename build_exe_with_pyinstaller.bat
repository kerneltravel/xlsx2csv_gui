Rem @echo off
Rem C:\Python27\Scripts\pyinstaller.exe --distpath dist_pyinstaller -F -w mainc.py
C:\Python27\Scripts\pyinstaller.exe --hidden-import pyexcel_xlsx --hidden-import pyexcel_xlsx.xlsxr --distpath dist_pyinstaller -i ico.ico -F -w mainc.py
