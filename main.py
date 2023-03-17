
import qrcode
import base64
from flask import Flask
from flask import request
from io import BytesIO

app = Flask(__name__)

@app.route("/qr")
def qr():
   msg = request.args.get('msg')
   img = qrcode.make(msg)

   buffer = BytesIO()
   img.save(buffer, format="png")

   img64 = base64.b64encode(buffer.getvalue())
   return f'<img src="data:image/png;base64, {img64.decode()}" alt="qrcode" />'

