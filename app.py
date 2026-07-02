from flask import Flask, render_template, request, send_file
import cv2
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encrypt", methods=["POST"])
def encrypt():

    if "image" not in request.files:
        return "No image uploaded"

    image = request.files["image"]
    message = request.form["message"]
    password = request.form["password"]

    if image.filename == "":
        return "Please choose an image"

    filename = str(uuid.uuid4()) + ".png"

    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    img = cv2.imread(image_path)

    if img is None:
        return "Invalid image."

    # Store password in first pixel
    img[0, 0, 0] = len(password)

    for i, ch in enumerate(password):
        img[0, i + 1, 0] = ord(ch)

    # Store message length
    img[1, 0, 0] = len(message)

    row = 2

    for i, ch in enumerate(message):
        img[row + i, 0, 0] = ord(ch)

    encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename)

    cv2.imwrite(encrypted_path, img)

    return send_file(
        encrypted_path,
        as_attachment=True,
        download_name="encrypted_image.png"
    )


@app.route("/decrypt", methods=["POST"])
def decrypt():

    if "image" not in request.files:
        return "No image uploaded"

    image = request.files["image"]
    entered_password = request.form["password"]

    filename = str(uuid.uuid4()) + ".png"

    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    img = cv2.imread(image_path)

    if img is None:
        return "Invalid image."

    password_length = img[0, 0, 0]

    original_password = ""

    for i in range(password_length):
        original_password += chr(img[0, i + 1, 0])

    if entered_password != original_password:
        return "<h2>❌ Wrong Password!</h2>"

    message_length = img[1, 0, 0]

    secret_message = ""

    row = 2

    for i in range(message_length):
        secret_message += chr(img[row + i, 0, 0])

    return f"""
    <html>
    <body style='font-family:Arial;text-align:center;margin-top:100px;'>
        <h2>✅ Secret Message</h2>
        <h1>{secret_message}</h1>
        <br>
        <a href="/">Go Back</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
