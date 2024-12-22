from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/membership')
def Membership():
    return render_template('Membership.html')

@app.route('/aboutus')
def aboutus():
    return render_template('AboutUs.html')

@app.route('/justaproject')
def justaproject():
    return render_template('justaproject.html')


if __name__=='__main__':
    app.run(debug=True)