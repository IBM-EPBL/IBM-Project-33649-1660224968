from flask import Flask, render_template, request, redirect, url_for
import backend

app = Flask(__name__)
path=''

@app.route('/', methods =["GET","POST"])
def index():
    global path
    if request.method == "POST":
        path = request.form.get("myInput")
        return render_template("translate.html", img_path=str(path), pred=str(backend.predict(path)))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)