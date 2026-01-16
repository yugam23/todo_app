from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todoDataBase.db"
db = SQLAlchemy(app)

#ORM type
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, default='active')
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"Task {self.id}"


@app.route('/', methods=['POST', 'GET'])
def index():
    #Create the task
    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            task = ToDo(content=content)
            db.session.add(task)
            db.session.commit()
    tasks = ToDo.query.filter_by(status='active').all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id:int):
    task = ToDo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')
    
@app.route('/complete/<int:id>')
def complete(id:int):
    task = ToDo.query.get_or_404(id)
    task.status = 'completed'
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id:int):
    task = ToDo.query.get_or_404(id)
    if request.method == 'POST':
        content = request.form.get('content')
        task.content = content
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit.html', task=task)

@app.route('/completed')
def completed():
    tasks = ToDo.query.filter_by(status='completed').all()
    return render_template('completed.html', tasks=tasks)

if __name__ in "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)