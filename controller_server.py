# controller_server.py
# genx control server
# docs: http://flask.pocoo.org/
# quickstart: http://flask.pocoo.org/docs/quickstart/#quickstart

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


# examples:
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()


# url_for('static', filename='style.css')

# from flask import render_template

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)


# Inside templates you also have access to the request, session
# and g [1] objects as well as the get_flashed_messages() function.

# searchword = request.args.get('key', '')


# You can handle uploaded files with Flask easily. Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.

# Uploaded files are stored in memory or at a temporary location on the filesystem. 
# You can access those files by looking at the files attribute on the request object.
# Each uploaded file is stored in that dictionary. It behaves just like a standard
#  Python file object, but it also has a save() method that allows you to store 
#  that file on the filesystem of the server. Here is a simple example showing 
#  how that works:

# from flask import request

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')
#     ...
# If you want to know how the file was named on the client before it was uploaded 
# to your application, you can access the filename attribute.




if __name__ == '__main__':
    app.run(debug=True) # turn off in production lol
