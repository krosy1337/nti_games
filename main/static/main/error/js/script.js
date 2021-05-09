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


