import picamera
from flask import Flask, render_template

app = Flask(__name__)
app._static_folder = "home/pi"

@app.route("/pictures")
def hello()
    with picamera.PiCamera() as camera:
    camera.capture('image.jpg')
    return app.send_static_file('image.jpg')

@app.route("/interface")
def interface_display(n):
	return render_template("interface.html")

#app = Flask(__name__)

#@app.route('/photo')
#def hello_world():
    #return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
