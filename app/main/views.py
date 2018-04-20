from . import main
from flask import render_template



@main.route('/')
def index():

  title ="Garvin's Manenos"
  return render_template('index.html', title = title)
