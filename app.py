from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    """Homepage for Open Terminal."""
    return render_template('index.html', slogan="Trade Smart, Trade Fast")

@app.route('/about')
def about():
    """About page for Open Terminal."""
    return render_template('about.html', description="Open Terminal is a Trading Terminal for traders built using Python, Flask, and AngelOne Smart API.")



if __name__ == '__main__':
    app.run(debug=True)
