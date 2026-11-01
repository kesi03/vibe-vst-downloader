vibe-firmware-manager/
│
├── src/
│   └── vibe_firmware/
│       │
│       ├── __init__.py
│       ├── __main__.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   ├── firmware.py
│       │   ├── library.py
│       │   └── download.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   ├── library_service.py
│       │   ├── download_service.py
│       │   ├── install_service.py
│       │   ├── backup_service.py
│       │   └── firmware_service.py
│       │
│       ├── storage/
│       │   ├── __init__.py
│       │   ├── paths.py
│       │   └── file_repository.py
│       │
│       ├── cli/
│       │   ├── __init__.py
│       │   └── commands.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── http.py
│           └── zip_utils.py
│
├── tests/
│   ├── test_downloads.py
│   ├── test_backups.py
│   ├── test_installer.py
│   └── test_library.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore