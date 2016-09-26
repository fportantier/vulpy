from flask import Flask, render_template, request, url_for, make_response
import html

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
@app.route('/<path:name>', methods=['GET'])
def hello(name='nobody'):
    #name = html.escape(name)
    response = make_response(render_template('hello.html', name=name))
    return response

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000)

