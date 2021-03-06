#!/bin/bash

if [ ! -d "./p-env/" ]; then
    virtualenv -p python3 doc-env
fi

source ./doc-env/bin/activate

TMP_DEPS=/tmp/temp_deps_${RANDOM}
pip freeze -l > ${TMP_DEPS}
if ! cmp ./requirements.txt ${TMP_DEPS} > /dev/null 2>&1
then
  echo "Installing Python dependencies ..."
  cat ${TMP_DEPS}
  pip install -r ./requirements.txt
fi

export FLASK_APP=api.py
flask run
