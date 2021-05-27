const mainGameButtons = document.querySelectorAll('.main__game-button_o')

if (mainGameButtons) {
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
}


const progressBar = document.querySelector('.graph__bar-value')
const progressBarText = document.querySelector('.graph__bar-text')

function changeProgressBar() {
	progressBarText.style.right = `-${progressBarText.clientWidth / 2}px`

	n = +progressBar.dataset.value
	base = 'очк'

	if ((n % 10 === 0) || (n % 10 > 4) & (n % 10 < 10) || (n % 100 > 10) & (n % 100 < 15)) {
		progressBarText.textContent = `${n} ${base + 'ов'}`
	} else if ((n % 10 > 1) & (n % 10 < 5)) {
		progressBarText.textContent = `${n} ${base + 'а'}`
	} else {
		progressBarText.textContent = `${n} ${base + 'о'}`
	}


	progressBar.style.width = `${progressBar.dataset.value}%`
	if (localStorage.getItem('theme') === 'light-theme') {
		progressBar.style.backgroundColor = `hsl(${progressBar.dataset.value * 1.3}, 42%, 54%)`
	} else {
		progressBar.style.backgroundColor = '#188e8e'
	}
}

if (progressBar) {
	changeProgressBar()
}
const switchButton = document.querySelector('.theme-switch')

function initialState(themeName) {
	if (switchButton) {
		if (themeName === 'light-theme') {
			switchButton.checked = false
		} else {
			switchButton.checked = true
		}
	}
	localStorage.setItem('theme', themeName)
	document.documentElement.className = themeName
	if (progressBar) {
		changeProgressBar()
	}
}

function initTheme() {
	if (localStorage.getItem('theme')) {
		initialState(localStorage.getItem('theme'))
		return
	}
	initialState('light-theme')
}

initTheme()

if (switchButton) {
	switchButton.addEventListener('change', () => {
		if (localStorage.getItem('theme') === 'light-theme') {
			initialState('dark-theme')
			return
		}
		initialState('light-theme')
	})
}

const sideBar = document.querySelector('.side')
const burger = document.querySelector('.header__burger')
const overlay = document.querySelector('.overlay')

if (overlay) {
	overlay.addEventListener('click', () => {
		sideBar.classList.remove('active')
		document.body.classList.remove('lock')
		overlay.classList.remove('active')
		burger.classList.remove('active')
	})
}

if (burger) {
	burger.addEventListener('click', () => {
		sideBar.classList.toggle('active')
		document.body.classList.toggle('lock')
		overlay.classList.toggle('active')
		burger.classList.toggle('active')
	})
}

// function analyseHandler(e) {
// 	e.preventDefault()
// 	const buttonsContainer = this.closest('.main__game-buttons')
// 	buttonsContainer.querySelectorAll('.main__game-button').forEach(btn => {
// 		btn.style.display = 'none'
// 	})
// 	buttonsContainer.insertAdjacentHTML('afterbegin', '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>')
// 	this.removeEventListener('click', analyseHandler)
//
// 	setTimeout(() => {
// 		this.click()
// 	}, 3000)
// }
//
// const analyseButtons = document.querySelectorAll('.analyse-btn')
//
// analyseButtons.forEach(btn => {
// 	btn.addEventListener('click', analyseHandler)
// })

