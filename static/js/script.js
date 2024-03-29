
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
    

    //function for obtaining the data from user guess submissions
    document.getElementById("countries_guess").addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this)
        var formDataString = JSON.stringify(Object.fromEntries(formData));
        if ('databases/countries.txt'.includes(formData)) {
            HandleInput(formDataString);
        }
    });
});


//handling the user's guess: see's if its a valid guess and then evaluates if its correct
async function HandleInput(input) {
    console.log('valid')
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
    fetch('/get-data')
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Process the countries list here
            validGuesses = data;
        })
        .catch(error => console.error('Error fetching data:', error));
    
**/