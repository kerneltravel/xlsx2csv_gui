================================================================================
 - Easy convert xlsx(table) to csv file, Let you focus on data, instead of file formats.
================================================================================

Known constraints
==================

Test under windows system, system's default charset is GBK.

Introduction
================================================================================

Feature Highlights
================================================================================
1. Easy to export excel 2013's xlsx file to csv
   * columns saperated by comma and quotes
   * support utf8 encoded chars in csv, which python's default csv is not support.
   * easy to use



How to Use 
================================================================================
You can just click dist_pyinstaller/mainc.exe to run a gui application.
===============
.. image:: https://github.com/kerneltravel/xlsx2csv_gui/raw/master/GUI_screenshot.jpg

How to build
================================================================================
for developers, this project requires the following modouls:
1. software dependences:
  * the python version >2.7,
  * PyQt4,
  * pyexcel_xlsx
  * unicodecsv
  * pyinstaller

for pyexcel_xlsx and unicodecsv and pyinstaller, You can install it via pip:

.. code-block:: bash

    > pip install unicodecsv pyexcel_xlsx pyinstaller
    > cd xlsx2csv_gui
    > .\build_exe_with_pyinstaller.bat or double click build_exe_with_pyinstaller.bat to build exe

Thanks to
================================================================================
`pyexcel-xlsx project for supporting me on pyinstaller packaging issue <https://github.com/pyexcel/pyexcel-xlsx/issues/19>`_

License
================================================================================

New BSD License
