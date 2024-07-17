document.getElementById('fetchButton').addEventListener('click', fetchData);
document.getElementById('playerForm').addEventListener('submit', addPlayer);

function fetchData() {
    // const url = 'https://jsonplaceholder.typicode.com/posts'; // Example API
    const url = 'http://127.0.0.1:8000/'; // Example API

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            displayData(data);
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

function displayData(data) {
    const dataContainer = document.getElementById('dataContainer');
    dataContainer.innerHTML = ''; // Clear previous data

    data.forEach(item => {
        const player = document.createElement('div');
        player.innerHTML = `<h3>${item.username}</h3><p>${item.password}</p>`;
        // post.innerHTML = `<h3>${item.title}</h3><p>${item.body}</p>`;
        dataContainer.appendChild(player);
    });
}



function addPlayer(event) {
    event.preventDefault();

    const url = 'http://127.0.0.1:8000'; // Your Django server URL for POST
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const player = {
        username: username,
        password: password
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': '5',
            // 'X-CSRFToken': getCookie('csrftoken') // Add CSRF token to the headers
        },
        body: JSON.stringify(player)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Player added:', data);
        fetchData(); // Refresh the list of players
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}