from flask import render_template, redirect, url_for, request

from app import app, db, freezer
from models import *

# Site Path
app.config['SITE_PATH'] = "2016/najee-harris"

# Project Title
app.config['PROJ_TITLE'] = "The Najee Chronicles"

# Project Hashtag
app.config['HASHTAG'] = 'najeeharris'

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
    	title="Najee Harris' life as nation's No. 1 recruit",
    	description="The Antioch High running back enters his senior year widely regarded as the nation's top recruit, earning him a slice of celebrity in our football-obsessed culture.",
    	twitter_text="The Najee Chronicles: Life as nation's No. 1 recruit.")

@app.route('/chaptertwo/')
def chaptertwo():
    return render_template('two.html',
    	slug="team-player",
    	title="Najee Harris' life as nation's No. 1 recruit",
    	description="The Antioch High running back enters his senior year widely regarded as the nation's top recruit, earning him a slice of celebrity in our football-obsessed culture.",
    	twitter_text="The Najee Chronicles: Life as nation's No. 1 recruit.")
