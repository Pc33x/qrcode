import io
import base64
import qrcode
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        input = request.form.get("user_text")
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(input)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        img = base64.b64encode(buffer.getvalue()).decode('utf-8')
   
        return render_template("qrcode.html", img=img)