from flask import Flask

app = Flask(__name__)
from app import views

if __name__ == '__main__':
    app.run('0.0.0.0')