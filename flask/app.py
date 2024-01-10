from flask import Flask, render_template,url_for

from form import RegisterForm, LoginForm

app = Flask(__name__)
app.secret_key = '1c3ac12cb7e488485934263199f85c14'

# dummy posts
posts = [
    {
        'title' : 'Blog1',
        'author' : 'CB Vishwakarma',
        'date' : 'Jan 07, 2024',
        'content' : 'This is first blog.'
    },
    {
        'title' : 'Blog2',
        'author' : 'Past Writers',
        'date' : 'Jan 07, 2024',
        'content' : 'This is second blog.'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title="About")

@app.route("/register",methods=['POST','GET'])
def register():
    form = RegisterForm()
    return render_template('register.html',form = form, title = "Register")

@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html',form = form, title = "Login")

if __name__ == "__main__":
    app.run(debug=True)