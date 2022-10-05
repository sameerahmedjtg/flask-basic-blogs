from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "42a6708574dba971d56e44f5cc18f8a4"

posts = [
    {
        "author": "Sameer Ahmed",
        "title": "Top  5 JS Practices",
        "content": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid magnam quos corrupti, libero rem sit porro velit!",
        "date_posted": "Oct 3, 2022",
    },
    {
        "author": "Rajat Maurya",
        "title": "Best ways to remain silent",
        "content": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid magnam quos corrupti, libero rem sit porro velit!",
        "date_posted": "Oct 4, 2022",
    },
    {
        "author": "Nishant Jawla",
        "title": "How not to act in an office",
        "content": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Aliquid magnam quos corrupti, libero rem sit porro velit!",
        "date_posted": "Oct 5, 2022",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login ", form=form)


if __name__ == "__main__":
    app.run(debug=True)
