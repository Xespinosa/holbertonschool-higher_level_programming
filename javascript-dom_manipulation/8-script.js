document.addEventListener("DOMContentLoaded", function () {
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
        .then(function (response) {
            if (!response.ok) {
                throw new Error("Error network response");
            }
            return response.json();
        })
        .then(function (data) {
            document.getElementById("hello").textContent = data.hello
        })
        .catch(function (error) {
            console.error("There was a problem with the fetch operation:", error);
        });
});