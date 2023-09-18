fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(function(response) {
        if (!response.ok){
            throw new Error("Network response was not ok")
        }
        return response.json();
    })
    .then(
        function(data){
            document.getElementById('character').textContent = "Character: " + data.name;
    })
    .catch(function(error){
        console.error('There was a problem with fetch operation:', error)
    })