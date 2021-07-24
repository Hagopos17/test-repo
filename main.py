from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rootpage():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
    return render_template('index.html', entered_name=name)


app.run()
