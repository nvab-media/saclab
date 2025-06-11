from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def serve_pdf():
    return send_from_directory(directory='sql', path='pdf1.pdf')

@app.route("/1")
def se_pdf():
    return send_from_directory(directory='sql', path='pdf1.pdf')

@app.route("/2")
def second_pdf():
    return send_from_directory(directory='sql', path='pdf2.pdf')

@app.route("/3")
def third_pdf():
    return send_from_directory(directory='sql', path='pdf3.pdf')

if __name__ == "__main__":
    app.run()
