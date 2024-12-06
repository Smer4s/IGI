document.addEventListener('DOMContentLoaded', function () {
    const contactsTable = document.getElementById('contactsBody');
    const paginationContainer = document.getElementById('pagination');
    const filterTextInput = document.getElementById('filterText');
    const loader = document.querySelector('.loader');
    document.getElementById('filterButton').addEventListener('click', () => filterContacts());
    document.getElementById('addButton').addEventListener('click', () => showAddForm());
    document.getElementById('premiateButton').addEventListener('click', () => premiate());
    document.getElementById('addContactButton').addEventListener('click', () => addContact());
    const contactsUrl = '/myapp/api/contacts/';  

    let contacts = [];
    let filteredContacts = [];
    let currentPage = 1;
    const itemsPerPage = 3;

    function showLoader() { 
        loader.style.display = 'block'; 
    } 
    function hideLoader() { 
        loader.style.display = 'none';
     }

     
    function loadContacts() {
        fetch(contactsUrl)
            .then(response => response.json())
            .then(data => {
                showLoader();
                contacts = data;
                filteredContacts = contacts;
                displayContacts();
                setupPagination();
                hideLoader();
            })
            .catch(error => console.error('Error fetching contacts:', error));
    }

     
    function displayContacts() {
        showLoader();
        const start = (currentPage - 1) * itemsPerPage;
        const end = start + itemsPerPage;
        const pageContacts = filteredContacts.slice(start, end);

        contactsTable.innerHTML = '';
        pageContacts.forEach(contact => {
            const row = contactsTable.insertRow();
            row.insertCell().innerText = contact.name;
            row.insertCell().innerHTML = `<img src="${contact.photo}" alt="Фото" width="50">`;
            row.insertCell().innerText = contact.phone;
            row.insertCell().innerText = contact.email;
            row.insertCell().innerHTML = '<input type="checkbox">';
            row.addEventListener('click', () => displayContactDetails(contact));
        });
        hideLoader();
    }

     
    function displayContactDetails(contact) {
        showLoader();
        const selectedContactDiv = document.getElementById('selectedContact');
        selectedContactDiv.innerHTML = `
            <h2>Детали контакта</h2>
            <p><strong>ФИО:</strong> ${contact.name}</p>
            <p><strong>Фото:</strong> <img src="${contact.photo}" alt="Фото" width="100"></p>
            <p><strong>Телефон:</strong> ${contact.phone}</p>
            <p><strong>Почта:</strong> ${contact.email}</p>
        `;
        hideLoader();
    }

     
    function sortTable(column) {
        showLoader();
        let order = 'asc';
        const th = document.querySelector(`th[data-column="${column}"]`);
        if (th.classList.contains('sort-asc')) {
            order = 'desc';
            th.classList.remove('sort-asc');
            th.classList.add('sort-desc');
        } else {
            th.classList.remove('sort-desc');
            th.classList.add('sort-asc');
        }

        filteredContacts.sort((a, b) => {
            if (a[column] < b[column]) return order === 'asc' ? -1 : 1;
            if (a[column] > b[column]) return order === 'asc' ? 1 : -1;
            return 0;
        });
        displayContacts();
        hideLoader();
    }

     
    function filterContacts() {
        showLoader();
        const filterText = filterTextInput.value.toLowerCase();
        filteredContacts = contacts.filter(contact => {
            return contact.name.toLowerCase().includes(filterText) ||
                contact.phone.toLowerCase().includes(filterText) ||
                contact.email.toLowerCase().includes(filterText);
        });
        currentPage = 1;  
        displayContacts();
        setupPagination();
        hideLoader();
    }

     
    function setupPagination() {
        const totalPages = Math.ceil(filteredContacts.length / itemsPerPage);
        paginationContainer.innerHTML = '';

        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement('button');
            button.innerText = i;
            button.addEventListener('click', () => {
                currentPage = i;
                displayContacts();
            });
            paginationContainer.appendChild(button);
        }
    }

     
    function showAddForm() {
        const addForm = document.getElementById('addForm');
        addForm.style.display = 'block';
    }

    function isValidUrl(url) {
        const regex = /^(http:\/\/|https:\/\/)(.*)(\.png|\.jpg)$/;
        return regex.test(url);
    }

    function isValidPhone(phone) {
        const regex = /^(8|\+375)\s*(\(|0)?29\)?\s*\-?\d{3}\s*\-?\d{2}\s*\-?\d{2}$/;
        return regex.test(phone);
    }

     
    function addContact() {
        showLoader();
        const fullName = document.getElementById('fullName').value;
        const photo = document.getElementById('photo').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;

        const validationMessage = document.getElementById('validationMessage');
        validationMessage.innerHTML = '';

        let isValid = true;

        if (!isValidUrl(photo)) {
            isValid = false;
            validationMessage.innerHTML += '<p>Невалидный URL для фото.</p>';
            document.getElementById('photo').classList.add('highlight');
        } else {
            document.getElementById('photo').classList.remove('highlight');
        }

        if (!isValidPhone(phone)) {
            isValid = false;
            validationMessage.innerHTML += '<p>Невалидный номер телефона.</p>';
            document.getElementById('phone').classList.add('highlight');
        } else {
            document.getElementById('phone').classList.remove('highlight');
        }

        if (isValid) {
            const newContact = {
                name: fullName,
                photo,
                phone,
                email
            };
            contacts.push(newContact);
            filteredContacts = contacts;
            displayContacts();
            setupPagination();
            document.getElementById('contactForm').reset();
        }
        hideLoader();
    }

     
    function premiate() {
        showLoader();
        const selectedContacts = [];
        const checkboxes = document.querySelectorAll('#contactsTable tbody input[type="checkbox"]:checked');

        checkboxes.forEach(checkbox => {
            const row = checkbox.closest('tr');
            const fullName = row.cells[0].innerText;
            selectedContacts.push(fullName);
        });

        const premiationMessage = document.getElementById('premiationMessage');
        premiationMessage.innerHTML = `Премированы сотрудники: ${selectedContacts.join(', ')}`;
        hideLoader();
    }

     
    document.querySelectorAll('th[data-column]').forEach(th => {
        th.addEventListener('click', function () {
            const column = this.getAttribute('data-column');
            sortTable(column);
        });
    });

     
    loadContacts();
});
