from flask import render_template, redirect, url_for, request

from app import app, db, freezer
from models import *

# Site Path
app.config['SITE_PATH'] = "2016/najee-harris"

# Project Title
app.config['PROJ_TITLE'] = "The Najee Harris Chronicles"

# Project Hashtag
app.config['HASHTAG'] = ''

"""
slug completes:
- twitter:url
- og:image/Facebook image preview
- Twitter/Facebook share url
- url for email body

title:
- Page title
- og:title/Facebook headline
- email subject
- twitter:title

description:
- meta description
- og:description/Facebook description

twitter_text:
- text that appears on tweet

"""

@app.route('/')
def index():
    return render_template('index.html',
    	title="As city lowers boom, Airbnb and rivals thrive",
    	description="Special report: Data on Airbnb shows that visitors continue to flock to the rentals - often in defiance of city requirements to register these impromptu inns.",
    	twitter_text="Airbnb, rivals flourish in SF amid regulatory crackdown.")
