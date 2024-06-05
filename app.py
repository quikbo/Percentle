from flask import Flask, render_template, request, session, flash
from flask_session import Session
import sys
sys.path.append('/Users/williamboudy/Desktop/programs/Percentle/databases')
import pctle # type: ignore
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

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



#making valid guesses and top5 lists global for now: HAVE TO REPLACE WITH A DATABASE LATER
with open('databases/countries.txt', 'r') as f: 
        validGuessesList = f.readlines()
validGuesses = [x.strip() for x in validGuessesList]
randomChar_ascii_index = random.randint(65,90)
randChar = chr(randomChar_ascii_index)
daily_letter_countries = pctle.h_pct_letter(validGuesses)
top5 = listTrimmer(daily_letter_countries[randomChar_ascii_index-65], randChar)
top5CountryPercentageGuessBool = [[x[0],x[1],False] for x in top5]
print(top5CountryPercentageGuessBool)

#FLASK FUNCTIONS


#also need to render home page index.html through here
@app.route('/')
def home_page():
     return render_template('index.html')

#render countries.html
#change this so this function creates the randomized letter and it 
#renders the html with the daily letter
@app.route('/countries')
def countries():
    session['mistakes'] = []
    session['guesses'] = []
    return render_template('countries.html', daily_letter = f"Letter: {randChar}", \
                           top5=top5CountryPercentageGuessBool, mistakes = session['mistakes'])

## i wonder if i need to send all the information every time i run render template, especially parts that aren't dynamic 
## like  top5 and daily letter 
@app.route('/submit', methods=['POST'])
def submit(): #make this function grab guess from html file and handle it
    guess = request.form['guess']
    if guess in session['guesses']:
         flash('Already guessed!')
         return render_template('countries.html', daily_letter = f"Letter: {randChar}", \
                           top5=top5CountryPercentageGuessBool, mistakes = session['mistakes'])
    elif guess not in validGuesses:
         flash('Not a valid guess!')
         return render_template('countries.html', daily_letter = f"Letter: {randChar}", \
                           top5=top5CountryPercentageGuessBool, mistakes = session['mistakes'])
    else:
        session['guesses'].append(guess)
        print(guess)
        for x in range(len(top5CountryPercentageGuessBool)):
            if top5CountryPercentageGuessBool[x][0] == guess: #indexing every country's name in list 
                top5CountryPercentageGuessBool[x][2] = True
                return render_template('countries.html', daily_letter = f"Letter: {randChar}", \
                           top5=top5CountryPercentageGuessBool, mistakes = session['mistakes'])
        session['mistakes'].append('X')
        return render_template('countries.html', daily_letter = f"Letter: {randChar}", \
                           top5=top5CountryPercentageGuessBool, mistakes = session['mistakes'])



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    

