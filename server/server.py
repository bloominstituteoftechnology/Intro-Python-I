import flask
import subprocess
import time

app = flask.Flask(__name__)

@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['python ../src/days-2-4-adv/adv.py'],
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )

        for line in iter(proc.stdout.readline, ''):
            time.sleep(1)
            yield line.rstrip() + '<br/>\n'
        
    return flask.Response(inner(), mimetype='text/html')

app.run(debug=True, port=5000)
