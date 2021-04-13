const mainGameButtons = document.querySelectorAll('.main__game-button')

mainGameButtons.forEach(button => {
	button.addEventListener('click', () => {
		const containerBody = button.closest('.game').querySelector('.game__body')

		if (containerBody.classList.contains('active')) {
			containerBody.style.maxHeight = null
			containerBody.classList.remove('active')
		} else {
			containerBody.style.maxHeight = containerBody.scrollHeight + 'px'
			containerBody.classList.add('active')
		}

		button.classList.toggle('active')


	})
})

const sideBar = document.querySelector('.side')
const burger = document.querySelector('.header__burger')
const overlay = document.querySelector('.overlay')

overlay.addEventListener('click', () => {
	sideBar.classList.remove('active')
	document.body.classList.remove('lock')
	overlay.classList.remove('active')
	burger.classList.remove('active')
})

burger.addEventListener('click', () => {
	sideBar.classList.toggle('active')
	document.body.classList.toggle('lock')
	overlay.classList.toggle('active')
	burger.classList.toggle('active')
})