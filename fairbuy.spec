# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['login_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Abraham Oluwagbenga/Music/fairbobs/admin_ops_gui.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/admin_controller.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/vendor_gui.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/admin_op_guis.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/report_generator.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/login_controller.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/login_db_model.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/logs_model.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/vendor_controller.py', '.'), ('C:/Users/Abraham Oluwagbenga/Music/fairbobs/vendor_db_model.py', '.')],
    hiddenimports=['bcrypt', 'sqlite3', 'reportlab', 'reportlab.lib.units', 'reportlab.lib.pagesizes', 'reportlab.pdfgen.canvas'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='fairbuy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.ico'],
)
