from flask import Flask
from flask import render_template
import requests
from flask import request
from flask import *
import requests
import json
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route("/ObjectD.html")
def giris():
    return render_template('ObjectD.html')

@app.route("/Predictive.html")
def predictive():
    return render_template('Predictive.html')

@app.route("/Video.html")
def video():
    return render_template('Video.html')
@app.route("/Demo.html")
def demo():
        return render_template('Demo.html')

@app.route('/Demo.html', methods=['POST'])
def upload_file():
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
                if " " in uploaded_file.filename:
                    uploaded_file.filename = "x"
                uploaded_file.save("./static/uploads/"+uploaded_file.filename)
                filepath="./static/uploads/"+uploaded_file.filename
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
                'images' : open(file_path, 'rb')
                }
                response = requests.post(Service_API_Address, headers = Headers, files = Files)
                x = response.text
                print(x)
                print(x[23])
                {"detection_classes": [], "detection_boxes": [], "detection_scores": []}
                if x[22]=="[" and x[23]=="]":
                    x="Bu resimde kedi ya da köpek bulunamadı.."

                return render_template('Demo.html', variable=file_path, variable2=x)
        else:
            return render_template('Demo.html', variable2="Lütfen resim seçtiğinizden emin olun")



