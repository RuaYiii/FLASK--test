'''$env:FLASK_APP = "Flask_test.py"'''
# set FLASK_ENV=development
from flask import Flask
from flask import escape
from flask import url_for
from flask import request
from werkzeug.utils import secure_filename
from flask import abort, redirect,render_template,get_flashed_messages
from flask import session
#from werzeug.debug import DebugApplication
#from myapp import app
#app= DebugApplication(app,evalex= True)
app= Flask(__name__)
@app.errorhandler(404)
def page_404(error):
    return render_template('你迷失了/n 不过这是正常的.html'),404
@app.route('/')
def index():
    usernm= request.cookies.get('username')
    if 'username' in session:
        return 'logged in as %s ' % escape(session['username'])
    return 'you re not logged in'
@app.route('/login',methods= ['GET','POST'])
def login():
    pass
    if request.method == 'POST':
        session['username']= request.form('index')
        return redirect(url_for('index'))
    return 'login!!!!!!!'
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

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
        F_.save('/var/www/uploads/'+secure_filename(F_.filename))
@app.route('/me')
def me_api():
    user=' get_current_user()'
    return {
        'username': user.username,
        'theme': user.theme,
        'image': url_for("user_image",filename= user.image),
    }
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next= '/'))
    print(url_for('show_user_profile',username= "Jam"))

''' '''