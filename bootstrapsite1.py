from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bootstrap")
def bootstrapsite():
    return render_template('bootstrapsite1.html')



if __name__ == "__main__":
    app.run(debug=True)

