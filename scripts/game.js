document.getElementById('rollButton').addEventListener('click', function() {
sendJSONData({ action: 'roll' });
});

document.getElementById('purchaseButton').addEventListener('click', function() {
sendJSONData({ action: 'purchase' });
});

document.getElementById('buildButton').addEventListener('click', function() {
sendJSONData({ action: 'build' });
});

document.getElementById('pledgeButton').addEventListener('click', function() {
sendJSONData({ action: 'pledge' });
});

document.getElementById('bankruptcyButton').addEventListener('click', function() {
sendJSONData({ action: 'bankruptcy' });
});

document.getElementById('rentButton').addEventListener('click', function() {
sendJSONData({ action: 'rent' });
});

function sendJSONData(data) {

var url = '';

var options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
};

fetch(url, options)
    .then(response => {
        if (response.ok) {
            console.log('Данные успешно отправлены');
        } else {
            console.error('Ошибка при отправке данных:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Ошибка при отправке данных:', error.message);
    });
}
