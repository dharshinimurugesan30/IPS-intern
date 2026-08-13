from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    kural = None
    error = None

    if request.method == "POST":

        number = request.form.get("number")

        try:
            number = int(number)

            if number < 1 or number > 1330:
                error = "Please enter a number between 1 and 1330."

            else:
                url = f"https://tamil-kural-api.vercel.app/api/kural/{number}"

                response = requests.get(url, timeout=10)

                if response.status_code == 200:
                    kural = response.json()
                else:
                    error = "Unable to get the Kural from API."

        except ValueError:
            error = "Please enter a valid number."

        except requests.RequestException:
            error = "Unable to connect to Thirukkural API."

    return render_template(
        "index.html",
        kural=kural,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)