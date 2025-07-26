from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "At last, after so many buildsss"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
