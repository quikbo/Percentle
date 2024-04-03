from flask import Flask,  render_template, jsonify, request

app = Flask(__name__)

#setting up a route to countries.html
@app.route('/')
def countries():
    return render_template('countries.html')

@app.route('/get_data', methods=['GET'])
def GET_guesses_list():
    with open('databases/countries.txt', 'r') as f: 
        validGuessesList = f.readlines()
    data = [x.strip() for x in validGuessesList]
    return jsonify(data)

@app.route('/post_data', methods=['POST'])
def POST_guesses():
    data_received = request.json
    guess = data_received['guess']
    letter = data_received['daily_letter']
    print(guess)
    print(letter)
    return jsonify({'status' : 'success'})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    