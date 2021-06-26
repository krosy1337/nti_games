function startModal() {
	const modalBtn = document.querySelector('.side__accounts-arrow')
	const modal = document.querySelector('.modal')

	if (modal) {
		modalBtn.addEventListener('click', () => {
			modal.classList.add('active')

			modal.addEventListener('click', event => {
				const target = event.target

				if (target.closest('.modal__close-btn') || target.classList.contains('modal__wrapper')) {
					modal.classList.remove('active')
				}
			})
		})
	}
	
}

export default startModal