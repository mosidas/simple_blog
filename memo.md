# memo

## db.create_all
```
python
>>> from flask_blog import app
>>> from flask_blog import db
>>> with app.app_context():
...     db.create_all()
```