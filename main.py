from flask import Flask, render_template
app = Flask(__name__)


@app.route('/conservation')
def conservation():
    return render_template('conservation.html')


@app.route('/birds')
def birds():
    return render_template('birds.html')


@app.route('/sanctuaries')
def sanctuaries():
    return render_template('sanctuaries.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

