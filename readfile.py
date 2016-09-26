from flask import Flask, render_template, request, url_for
import subprocess
import shlex

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def usage():
    return "Submit a File to Read"


@app.route('/<path:filename>', methods=['GET'])
def readfile(filename):
    try:
        with open('txt/' + filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        content = "File Not Found"

    return render_template('readfile.html', content=content)


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000)

