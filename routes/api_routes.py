from app import app, Todo, Done, db
import datetime
from flask import request, redirect, url_for

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete

    done = Done(title=todo.title, complete=True)
    done.completeDate = datetime.datetime.now()
    db.session.add(done)

    db.session.delete(todo)

    db.session.commit()
    return redirect(url_for("home"))

@app.route("/undo/<int:todo_id>")
def undo(todo_id):
    done = Done.query.filter_by(id=todo_id).first()
    done.complete = not done.complete

    todo = Todo(title=done.title, complete=False)
    db.session.add(todo)

    db.session.delete(done)

    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/deleteDone/<int:todo_id>")
def deleteDone(todo_id):
    done = Done.query.filter_by(id=todo_id).first()
    db.session.delete(done)
    db.session.commit()
    return redirect(url_for("done"))