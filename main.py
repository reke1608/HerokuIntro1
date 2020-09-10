from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    return render_template("index.html" , some_text=some_text, current_year=current_year)

@app.route("/about-me")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run()