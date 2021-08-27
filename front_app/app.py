from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(f'index.html')

@app.route("/calculation", methods = ['POST'])
def calculation():
    number_one, number_two = request.form.values()
    return f"{number_one}, {number_two}"


if __name__ == '__main__':
   app.run(port=8080)