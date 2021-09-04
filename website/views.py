from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
from flask_login import login_required, current_user
from .models import Note, Shelf
from . import db
import json
import os

views = Blueprint('views', __name__)




@views.route('/static/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(views.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

'''
    Shelf-list
    List of all shelves a User has created

    Shelf {
        name,
        category,
        user_ID
    }
'''
@views.route('/shelf-list', methods=['GET', 'POST'])
@login_required
def shelf_list():
    if request.method == 'POST':
        if 'Test' in request.form:
            shelf_name = request.form.get('Name')
            shelf_cat = request.form.get('Category')
            new_shelf = Shelf(name=shelf_name, category=shelf_cat, user_ID = current_user.id)
            db.session.add(new_shelf)
            db.session.commit()
            flash('Note added!', category='success')
        else:

            shelf_id = request.form.get('shelf')
            s = db.select(shelf, int(shelf_id))
            # s = db.select(shelf).where(shelf.c.id == int(shelf_id))
            # s = Shelf.query.get(shelf_id)
            # sql = 'select * from shelf where id = ?'
            # cur = db.cursor()
            # cur.execute(sql, shelf_id)
            # s = cur.fetchone()
            flash('working!', category='success')
            chosen_shelf = conn.execute(s)
            print(chosen_shelf.name)
            return render_template("shelf.html", user=current_user, shelf=chosen_shelf)

    return render_template("shelf_list.html", user=current_user)

'''
    Shelf page
    Individual shelf, with a list of items.
'''
@views.route('/shelf', methods=['GET','POST'])
@login_required
def shelf():
    if request.method == 'POST':
        shelf_id = request.form.get('add-item')
        # s = db.shelf.select(shelf_id)
        # # s = db.select(shelf).where(shelf.c.id == shelf_id)
        # s = Shelf.query.get(shelf_id)
        # # sql = 'select * from shelf where id = ?'
       
        print("Reading single row \n")
        # chosen_shelf = db.execute(s)
        return render_template("shelf.html", user=current_user, shelf=s)

@views.route('/test', methods=['GET','POST'])
@login_required
def test():
    return render_template("test.html", user=current_user)
  
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # new_note = Note(data=note, item_id=current_user.id)
            new_note = Note(data=note)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)
