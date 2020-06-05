from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_user, login_required, logout_user, current_user
from src import app, db
from src.models import User
from src.forum.forms import NewTopicForm
import datetime

forum_blueprint = Blueprint('forum',  __name__,
                            template_folder='templates/forum')


@forum_blueprint.route('/')
def index():
    return render_template('main.html')


@forum_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = NewTopicForm()
    return render_template('new_topic.html', form=form)
