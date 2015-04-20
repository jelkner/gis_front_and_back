(function () {
    var newNote = document.querySelector('#note-text');
    var saveButton = document.querySelector('#save');
    var notes = document.querySelector('#notes');
    var contacts = document.querySelector('#contacts');
    function getContacts() {
        if (!('mozContacts' in navigator)) {
            return;
        }
        var req = window.navigator.mozContacts.getAll();
        req.onsuccess = function () {

            if (this.result) {
                // Display the name of the contact
                var option = document.createElement('option');
                console.log(this.result.givenName + ' ' + this.result.familyName);
                option.textContent = this.result.givenName + ' ' +
                    this.result.familyName;
                contacts.appendChild(option);

                // Move to the next contact which will call the request.onsuccess with a new result
                this.continue();

            } else {
                
            }
        };

        req.onerror = function () {
            console.error('Could not recieve contacts!', req.error);
        };
    }
    getContacts();

    saveButton.addEventListener('click', function () {
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
            }, function (err) {
                console.error('Failed to get user location', err);
                store('Could not get your location');
            });
        } else {
            store('You don\'t have GPS');
        }
    });
})();