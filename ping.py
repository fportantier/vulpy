from flask import Flask, render_template, request, url_for
import subprocess
import shlex

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def ping():
    if 'host' not in request.args:
        return render_template('ping_form.html')
    else:
        host = request.args['host']
        p = subprocess.run("/usr/bin/ping -c 1 " + request.args['host'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return render_template('ping.html', output=p.stdout.decode())

'''
host = shlex.quote(request.args['host'])
'''

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000)

