from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Heroku!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get PORT from Heroku or default to 5000
    app.run(host="0.0.0.0", port=port)
