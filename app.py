from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from menu import *
from pemesanan import *
from antrian import *
from pembayaran import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
