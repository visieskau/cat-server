from flask import Flask, render_template
app = Flask(__name__)

@app.route('/status')
def zahardko_status():
    return render_template('dzialam.html')

if __name__ == "__main__":
    app.run()
