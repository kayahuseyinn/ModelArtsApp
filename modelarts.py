from flask import Flask
from flask import render_template
import requests
from flask import request
from flask import *
import requests
import json
app = Flask(__name__)
y="..."
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/Giriş.html")
def giris():
    return render_template('Giriş.html')


@app.route("/Demo.html")
def demo():
        return render_template('Demo.html')

@app.route('/Demo.html', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save("./static/uploads/"+"1.png")
        filepath="./static/uploads/"+"1.png"
    Auth_Token_URL = "https://iam.ap-southeast-3.myhuaweicloud.com/v3/auth/tokens"
    Body = {
          "auth" : { 
            "identity": { 
               "methods": ["password"], 
                "password": { 
                    "user": { 
                        "name": "h00822512", 
                        "password": "Liveexplorer.2", 
                        "domain": { 
                            "name": "hwc05519202"
                        } } } }, 
                    "scope": { 
                        "project": { 
                            "name": "ap-southeast-3" 
                        } } }
        }
    response = requests.request( "POST", Auth_Token_URL, json=Body)
    X_Auth_Token = response.headers["X-Subject-Token"]
    Service_API_Address = "https://2fec676ce4e447d0980abfbeb404b0a3.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/3c1e57b1-99e1-4f0a-aaee-11ce28434db4"
    file_path = filepath
    Headers= {
    'X-Auth-Token' : X_Auth_Token
    }
    Files = {
    'images' : open( file_path, 'rb' )
    }
    response = requests.post(Service_API_Address, headers = Headers, files = Files)
    print (response.status_code)
    print (type(response.text))
    return render_template('Demo.html', variable=filepath, variable2=response.text)

