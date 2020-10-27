
from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)

@app.route('/temperature', methods = ['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=39383b605fdd2e0ac7cce677d0d7f32a')
    myobj = r.json()
    print(myobj)
    temp_k = float(myobj['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    formatted_string = "{:.2f}".format(temp_f)
    print(formatted_string)

   
    return render_template('home.html', temp = formatted_string)



@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)