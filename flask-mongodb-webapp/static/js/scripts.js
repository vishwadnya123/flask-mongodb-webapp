document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addDataForm').addEventListener('submit', addData);
    document.getElementById('getDataBtn').addEventListener('click', getData);
    document.getElementById('analyzeDataBtn').addEventListener('click', analyzeData);
});

function addData(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const value = parseFloat(document.getElementById('value').value);

    fetch('/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: name, value: value })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    });
}

function getData() {
    fetch('/data')
    .then(response => response.json())
    .then(data => {
        let dataList = document.getElementById('dataList');
        dataList.innerHTML = '';
        data.forEach(item => {
            let li = document.createElement('li');
            li.textContent = `Name: ${item.name}, Value: ${item.value}`;
            dataList.appendChild(li);
        });
    });
}

function analyzeData() {
    fetch('/analysis')
    .then(response => response.json())
    .then(data => {
        document.getElementById('mean').textContent = `Mean: ${data.mean}`;
        document.getElementById('median').textContent = `Median: ${data.median}`;
        document.getElementById('summary').textContent = `Summary: ${JSON.stringify(data.summary)}`;
    });
}
