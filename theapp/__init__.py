from flask import Flask
from flask_cors import CORS

import os

from .bp.chat.routes import chat_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # uri_db = 'mysql+pymysql://root:@localhost/pendu?charset=utf8mb4'
    # uri_db = 'mysql+pymysql://inonaryc_penduuser:pendupassword666@inonary.com/inonaryc_pendu?charset=utf8mb4'
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_PENDU', uri_db)
    app.secret_key = "secret_key"
    app.config['PERMANENT_SESSION_LIFETIME'] = 360000
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(chat_bp)

    with app.app_context() :
        # from .models import db, convert_table_character
        
        # db.init_app(app)
        # db.create_all()
        # convert_table_character()

        return app