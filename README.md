# VIBE Firmware Manager

Firmware download and installation manager for VIBE FM firmware packages.

The application connects to The Firmware Hub, downloads available firmware packages, stores them locally and installs firmware files into the VIBE FM Firmware directory.

---

## Features

✅ Download firmware packages

✅ Cache downloads locally

✅ Install downloaded firmware

✅ Backup existing firmware before updates

✅ Force download all firmware packages

✅ Force reinstall all firmware packages

✅ Offline installation from cached packages

✅ Command line interface

---

## Installation

### From PyPI

```bash
pip install vibe-firmware-manager
```

---

## Usage

Show help:

```bash
vibe-fw --help
```
Download sync firmware packages:

```bash
vibe-fw sync

Download available firmware packages:

```bash
vibe-fw download
```

Install previously downloaded firmware:

```bash
vibe-fw install
```

Download and reinstall everything:

```bash
vibe-fw force
```

---

## Application Folders

The application stores all firmware data under:

```text
%APPDATA%\VIBE FM
```

Directory structure:

```text
VIBE FM
│
├── library.json
│
├── Downloads
│   ├── PackageA-1.0.zip
│   ├── PackageB-1.2.zip
│   └── PackageC-4.0.zip
│
├── Firmware
│   ├── PackageA.json
│   ├── PackageA.wasm
│   └── PackageA.aot
│
└── Backup
    ├── 20261101-120000
    └── 20261101-133000
```

---

## Download Process

Downloaded ZIP files are stored in:

```text
%APPDATA%\VIBE FM\Downloads
```

Downloads are retained so firmware can be installed later without requiring another download.

---

## Supported Firmware Files

Only the following file types will be installed:

```text
.json
.wasm
.aot
```

All other files contained within firmware packages are ignored.

---

## Backup Process

Before replacing firmware files, the current firmware files are backed up.

Example:

```text
Backup
└── 20261101-120000
    ├── SynthOne.json
    ├── SynthOne.wasm
    └── SynthOne.aot
```

This allows firmware rollback if required.

---

## Force Install

Force Install performs the following steps:

```text
1. Download all firmware packages
2. Backup current firmware
3. Remove existing firmware files
4. Reinstall all downloaded firmware
```

Files removed during force install:

```text
*.json
*.wasm
*.aot
```

---

## Development

Clone repository:

```bash
git clone https://github.com/kesi03/vibe-firmware-manager.git
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Install editable package:

```bash
pip install -e .
```

Run directly:

```bash
python -m vibe_firmware download
```

---

## Running Tests

```bash
pytest
```

---

## License

MIT License