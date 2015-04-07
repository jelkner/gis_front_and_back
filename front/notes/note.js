(function() {
    var newNote = document.querySelector('#note-text');
    var saveButton = document.querySelector('#save');
    var notes = document.querySelector('#notes');

    saveButton.addEventListener('click', function() {
        var newItem = document.createElement('li');
        newItem.textContent = newNote.value;
        notes.appendChild(newItem);

        newNote.value = '';
        notes.classList.remove('no-items');
    });
})();
