from flask import Flask,render_template,request,jsonify,make_response,url_for,redirect,Response,flash,send_from_directory
import os
import uuid
import pandas as pd

app = Flask(__name__)
# Required for Sessions
app.secret_key = '1OhMyNiga0'

@app.route('/')
def home():
    routes = ['signin','upload','convert']
    flash("Home Page")
    return render_template('home.html',routes=routes)

@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('Users.txt','a') as f:
            f.write(f"{username,password}\n")
        return redirect(url_for('home'))

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        file = request.files['file']
        df = pd.read_csv(file)
        return df.to_html()
    
@app.route('/convert',methods=['GET','POST'])
def convert():
    if request.method == 'GET':
        return render_template('TxtToCsv.html')
    else:
        file = request.files['file']
        df = pd.read_csv(file)
        first_rows = df.head(10)
        if not os.path.exists('downloads'):
            os.makedirs('downloads')

        filename = f"{uuid.uuid4()}.csv"
        files = os.listdir('downloads')

        df.to_csv(os.path.join('downloads',filename))

        return render_template('download.html',filename=filename,df=first_rows,files=files)
    
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name='out.csv')

@app.route('/show_data/<df>')
def show_data(df):
    return df.to_html()

