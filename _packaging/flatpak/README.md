# Flatpak Development

### Local dependencies
- python >= 3.9
- flatpak-builder

### Download the application
```bash
git clone https://github.com/Snuggerdog/pulseSMS.git
cd pulseSMS
```

### Installing dependencies
```bash
# add flathub remote
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# installing required packages
flatpak install --user --assumeyes flathub org.kde.Platform//6.7 org.kde.Sdk//6.7 com.riverbankcomputing.PyQt.BaseApp//6.7 
```

## Building Single-file

Generates a unique file for installation and distribution
```bash
#Setup Virtual Python Environment
    #Note this is the only way I was able to get this working. If you discover another way, please let us know
python -m venv /path/to/pulseSMS/.venv

# Building and Running
/path/to/pulseSMS/.venv/bin/python /path/to/pulseSMS/_packaging/flatpak/build_single_file.py```

At the end, the file for installation will be in the 'export' folder with the name zapzap.flatpak.
For installation:
```bash
flatpak install export/pulsesmsreboot.flatpak
```
