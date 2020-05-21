from flask import Flask,url_for,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/hp/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

@app.route("/add",methods = ["POST"])
def add():
    title = request.form.get("title")
    NewTodo = Todo(title = title, complete =False)
    db.session.add(NewTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def TodoDelete(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def TodoComplete(id):
    todo = Todo.query.filter_by(id = id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html",todos = todos)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)


