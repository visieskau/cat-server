from flask import Flask, render_template, jsonify


from animals import Cat
app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return render_template('dzialam.html')


@app.route('/api/koty', methods=['GET'])
def cats_to_json():
    tina = Cat(name="Tina", age=5)
    klakier = Cat(name="Klakier", age=2)
    rudy = Cat(name="Rudy", age=1)
    return jsonify(tina.__dict__, klakier.__dict__, rudy.__dict__)


if __name__ == "__main__":
    app.run()
