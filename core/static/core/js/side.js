function getScrollWidth() {
	let div = document.createElement('div');

	div.style.overflowY = 'scroll';
	div.style.width = '50px';
	div.style.height = '50px';

	document.body.append(div);

	let scrollWidth = div.offsetWidth - div.clientWidth;

	div.remove();

	return scrollWidth
}

function startSide() {
	const side = document.querySelector('.side')

	if (side) {
		const menuBtn = document.querySelector('.menu-btn')
		const layout = document.querySelector('.layout')
		const sideArrow = document.querySelector('.side__arrow')

		function exitHandler() {
			side.classList.remove('active')
			layout.classList.remove('active')
			side.addEventListener('transitionend', () => {
				document.body.classList.remove('lock')
				document.body.style.paddingRight = ''
			})


			this.removeEventListener('click', exitHandler)
		}

		menuBtn.addEventListener('click', event => {
			if (!event.target.closest('.tooltip')) {
				side.classList.add('active')
				layout.classList.add('active')
				let scrollWidth = 0
				if (window.innerHeight < document.documentElement.scrollHeight) {
					scrollWidth = getScrollWidth()
				}


				side.addEventListener('transitionend', () => {
					document.body.classList.add('lock')
					document.body.style.paddingRight = `${scrollWidth}px`
				})

				sideArrow.addEventListener('click', exitHandler)
				layout.addEventListener('click', exitHandler)
			}

		})
	}
}

export default startSide
