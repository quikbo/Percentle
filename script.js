

var COUNTRIES_UI = (function() {
    var daily_letter = 'A';
    
    document.getElementById("countries").addEventListener('submit', function(event) {
        event.preventDefault();
        var formdata = new FormData(this)
        var formDataString = JSON.stringify(Object.fromEntries(formData));
        HandleInput(formDataString);
    });

    function HandleInput(input) {

    }
})();