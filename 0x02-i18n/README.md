### 0\. Basic Flask app

mandatory

First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `0-app.py, templates/0-index.html`

-----

### 1\. Basic Babel setup

mandatory

Install the Babel Flask extension:

    $ pip3 install flask_babel==2.0.0
    

Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `1-app.py, templates/1-index.html`

-----

### 2\. Get locale from request

mandatory

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `2-app.py, templates/2-index.html`

-----

### 3\. Parametrize templates

mandatory

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_
    

Then initialize your translations with

    $ pybabel extract -F babel.cfg -o messages.pot .
    

and your two dictionaries with

    $ pybabel init -i messages.pot -d translations -l en
    $ pybabel init -i messages.pot -d translations -l fr
    

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

msgid

English

French

`home_title`

`"Welcome to Holberton"`

`"Bienvenue chez Holberton"`

`home_header`

`"Hello world!"`

`"Bonjour monde!"`

Then compile your dictionaries with

    $ pybabel compile -d translations
    

Reload the home page of your app and make sure that the correct messages show up.

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`

-----

### 4\. Force locale with URL parameter

mandatory

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:** ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240409%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240409T143628Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ad47feeccad001b5042bdfc26c634f4aed18143682555a03bb28200f93bd6c2c)

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `4-app.py, templates/4-index.html`

-----

### 5\. Mock logging in

mandatory

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.
```
    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }
```    

This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid

English

French

`logged_in_as`

`"You are logged in as %(username)s."`

`"Vous êtes connecté en tant que %(username)s."`

`not_logged_in`

`"You are not logged in."`

`"Vous n'êtes pas connecté."`

**Visiting `http://127.0.0.1:5000/` in your browser should display this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240409%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240409T143628Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0639431d78fad066a3fd689d267d1f7c3c7b248b9740686a39fbb4f2a66866ab)

**Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:** ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240409%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240409T143628Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=39d33d724570d86e208f87237ff39c178eb1a1c28a98d07a7a682486b7803aec)

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `5-app.py, templates/5-index.html`

-----

### 6\. Use user locale

mandatory

Change your `get_locale` function to use a user’s preferred local if it is supported.

The order of priority should be

1.  Locale from URL parameters
2.  Locale from user settings
3.  Locale from request header
4.  Default locale

Test by logging in as different users

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240409%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240409T143628Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=22ed61992796846a1fdd0c18872d2f9bc94259ae64fe1afad6dc18c9aad0d835)

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `6-app.py, templates/6-index.html`

-----

### 7\. Infer appropriate time zone

mandatory

Define a `get_timezone` function and use the `babel.timezoneselector` decorator.

The logic should be the same as `get_locale`:

1.  Find `timezone` parameter in URL parameters
2.  Find time zone from user settings
3.  Default to UTC

Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use `pytz.timezone` and catch the `pytz.exceptions.UnknownTimeZoneError` exception.

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `7-app.py, templates/7-index.html`

-----

### 8\. Display the current time

#advanced

Based on the inferred time zone, display the current time on the home page in the default format. For example:

`Jan 21, 2020, 5:55:39 AM` or `21 janv. 2020 à 05:56:28`

Use the following translations

msgid

English

French

`current_time_is`

`"The current time is %(current_time)s."`

`"Nous sommes le %(current_time)s."`

**Displaying the time in French looks like this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bba4805d6dca0a46a0f6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240409%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240409T143628Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bef391a5642b4f7b192b9781d27da49de24a9ba7b44890795afa3cca2c5b0751)

**Displaying the time in English looks like this:**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/54f3be802024dbcf06f4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240409%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240409T143628Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=792cbaf4ba9a2ca54cb22d9e7d0619e3b0217011ede39a3b81caa26c0b6c353c)

**Repo:**

*   GitHub repository: `alx-backend`
*   Directory: `0x02-i18n`
*   File: `app.py, templates/index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po`

----------------------------------------------------------------
