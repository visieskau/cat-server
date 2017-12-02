from flask import Flask
app = Flask(__name__)

@app.route('/status')
def zahardko_status():
    return 'Działam'

if __name__ == "__main__":
    app.run()
