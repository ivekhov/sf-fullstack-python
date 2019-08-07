// console.log(42);

let button = document.querySelector('.popup-button');

button.addEventListener('click', showPopup);

function showPopup() {
	document.querySelector('.popup').classList.toggle('visible');
	console.log('showPopup works');
}

