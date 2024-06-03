# Percentle

06/03:
    goal - refactor to move functionality and all HTML VERB pathways GET and POST directly to app.py
    remove most of the code from script.js
    make html prettier
    figure out modulenotfounderror for databases


04/04:
    saved top5list in a promise and handled input validation: now need to 
    make result of validation affect html structures on screen 


04/03:
    added route for getting top5 list into script. still need to have JS make error messages for inputs
    and want to make the length of top5 list affect html for answer boxes.


04/02: 
    Implemented two RESTful API routes, GET for validating if guesses are even in the pool of guessable
    words (error message pops up in console but next session will have javascript create an html error
    message), and POST for sending guessed word and the daily letter to python server for handling


goal for 03/29/24: 
    get the game itself working. connect python scripts for top 5 countries of daily letter to 
    the UI. just for countries. 

    refactored directories and folders into proper Flask app format.
    learned how to run Flask server and access webpage through local port.
    still need to figure out how to fetch the array of countries into JS script from Flask app.




