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

@app.route('/teammates/')
def chaptertwo():
    return render_template('two.html',
    	slug="teammates",
    	title="Top college football recruit excels as team-first star",
    	description="The Najee Chronicles: Najee Harris, the nation's No. 1 recruit, remains connected to his teammates even as an injury could derail his senior season at Antioch High.",
    	twitter_text="Najee Harris, nation's No. 1 college football recruit, excels as team-first star.")

@app.route('/the-opponent/')
def opponent():
    return render_template('three.html',
    	slug="the-opponent",
    	title="Big stage, bright spotlight for nation's No. 1 recruit",
    	description="The Najee Chronicles: Antioch High football star Najee Harris faces a stiff test against De La Salle, a program so prominent it has been the subject of a book and film.",
    	twitter_text="Big stage, bright spotlight: Nation's No. 1 football recruit faces stiff competition.")

@app.route('/home-life/')
def home():
    return render_template('four.html',
        slug="home-life",
        title="Nation's No. 1 recruit tackles challenges off the field",
        description="The Najee Chronicles: Even if he's the most coveted prep prospect in the country, Antioch High star Najee Harris deals with pressures that extend to his home life.",
        twitter_text="No place to run: For America's top college football recruit, tackling life off the field isn't easy.")

@app.route('/recruiting/')
def recruit():
    return render_template('five.html',
        slug="recruiting",
        title="Top schools ramp up recruiting of No. 1 football prospect",
        description="The Najee Chronicles: After unofficially committing to play for Alabama, Antioch's Najee Harris is still undecided - and the competition to land him grows more intense every week.",
        twitter_text="Top schools ramp up recruiting of Antioch's Najee Harris, the nation's No. 1 football prospect")
