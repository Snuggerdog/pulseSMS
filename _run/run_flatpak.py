import os

os.system('flatpak-builder build _packaging/flatpak/com.snuggerdog.pulsesmsreboot.yaml --force-clean --ccache --install --user')

os.system('flatpak run com.snuggerdog.pulsesmsreboot')
