# Loop through lines in LINGUAS file and generate .po files for each language
while read -r line
do
  # será criado apenas para colocar os .mo
  mkdir -p ./pulsesmsreboot/po/${line}/LC_MESSAGES/
  # create template POT
  xgettext --from-code=UTF-8 --keyword=_ --output=./po/pulsesmsreboot.pot --files-from=./po/POTFILES
  # por motivo desconhecido o arquivo criado não está em UTF-8
  sed -i 's/charset=CHARSET/charset=UTF-8/g' ./po/pulsesmsreboot.pot
  # See if file already exists
  if [ -f ./po/${line}.po ] 
  then
    echo "Skipping ${line}"
    # update PO file
    msgmerge -o ./po/${line}.po ./po/${line}.po ./po/pulsesmsreboot.pot
  else
    echo "Generating ${line}"
    # create PO file
    xgettext --from-code=UTF-8 --keyword=_ --output=./po/${line}.po --files-from=./po/POTFILES
    sed -i 's/charset=CHARSET/charset=UTF-8/g' ./po/${line}.po
    sed -i 's/Language:/Language:'${line}'/g' ./po/${line}.po
  fi
  # create MO
  msgfmt ./po/${line}.po -o ./pulsesmsreboot/po/${line}/LC_MESSAGES/pulsesmsreboot.mo

done < ./po/LINGUAS