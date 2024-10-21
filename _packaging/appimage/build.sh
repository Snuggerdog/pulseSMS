clear 

# Verifica se foi fornecido um argumento
if [ $# -eq 0 ]; then
    echo "Tag da versão não definida"
    exit 1
fi

# Armazena o argumento fornecido em uma variável
tag=$1

# Imprime o conteúdo da variável
echo "Construção para a tag: $tag"


# Download do AppImageTool-x86_64
arquivo="./appimagetool-x86_64.AppImage"

if [ -f "$arquivo" ]; then
    echo "O arquivo $arquivo existe."
else
    echo "O arquivo $arquivo não existe."
    echo "Downloading appimagetool-x86_64..."
    wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
    chmod +x appimagetool-x86_64.AppImage
fi

# Download do código fonte
arquivoZip="./$tag.tar.gz"

if [ -f "$arquivoZip" ]; then
    echo "O arquivo $arquivoZip existe."
else
    wget https://github.com/snuggerdog/pulsesmsreboot/archive/refs/tags/$tag.tar.gz
fi

pasta="./pulsesmsreboot-$tag"
if [ -d "$pasta" ]; then
    echo "A pasta $pasta existe."
else
    tar -xzf $arquivoZip
fi

# Cria arquivo .spec

echo "Criado pulsesmsreboot.spec"

# Conteúdo a ser adicionado ao arquivo
spec_txt="# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['./pulsesmsreboot/__main__.py'],
             pathex=[],
             binaries=[],
             datas=[('pulsesmsreboot', 'pulsesmsreboot')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='pulsesmsreboot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pulsesmsreboot')"


spec_file="$pasta/pulsesmsreboot.spec"

# Adiciona o novo conteúdo ao arquivo
echo "$spec_txt" >> "$spec_file"


# Construção pelo Pyinstaller

pyinstaller $spec_file -y

## AppRun file

appRun="#!/bin/sh\n\ncd \"\$(dirname \"\$0\")\"\nexec ./pulsesmsreboot"

echo -e "$appRun" > "./dist/pulsesmsreboot/AppRun"
chmod +x "./dist/pulsesmsreboot/AppRun"


## build.sh file
build_file="# detect machine's architecture
export ARCH=$(uname -m)

# get the missing tools if necessary
if [ ! -d ../build ]; then mkdir ../build; fi
if [ ! -x ../build/appimagetool-$ARCH.AppImage ]; then
  curl -L -o ../build/appimagetool-$ARCH.AppImage https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-$ARCH.AppImage
  chmod a+x ../build/appimagetool-$ARCH.AppImage 
fi
# the build command itself:
../build/appimagetool-$ARCH.AppImage $PWD

# move result in build folder
mv hello-world-appimage-*-$ARCH.AppImage ../build"

echo -e "$build_file" > "./dist/pulsesmsreboot/build.sh"
chmod +x "./dist/pulsesmsreboot/build.sh"

# Copiar icone

cp "./pulsesmsreboot-$tag/share/icons/com.snuggerdog.pulsesmsreboot.svg" "./dist/pulsesmsreboot/com.snuggerdog.pulsesmsreboot.svg"

# Copiar .desktop
cp "./pulsesmsreboot-$tag/share/applications/com.snuggerdog.pulsesmsreboot.desktop" "./dist/pulsesmsreboot/pulsesmsreboot.desktop"

ARCH=x86_64 ./appimagetool-x86_64.AppImage "./dist/pulsesmsreboot/"


## remove arquivos desnecessários
rm -r $pasta
