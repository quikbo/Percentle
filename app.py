from flask import Flask,  render_template, jsonify, request, json
import sys
sys.path.append('/Users/williamboudy/Desktop/programs/Percentle/databases')
import pctle

app = Flask(__name__)

#making valid guesses global? 
with open('databases/countries.txt', 'r') as f: 
        validGuessesList = f.readlines()
validGuesses = [x.strip() for x in validGuessesList]

#also need to render home page index.html through here

#render countries.html
#change this so this function creates the randomized letter and it 
#renders the html with the daily letter
@app.route('/countries')
def countries():
    return render_template('countries.html', )


@app.route('/countries_guesses', methods=['POST'])
def guess(): #make this function grab guess from html file and handle it
    return



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    

#HELPER FUNCTIONS

#takes organized list of countries and percentages for a letter and 
#extracts and returns top5 which includes ties
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