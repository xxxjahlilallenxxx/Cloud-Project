import pyrebase
from flask import Flask, render_template

firebaseConfig = {
    "apiKey": "AIzaSyBRqKEG14eU2yBO39S633fXJCa7BphB9zo",
    "authDomain": "swamii-20617.firebaseapp.com",
    "databaseURL": "https://swamii-260617.firebaseio.com",
    "projectId": "swamii-260617",
    "storageBucket": "swamii-260617.appspot.com",
    "messagingSenderId": "264652459566",
    "appId": "1:264652459566:web:3176279c6aa01377d8d9bf",
    "measurementId": "G-NQCSM517KM"
  }
firebase = pyrebase.initialize_app(firebaseConfig)
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def signup():
    error = None
    unsuccessful = 'Please check your credentials'

    if request.method == 'POST':
        email = request.form["username"]
        password = request.form["password"]

        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template()
        except:
            return render_template('signup.html', us=unsuccessful)
    return render_template('signup.html', error=error)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
