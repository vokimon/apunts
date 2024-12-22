#!/bin/bash
build() {
	pandoc metadata.yaml 0*.md -t revealjs -o index.html --self-contained
}
build
firefox index.html
inotifywait -mr -e close_write  . --exclude html | while read path events file 
do
	(echo $file | grep md$ ) ||
	(echo $file | grep png$ ) ||
	(echo $file | grep yaml$ ) ||
	continue
	build
done

