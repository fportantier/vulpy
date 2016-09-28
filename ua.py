from flask import Flask, render_template, request, url_for, make_response
import html
import os

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def save(name='nobody'):

    with open('ua-history.txt', 'a') as f:
        uagent = request.headers['User-Agent']
        #uagent = html.escape(uagent)
        f.write(uagent + "\n")

    return "ok <a href='/report'>Access Report</a>"


@app.route('/report', methods=['GET'])
def report():

    with open('ua-history.txt', 'r') as f:
        history = f.readlines()

    response = make_response(render_template('ua.html', history=history))
    response.headers['X-Frame-Options'] = 'DENY'
    return response


@app.route('/delhistory/', methods=['GET'])
def delhistory():

    if not str(request.referrer).startswith(request.url_root):
        #app.logger.info("referer:", str(request.referrer))
        return "CSRF ATTEMPT!"

    os.unlink('ua-history.txt')
    return "ok"


if __name__ == '__main__':
  app.run(port=8000)

