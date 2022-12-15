import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    bg_color = os.getenv('BG_COLOR','black')
    return render_template('index.html',name='Flask Project example',bg_color=bg_color,color='darkgray')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)
