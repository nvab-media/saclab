from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def serve_pdf():
    return send_from_directory(directory='sql', path='pdf1.pdf')

@app.route("/1")
def se_pdf():
    return send_from_directory(directory='sql', path='pdf1.pdf')


@app.route("/alive")
def alive():
    return "Keep alive"

@app.route("/2")
def second_pdf():
    return send_from_directory(directory='sql', path='pdf2.pdf')

@app.route("/3")
def third_pdf():
    return send_from_directory(directory='sql', path='pdf3.pdf')

@app.route("/4")
def ddl():
    return send_from_directory(directory='sql', path='dbms.pdf')

@app.route("/5")
def ghjk():
    return send_from_directory(directory='sql', path='pdf4.pdf')

@app.route("/5")
def ghjk():
    return send_from_directory(directory='sql', path='pdf4.pdf')

@app.route("/5")
def img():
    return send_from_directory(directory='sql', path='pattern.jpg')


if __name__ == "__main__":
    app.run()
