# -*- coding: utf-8 -*-
"""
"""
import os

from flask import Flask

# TODO: switch to instance path, move config to look in /var/www
#instance_path = "/var/www/pynuget/instance"
instance_path = os.path.abspath(".")
config_file = os.path.join(instance_path, "config.py")

app = Flask(__name__)
app.config.from_pyfile(config_file)

# contrary to Python style, the view imports must be *after* the application
# object is created.
# http://flask.pocoo.org/docs/0.11/patterns/packages/#simple-packages
try:
    import pynuget.routes
except FileNotFoundError:
    raise
    #logger.error("Can't import pynuget.routes.")
