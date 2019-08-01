#!/bin/bash

TARGET=dispconf
DIRTRANS=src/translations
IDIOMAS="de en es it pt"


for IDIOMA in $IDIOMAS
do	
	if [ ! -d $DIRTRANS/$IDIOMA/LC_MESSAGES ]; then
		mkdir -p $DIRTRANS/$IDIOMA/LC_MESSAGES
	fi
	
	
	echo "actualizando $DIRTRANS/$IDIOMA/LC_MESSAGES/$TARGET.mo"
	msgfmt $DIRTRANS/$IDIOMA/$TARGET.po -o $DIRTRANS/$IDIOMA/LC_MESSAGES/$TARGET.mo 

done
