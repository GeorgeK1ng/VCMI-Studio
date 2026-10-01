# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path


project_dir = Path(SPECPATH)
datas = [
    (str(project_dir / "res"), "res"),
    (str(project_dir / "presets"), "presets"),
    (str(project_dir / "library-bonusSystem.json"), "."),
    (str(project_dir / "library-identifiers.json"), "."),
]

a = Analysis(
    [str(project_dir / "VCMI_Studio.py")],
    pathex=[str(project_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="VCMI-Studio",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="VCMI-Studio",
)

