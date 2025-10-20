from flask import Flask, render_template

app = Flask(__name__)

# Route for the splash screen
@app.route('/')
def home():
    return render_template('index.html')

# NEW: Route for the new home page
@app.route('/home')
def main_page():
    return render_template('home.html')

# Route for the form redirect
@app.route('/join')
def join_page():
    return render_template('join.html')

if __name__ == '__main__':
    app.run()