'''$env:FLASK_APP = "Flask_test.py"'''
# set FLASK_ENV=development
from flask import Flask
from flask import escape
from flask import url_for
from flask import request
#from werzeug.debug import DebugApplication
#from myapp import app
#app= DebugApplication(app,evalex= True)
app= Flask(__name__)
@app.route('/')
def index():
    return "hello WORLD!!!!"
@app.route('/login')
def login():
    return 'login!!!!!!!'
@app.route('/hello')
def hello():
    return "test holeeeasx;askx;ak;XKA;JXKAJX"
@app.route('/user/<username>')
def show_user_profile(username):
    return '{} \' s prrfile !!  '.format(escape(username)) #escape??'''
@app.route("/post/<int:post_id>")
def show_port(post_id):
    return 'post %d' % post_id
@app.route("/path/<path:subpath>")
def show_subpath(path):
    return 'subpathe %s ' %escape(path)
@app.route("/upload",methods= ['GET','POST'])
def upload_files():
    if request.method == 'POST':
        F_= request.files["the_F"]
        F_.save('/var/www/uploads/'+secure_filename(f.filename))
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next= '/'))
    print(url_for('show_user_profile',username= "Jam"))

''' '''