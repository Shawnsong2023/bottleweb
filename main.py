from bottle import Bottle, request, run, static_file, response, route
import subprocess
import os

app = Bottle()

@app.route('/')
def home():
    return static_file('index.html', root='./')

@app.route('/api/', method='POST')
def api():
    code = request.forms.get('code')
    output = run_code(code)
    return {'output': output}

def run_code(code):
    try:
        output = subprocess.check_output(['python', '-c', code], universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
