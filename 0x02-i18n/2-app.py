#!/usr/bin/env python3
"""Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locales():
    """Get the locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """Index the application"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
