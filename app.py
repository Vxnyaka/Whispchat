from flask import Flask, request, render_template, redirect
app = Flask(__name__)

messages_file = "messages.txt"

def load_messages():
    try:
        with open(messages_file, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_message(msg):
    with open(messages_file, "a") as f:
        f.write(msg + "\n")

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["message"]
        save_message(msg)
        return redirect("/")
    messages = load_messages()
    return render_template("chat.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

