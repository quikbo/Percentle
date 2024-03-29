from flask import Flask, request, jsonify
import pctle

app = Flask(__name__)


def process_data():
    data = request.json
    f = open('databases/countries.txt',"r")
    database = f.readlines()
    print(pctle.h_pct_letter(data))

if __name__ == "__main__":
    app.run(debug=True)