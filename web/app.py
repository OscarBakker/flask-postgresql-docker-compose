# app.py


from flask import Flask
from flask import request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig
import logging

logger=logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

app.debug_log_format = "%(levelname)s in %(module)s [%(pathname)s:%(lineno)d]: %(message)s"

from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info('{} Request Recieved'.format(request.method))

    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run()
