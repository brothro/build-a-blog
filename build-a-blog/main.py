from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body




@app.route('/blog', methods=['POST', 'GET'])
def index():

    posts = Post.query.all()
    
    return render_template('blog.html',title="Blog Homepage", posts=posts)

@app.route('/entry', methods=['GET'])
def index2():
    form_value = request.args.get('id')
    entry = Post.query.get(form_value)

    return render_template('entry.html',title="Blog Entry", entry=entry)



@app.route('/newpost', methods=['POST', 'GET'])
def add_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
       
        
        if title == "":
            error = "The title cannot be left blank."
            return render_template('newpost.html', error=error, title=title, body=body)

        elif body == "":
            error = "The title cannot be left blank."
            return render_template('newpost.html', error=error, title=title, body=body)
        
        
        else:
            new_post = Post(title, body)
            db.session.add(new_post)
            db.session.commit()
        return redirect('/blog')
    


    return render_template('newpost.html',title="New Post")


if __name__ == '__main__':
    app.run()