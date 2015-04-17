(function() {
    var newNote = document.querySelector('#note-text');
    var saveButton = document.querySelector('#save');
    var notes = document.querySelector('#notes');

    saveButton.addEventListener('click', function() {
        function store(location) {
            var newItem = document.createElement('li');
            newItem.textContent = newNote.value;
            newItem.textContent += ' - ' + location;
            notes.appendChild(newItem);

            newNote.value = '';
            notes.classList.remove('no-items');
        }

        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition(function (position) {
                store(position.coords.latitude + ', ' +
                    position.coords.longitude);
            }, function(err) {
                console.error('Failed to get user location', err);
                store('Could not get your location');
            });
        }
        else {
            store('You don\'t have GPS');
        }
    });
})();
