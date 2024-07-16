from flask import render_template, redirect, url_for, flash, send_file
import os
from app import app, db, qr_svg
from .forms import CommentForm
from .models import Comments


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', svg_img=qr_svg)


@app.route('/shared_files')
def shared_files():
    sharemeet_path = os.getenv('SHAREMEET_PATH')
    all_files_dir = {'files': os.listdir(sharemeet_path)}
    return render_template('shared_files.html', files=all_files_dir)

@app.route('/shared_files/<filename>')
def download(filename):
    uploads = os.path.join(os.getenv('SHAREMEET_PATH'), filename)
    return send_file(uploads, as_attachment=True)


@app.route('/add_comment', methods=['GET', 'POST'])
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        name = form.name.data
        contact = form.contact.data
        comment = form.comment.data
        comment = Comments(name=name, contact=contact, comment=comment)
        db.session.add(comment)
        db.session.commit()
        flash(f'{name}, Ваш комментарий добавлен! Благодарю за обратную связь &#128166;')
        return redirect(url_for('add_comment'))
    return render_template('add_comment.html', form=form)