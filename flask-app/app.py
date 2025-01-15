import qrcode
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        input = request.form.get("user_text")
        img = qrcode.make(input)

        img.save("static/qr.png")

        return render_template("qrcode.html")