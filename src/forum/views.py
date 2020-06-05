from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import current_user
from src import app, db
from src.models import Topic, Category, User, Reply
from src.forum.forms import NewTopicForm, ReplyTopicForm
import datetime

forum_blueprint = Blueprint('forum', __name__,
                            template_folder='templates/forum')


@forum_blueprint.route('/')
def index():
    topics = Topic.query.all()
    categories = Category.query.all()
    return render_template('main.html', topics=topics, categories=categories)


@forum_blueprint.route('/<topic_id>')
def view(topic_id):
    replies = Reply.query.filter_by(reply_topic=topic_id)
    topic = Topic.query.filter_by(id=topic_id).first()
    return render_template('topic_details.html', topic=topic, replies=replies)


@forum_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = NewTopicForm(request.form)

    if request.method == 'POST' and form.validate():
        new_topic = Topic(topic_title=form.topic_title.data,
                          topic_content=form.topic_content.data,
                          topic_category=form.topic_category.data,
                          topic_date=datetime.datetime.now(),
                          topic_author=current_user.id)
        db.session.add(new_topic)
        db.session.commit()

        return redirect(url_for('forum.index'))
    return render_template('new_topic.html', form=form)


@forum_blueprint.route('<int:topic_id>/reply', methods=['GET', 'POST'])
def reply(topic_id):

    form = ReplyTopicForm(request.form)
    topic = Topic.query.filter_by(id=topic_id).first()

    if request.method == 'POST' and form.validate():
        new_reply = Reply(reply_content=form.reply_content.data,
                          reply_date=datetime.datetime.now(),
                          reply_topic=topic_id,
                          reply_author=current_user.id)
        db.session.add(new_reply)
        db.session.commit()

        return redirect(url_for('forum.view', topic_id=topic_id))

    return render_template('topic_reply.html', topic=topic, form=form)
