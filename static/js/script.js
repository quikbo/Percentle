
//CAN CUT MOST OF THIS OUT ONCE APP.PY UPDATED

//function for randomizing the daily letter
document.addEventListener("DOMContentLoaded", function(){
    //this block of code sets a random daily letter on the html headers
    function getRandomChar() {
        var asciiCode = Math.floor(Math.random() * 26) + 65;
        return String.fromCharCode(asciiCode);
    }

    var header = document.getElementById("daily_letter");
    var daily_letter = getRandomChar();
    header.textContent = "Letter: " + daily_letter;
    const top5Promise = sendLetter(daily_letter); //collects the top5 in a promise to be used later

    var validGuesses = [] //obtains what guesses could be valid for handling user guess input
    fetch('/get_valid') //this part works good
        .then(response => response.json())
        .then(data => {
            validGuesses = data;
        })
        .catch(error => console.error('Error fetching data:', error));

    //function for obtaining the data from user guess submissions
    document.getElementById("countries_guess").addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this)
        var formDataObject = Object.fromEntries(formData);
        if (validGuesses.includes(formDataObject.guess)) {
            HandleInput(formDataObject.guess, top5Promise);
        } else {
            console.log('Invalid guess, try again')
        }
    });
});


//sends daily_letter to flask file to set up top 5
async function sendLetter(input) {
    const dataToSend = { letter: input };

    try {
        const response = await fetch('/letter_route', {
            method: 'POST',  // or 'PUT'
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataToSend),  // Convert data to JSON string
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();  // Parse JSON response
        return data;  // Return the data for the caller to use
    } catch (error) {
        console.error('Error:', error);
        throw error;  // Rethrow to let the caller handle the error
    }
}

//sends user's guess and letter to flask file through POST request
function HandleInput(input, top5Promise) {

    top5Promise.then(top5 => {

        for (let i = 0; i < top5.length; i++) {
            if (input == top5[i][0]) {
                console.log('correct! ', (i + 1) , '. ', top5[i][0], ' ', top5[i][1])
                return
            }
        }
        console.log('wrong')
        return
    }).catch(error => {
        console.error(error);  // Handle errors
    });

}