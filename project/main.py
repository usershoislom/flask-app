from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from project import db
from project.models import Article

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/posts')
@login_required
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)


@main.route('/posts/<int:id>')
@login_required
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


@main.route('/posts/<int:id>/delete')
@login_required
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for('main.posts'))
    except:
        return "При удалении статьи произошла ошибка!"


@main.route('/create_article', methods=['POST', 'GET'])
@login_required
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        user_id = current_user.id

        article = Article(title=title, intro=intro, text=text, user_id=user_id)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect(url_for('main.posts'))
        except:
            return "При добавлении статьи возникла ошибка!"
    else:
        return render_template("create_article.html")


@main.route('/posts/<int:id>/update', methods=['POST', 'GET'])
@login_required
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return "При редактировании статьи возникла ошибка!"
    else:
        return render_template("post_update.html", article=article)

