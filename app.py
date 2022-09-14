
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"
@app.route('/next')
def next():
    return "next page"
@app.route('/<username>')
def username(username):
    return( "Welcome to page %s" %username)
@app.route('/logout')
def logout():
    return" NOT FOUND"
if __name__=='__main__':
    app.run()

