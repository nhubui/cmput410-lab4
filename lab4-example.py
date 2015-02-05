from flask import Flask # flask localhost port is default to 5000
app = Flask(__name__) #this name is used when you are using just 1 file, not package?

@app.route('/hello')
def hello():
    return '<h1>Hello Flask!</h1>'

@app.route('/second')
@app.route('/second/<name>')
def second(name = 'FLASK'):
    return '<h1>Hello %s again</h1>' %name


if __name__ == '__main__': #checks if this is run directly and not imported from elsewhere
    app.debug = True #for debugging purposes
    app.run()