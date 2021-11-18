from flask import Flask,jsonify
from flask import Flask, redirect, url_for, request
from api.routes import api

app = Flask(__name__)

@app.route('/')
def route_default_():
   return "<h1>Welcome to ML APIs</h1>"

app.register_blueprint(api)

if __name__ == '__main__':   
   app.run()