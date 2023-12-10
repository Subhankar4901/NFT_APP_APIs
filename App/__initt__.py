from flask import Flask, g 
from .routes import base_bp
from APP.utils import  get_db, SCHEMA
import os
app["secret_key"]="secret_sauce"
app = Flask(__name__)
app.register_blueprint(base_bp, url_prefix="/api")

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource(SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()