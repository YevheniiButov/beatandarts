import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # нужно для сессий и flash-сообщений

# Папка для загруженных файлов
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Конфигурация базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Глобально делаем lang и session доступными в шаблонах
@app.context_processor
def inject_globals():
    lang = request.args.get("lang", "en")
    return dict(lang=lang, session=session)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    lang = request.args.get("lang", "en") if request.method == "GET" else request.form.get("lang", "en")

    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(name=name).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_email'] = user.email
            return redirect(url_for("profile", lang=lang))
        else:
            return render_template("login.html", error="Invalid name or password.", lang=lang)

    return render_template("login.html", error=None, lang=lang)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index", lang=request.args.get("lang", "en")))

@app.route("/big-info")
def big_info():
    return render_template("big-info.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    lang = request.args.get("lang", "en") if request.method == "GET" else request.form.get("lang", "en")

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            flash("Passwords do not match.")
            return render_template("register.html", lang=lang)

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email is already registered.")
            return render_template("register.html", lang=lang)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        session['user_name'] = new_user.name
        session['user_email'] = new_user.email

        return redirect(url_for("profile", lang=lang))

    return render_template("register.html", lang=lang)

@app.route("/profile", methods=["GET"])
def profile():
    if 'user_id' not in session:
        return redirect(url_for("login", lang=request.args.get("lang", "en")))

    name = session.get("user_name", "User")
    email = session.get("user_email", "user@example.com")
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

    return redirect(url_for("profile", lang=request.args.get("lang", "en")))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # создаёт таблицы, если их ещё нет
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
