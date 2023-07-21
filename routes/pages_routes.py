from flask import Flask, render_template
from app import app, Todo, Done

@app.route("/")
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route("/done")
def done():
    done_list = Done.query.all()
    return render_template("done.html", done_list=done_list)