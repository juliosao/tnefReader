#!/bin/bash

TARGET=dispconf
VERSION=$(awk '/Version:/ { print $$2 }' $TARGET.spec)
DIRTRANS=src/translations
IDIOMAS="de en es it pt"

if [ ! -d translations ]; then
	echo "Creando directorio translations..."
	mkdir $DIRTRANS
fi

PYS=src/*.py src/ui/*.glade

if [ -f $DIRTRANS/$TARGET.pot ]; then	
	echo "Actualizando $DIRTRANS/$TARGETT"
	xgettext -o $DIRTRANS/$TARGET.pot -j --from-code=UTF-8 $PYS --package-name=$TARGET --package-version=$VERSION
else
	echo "Creando $DIRTRANS/$TARGETT"
	xgettext -o $DIRTRANS/$TARGET.pot --from-code=UTF-8 $PYS --package-name=$TARGET --package-version=$VERSION
fi

for IDIOMA in $IDIOMAS
do	
	if [ ! -d $DIRTRANS/$IDIOMA ]; then
		echo "Creando directorio $DIRTRANS/$IDIOMA..."
		mkdir translations/$IDIOMA
	fi

	if [ ! -f $DIRTRANS/$IDIOMA/$TARGET.po ]; then
		echo "Creando el fichero $DIRTRANS/$IDIOMA/$TARGET.po"
		msginit --locale=$IDIOMA --no-translator --input=$DIRTRANS/$TARGET.pot -o $DIRTRANS/$IDIOMA/$TARGET.po 2> /dev/null
		sed -i "s/PACKAGE VERSION/$TARGET/g" $DIRTRANS/$IDIOMA/$TARGET.po
	else
		echo "Actualizando $DIRTRANS/$IDIOMA/$TARGET.po"
		msgmerge $DIRTRANS/$IDIOMA/$TARGET.po  $DIRTRANS/$TARGET.pot -o $DIRTRANS/$IDIOMA/$TARGET.po
	fi
done

