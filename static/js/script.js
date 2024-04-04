
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

  
    //var top5 = sendLetter(daily_letter); //calls method to send daily letter to Flask script to then 
    //also obtains top5 list for that letter
    sendLetter(daily_letter).then(data => {
        var top5 = data;
    }).catch(error => {
        console.error(error);  // Handle any errors
    });


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
            HandleInput(formDataObject.guess);
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
function HandleInput(input) {
    const dataToSend = { guess: input};

    fetch('/post_guess', {
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