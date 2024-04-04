from flask import Flask,  render_template, jsonify, request, json
import sys
sys.path.append('/Users/williamboudy/Desktop/programs/Percentle/databases')
from databases import pctle

app = Flask(__name__)

#setting up a route to countries.html
@app.route('/')
def countries():
    return render_template('countries.html')

@app.route('/get_valid', methods=['GET'])
def GET_guesses_list():
    with open('databases/countries.txt', 'r') as f: 
        validGuessesList = f.readlines()
    data = [x.strip() for x in validGuessesList]
    return jsonify(data)

@app.route('/letter_route', methods=['POST'])
def letter_route():
    data = request.json
    f = open("databases/countries.txt","r")
    database_info = f.readlines()
    letter = data['letter'] #next line uses function from pctle module to obtain organized list of countries/percentages
    letter_list = pctle.h_pct_letter(database_info)[(ord(letter) - ord('A'))]
    top5_list = listTrimmer(letter_list, letter)
    json_list = json.dumps(top5_list)
    return json_list

#takes organized list of countries and percentages for a letter and cuts out until its top5
def listTrimmer(data, letter):

    modified_list = []
    if len(data) > 5:
            for i in range(5):
                 modified_list.append(data[i])
            for i in range(5, len(data)):
                if data[i][1] == data[4][1]:
                     modified_list.append(data[i])
    else:
        for i in range(len(data)):
            modified_list.append(data[i])

    return modified_list




if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    