from flask import Flask, jsonify, render_template

app = Flask(__name__)

#setting up a route to countries.html
@app.route('/countries')
def countries():
    return render_template('countries.html')

app.run(host="0.0.0.0", port=80)

"""
#sending list of valid guesses to JS file
@app.route('/get_data')
def compile_list_and_send_to_script():
    with open('databases/countries.txt', 'r') as f: 
        validGuessesList = f.readlines()
    data = [x.strip() for x in validGuessesList]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
    """