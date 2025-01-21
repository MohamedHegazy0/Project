from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/500MbOrange', methods=['POST'])
def run_orange_script():
    os.system("python3 500MbOrange.py")
    return "تم تشغيل سكربت 500 ميجا أورنج بنجاح!"

@app.route('/2hoursEtisalat', methods=['POST'])
def run_etisalat_script():
    os.system("python3 2hoursEtisalat.py")
    return "تم تشغيل سكربت ساعتين نت اتصالات بنجاح!"

if __name__ == "__main__":
    app.run()
