from flask import Flask, render_template
app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return render_template('dzialam.html')

@app.route('/api/koty', methods=['GET'])
def json_zahardko():
    return render_template('cats.json')

if __name__ == "__main__":
    app.run()
