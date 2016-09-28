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
        #host = shlex.quote(request.args['host'])
        p = subprocess.run(["/usr/bin/ping", "-c", "1", host], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return render_template('ping.html', output=p.stdout.decode())

'''

'''

if __name__ == '__main__':
    app.run(port=8000)

