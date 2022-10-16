# memo

## db.create_all
```
python
>>> from flask_blog import app
>>> from flask_blog import db
>>> with app.app_context():
...     db.create_all()
```

## flask command

### run
- linux

```
export FLASK_APP=flask_blog
flask run
```
- windows

```
$env:FLASK_APP="flask_blog"
flask run
```

### debug mode
- linux

```
export FLASK_ENV=development
```
- windows

```
$env:FLASK_ENV="development"
```