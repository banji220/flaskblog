from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "MuhammadHussein Khanjani",
        "title": "Blog Post 1",
        "content": "My first blog post in Flask",
        "date" : "Sep 1, 2020"
    },
    {
        "author": "Amir Mousavi",
        "title": "Blog Post 2",
        "content": "My Second blog post in Flask",
        "date": "Sep 4, 2020"
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")
if __name__ == '__main__':
    app.run(debug=True)
    
