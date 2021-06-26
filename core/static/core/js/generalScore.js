function startGeneralScore() {
    const generalScore = document.querySelector('.general-stats')

    if (generalScore) {
        const scoreText = document.querySelector('.general-stats__score')
        const score = generalScore.dataset.score

        let n = +score
        let base = 'очк'

        if ((n % 10 === 0) || (n % 10 > 4) & (n % 10 < 10) || (n % 100 > 10) & (n % 100 < 15)) {
            scoreText.textContent = `${n} ${base + 'ов'}`
        } else if ((n % 10 > 1) & (n % 10 < 5)) {
            scoreText.textContent = `${n} ${base + 'а'}`
        } else {
            scoreText.textContent = `${n} ${base + 'о'}`
        }

        const blockWidth = generalScore.clientWidth

        const marker = generalScore.querySelector('.general-stats__marker')
        const toner = generalScore.querySelector('.general-stats__toner')

        const offset = (blockWidth * score / 100) - marker.clientWidth / 2

        marker.style.left = `${score}%`
        toner.style.left = `${score}%`
    }
}

export default startGeneralScore