from flask import Blueprint, Flask, abort, render_template, request, redirect, url_for
import os
from .migration_kaiin_table import *
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/mypage')
@login_required
def mypage():
    return render_template('profile.html')
    
@main.route('/')
@login_required
def index():
    return render_template('profile.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

#if __name__=="__main__":
#    app.debug = True
#    app.run(host='0.0.0.0', port="8888")