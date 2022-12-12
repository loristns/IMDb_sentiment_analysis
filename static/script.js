const form = document.querySelector('.review');
const send = document.getElementById('send');
const text = document.getElementById('text');
const model = document.getElementById('model');
const result = document.getElementById('result');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const data = {
        text: text.value,
        model: model.value
    };

    fetch(`/predict?text=${data.text}&model=${data.model}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.sentiment === 'positive') {
                result.querySelector('.positive').style.display = 'flex';
                result.querySelector('.negative').style.display = 'none';
            } else {
                result.querySelector('.negative').style.display = 'flex';
                result.querySelector('.positive').style.display = 'none';
            }
        })
        .catch(error => {
            console.error(error);
        });
});
