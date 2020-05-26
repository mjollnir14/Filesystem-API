# REST API

## what is this?
simple api using flask to retrieve basic filesystem informations such as the content of a directory


## install

```
# create python virtual env
virtualenv rest-api
source rest-api/bin/activate
mkdir ~/rest-app
cd ~/Filesystem-API

pip install -r requirements.txt


# make fresh db
rm content.db
$ sqlite3 content.db
sqlite> .mode csv content
sqlite> .import content.csv content
```

## run
```
python app.py
```

then go to http://localhost:5000/departments

you could drill down by deparments too!

try http://localhost:5000/dept/police

## inspired by:
https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/
