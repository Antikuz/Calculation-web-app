from flask import Flask, request
from socket import gethostname

app = Flask("Addition app")

@app.route("/", methods = ['GET'])
def multiplication():
    try:
        number_one, number_two = map(int, request.args.values())
        response = {'hostname': gethostname(), 'result': number_one + number_two}
    except Exception as err:
        response = {'hostname': gethostname(), 'result': str(err)}

    return response

if __name__ == '__main__':
   app.run()