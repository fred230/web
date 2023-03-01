
#!bin/bash

# build_files.sh
echo" building the project"
pip install -r requirements.txt

python3 manage.py collectstatic --noinput

