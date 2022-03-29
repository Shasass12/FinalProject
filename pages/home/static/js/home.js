const cb = document.getElementById("checkbox");
const instructionBtn = document.getElementById("submitInstruction");


cb.addEventListener('change', () => {
    if (cb.checked) {
        instructionBtn.disabled = false;
    } else {
        instructionBtn.disabled = true;
    }

});