#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Configuration for supported languages and default settings
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

# Initialize Babel
babel = Babel(app)

# Get locale from request
@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page."""
    # 1. Check if the locale is in the URL query parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Check if the user is logged in and has a locale preference
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Use the locale from the request's Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Function to retrieve a user from the 'database'
def get_user():
    """Retrieves a user based on a user id.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

# before_request function to set the user in the global context
@app.before_request
def before_request():
    """Retrieves a user based on a user id.
    """
    g.user = get_user()

# Define the root route
@app.route('/')
def index():
    """The home/index page.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
