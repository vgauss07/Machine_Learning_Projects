from flask import Flask


app = Flask(__name__)

app.Config.from_object("config.DevelopmentConfig")

from app import views

