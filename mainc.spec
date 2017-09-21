# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainc.py'],
             pathex=['E:\\dev_works\\pyexcel2csv_gui'],
             binaries=[],
             datas=[],
             hiddenimports=['pyexcel_xlsx', 'pyexcel_xlsx.xlsxr'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mainc',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ico.ico')
