from flask import Flask, render_template, request, make_response
import datetime
app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year

    cities = ["Winnipeg", "Brandon", "Steinbach", "Westhawk"]
    return render_template("index.html" , some_text=some_text, current_year=current_year, cities=cities)

@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", user_name=user_name)

    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookies("user_name", contact_name )

        return response


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template ("success.html")


if __name__ == '__main__':
    app.run()