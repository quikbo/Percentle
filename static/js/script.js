
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

    var validGuesses = []
    fetch('/get_data') //this part works good
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
            HandleInput(formDataObject.guess, daily_letter);
        } else {
            console.log('Invalid guess, try again')
        }
    });
});


//sends user's guess and letter to flask file through POST request
function HandleInput(input, letter) {
    const dataToSend = { guess: input, daily_letter : letter };

    fetch('/post_data', {
        method: 'POST',  // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),  // Convert data to JSON string
    })
        .then(response => response.json())  // Parse JSON response
        .then(data => console.log(data))  // Do something with the response
        .catch(error => console.error('Error:', error));
}

/** 
//isValid grabs list of possible countries from fetchData function and returns true if input is present
async function isValid(input) {
    const data = await fetchData();
    return data.includes(input);
}

async function fetchData() {
    try {
        // Use the Fetch API to send the request
        const response = await fetch('/get_data');

        // Check if the request was successful
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();
        return data; 

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


//*
    //code to obtain array list of valid guesses
    
    
**/