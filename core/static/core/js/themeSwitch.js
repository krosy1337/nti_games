function startThemeSwitch() {
	const switchButton = document.querySelector('.theme-switch')

	function initialState(themeName) {
		if (switchButton) {
			if (themeName === 'light-theme') {
				switchButton.textContent = 'Тёмная тема'
			} else {
				switchButton.textContent = 'Светлая тема'
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
		switchButton.addEventListener('click', event => {
			event.preventDefault()
			if (localStorage.getItem('theme') === 'light-theme') {
				initialState('dark-theme')
				return
			}
			initialState('light-theme')
		})
	}
}

export default startThemeSwitch