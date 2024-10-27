from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clanky')
def clanky():
    return render_template('clanky.html')

@app.route('/onas')
def onas():
    return render_template('oNas.html')

@app.route('/profil')
def profil():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)