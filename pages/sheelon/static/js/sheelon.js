let form = document.getElementById("sheelon_form")
form.addEventListener('submit', function(event) {
    const formData = new FormData(form)
    let counter = 0
    for (var pair of formData.entries()) {
        counter = counter + 1
    }
    if (counter < 8) {
        event.preventDefault();
        alert('נא למלא את כל השאלות')
    }

})
