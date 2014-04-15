#!/bin/bash

cp -a jozihub-web/src ./build/jozihub-web

mkdir -p ./build/jozihub-web/project/media/uploads
mkdir -p ./build/jozihub-web/project/whoosh
mkdir -p ./build/jozihub-web/project/static

touch ./build/jozihub-web/project/media/uploads/Keep
touch ./build/jozihub-web/project/whoosh/Keep
touch ./build/jozihub-web/project/static/Keep

${PIP} install -r jozihub-web/requirements.txt

