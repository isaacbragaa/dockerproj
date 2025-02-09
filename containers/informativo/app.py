from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def informativo():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
