import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Папка для загруженных файлов
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        # Простая проверка — замени на свою логику при необходимости
        if name == "test" and password == "1234":
            return redirect("http://localhost:8501")  # или твой Streamlit-URL
        else:
            return render_template("login.html", error="Invalid name or password.")

    return render_template("login.html", error=None)



@app.route("/big-info")
def big_info():
    return render_template("big-info.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return redirect(url_for("profile", name=name, email=email))
    return render_template("register.html")

@app.route("/profile", methods=["GET"])  # ⬅ только GET!
def profile():
    name = request.args.get("name", "User")
    email = request.args.get("email", "user@example.com")
    return render_template("profile.html", name=name, email=email)

@app.route("/upload", methods=["POST"])
def upload():
    cv = request.files.get("cv")
    doc = request.files.get("doc")

    if cv:
        filename = secure_filename(cv.filename)
        cv.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if doc:
        filename = secure_filename(doc.filename)
        doc.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for("profile", name="User", email="user@example.com"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

