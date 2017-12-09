from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return render_template('dzialam.html')

@app.route('/api/koty', methods=['GET'])
def json_zahardko():
    return Response(response=render_template('cats.json'), mimetype="application/json")

if __name__ == "__main__":
    app.run()
