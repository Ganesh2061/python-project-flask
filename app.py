from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created= db.Column(db.DateTime,default=datetime.utcnow )

    def __repr__(self) -> str:
        return f"{self.sno} . {self.title}"
         


@app.route("/")
def hello_world():
    todo = Todo(title = "first todo", desc = "start investing in stock market")
    ab = Todo(title = "second todo", desc = "start practice on english")
    db.session.add(todo)
    db.session.add(ab)
    db.session.commit()
    return render_template('index.html')

if __name__ == "__main__":
     # Create the database tables if they don't exist
    with app.app_context():
        db.create_all() 
        print("Database tables created successfully!")

    app.run(debug=True)