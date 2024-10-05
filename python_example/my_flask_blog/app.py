# start app
from flask import Flask, render_template, request,redirect,url_for;
from posts import get_posts, add_post;

app = Flask(__name__)

# Coding here
@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["POST"])
def add():
    #Step 1 MVC -> Request to controller
    title = request.form["title"] #Nhận dữ liệu từ title trong form
    content = request.form["content"] #Nhận dữ liệu từ content trong form
    #Step 2: call model
    add_post(title, content)
    #Step 3: Return to view
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)