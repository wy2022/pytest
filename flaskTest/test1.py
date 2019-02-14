from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
#访问 127.0.0.1:5000/hello可以访问到
@app.route('/hello')
def helloo():
    return 'hello 123'
#访问 127.0.0.1:5000/about可以访问到
@app.route('/about')
def about():
    return 'about'

#变量规则,url添加变量
#http://127.0.0.1:5000/user/xiaoming
#浏览器返回 User xiaoming
@app.route('/user/<username>')

def show_user_profile(username):
    return 'User %s' %username
#http://127.0.0.1:5000/post/1
#
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post_id : %d' %post_id



if __name__ =='__main__':
    app.debug=True
    app.run(host='0.0.0.0')