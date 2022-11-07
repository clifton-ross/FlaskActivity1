from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
     strHomePageContent = '<h1> Hello World, this is Applied Computing!</h1><h3>This website utilises the Flask web development framework to deliver this functional masterpiece!! </h3>'
     return strHomePageContent
#  return render_template('index.html')
#    return '<h2>Hello!! Wowee a flask web page!!</h2>'

@app.route('/<string:name>')
def hello_there(name):
    return '<h1>Hello there ' + name + '!</h1>'


app.run(host='0.0.0.0', port=81)
