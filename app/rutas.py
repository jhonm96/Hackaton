from wtforms import form
from app import app
from flask import render_template, redirect, request
from flask import Flask, render_template, redirect, session, flash, request, send_file
from flask.helpers import make_response, url_for
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

@app.route('/')
def hello():
    return 'Hello World!'