function startTooltipProgress() {
    const tooltipProgress = document.querySelector('.tooltip__progress')

    if (tooltipProgress) {
        const score = tooltipProgress.dataset.score

        const tooltipProgressBlock = document.querySelector('.tooltip__progress-block')
        const tooltipProgressMarker = document.querySelector('.tooltip__progress-marker')
        tooltipProgressBlock.style.width = `${score}%`
        tooltipProgressMarker.style.left = `${score}%`
    }
}

export default startTooltipProgress