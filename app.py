from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collecting form data
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]
        city = request.form["city"]
        state = request.form["state"]
        phone_number = request.form["phone_number"]
        email = request.form["email"]

        # Constructing the message
        message = (f"Welcome {first_name} {last_name} to our page, "
                   f"your date of birth is {date_of_birth}, you live in {city}, {state}, "
                   f"your phone number is {phone_number}, and your email is {email}. "
                   f"Thank you for visiting our page!")

        # Rendering the form with the output message
        return render_template("index.html", message=message)

    # Render the form without any message (initial GET request)
    return render_template("index.html", message=None)

if __name__ == "__main__":
    app.run(debug=True)
