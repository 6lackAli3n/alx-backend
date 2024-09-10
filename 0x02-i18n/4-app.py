#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""


from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Configuration for supported languages and default settings
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Get locale from request, checking for a 'locale' parameter first
@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page.
    """
    # Check if 'locale' is present in the query parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Define the root route
@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
