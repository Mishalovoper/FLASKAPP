from flask import Flask, render_template, url_for

app = Flask(__name__)

all_posts = [
    {
        'title':'Post1',
        'content': 'This is the content of post 1 GG',
        'author': 'Mishal'
    },
    {
        'title': 'Post2',
        'content': 'This is the content of post 2 Kfoo ya w7sh'
    }

]

@app.route('/')

def index():

    return render_template('index.html')

@app.route('/posts')

def posts():
    return render_template('posts.html', posts = all_posts, title="Bo jally")


@app.route('/home/user/<string:name>/id/<string:id>')

def hello(name,id):

    return "Hi, "+name+". Your Id is "+id

@app.route('/onlyget',methods=['GET'])

def get_req():

    return "This webpage only allows GET request"

@app.route('/bootstrap')
def boots():
    return render_template('bootstrap_test.html')

@app.route('/personal')
def personal():
    return render_template('index.html')
if __name__ == '__main__':

    app.run(debug=True)
