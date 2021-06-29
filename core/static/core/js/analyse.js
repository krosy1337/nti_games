const csAnalyseBtn = document.querySelector('.analyse_csgo')
const dotaAnalyseBtn = document.querySelector('.analyse_dota')
const logoutButtons = document.querySelectorAll('a.side__account-exit')
const exitModal = document.querySelector('.exit-warning')
const talentLogout = document.querySelector('.user__logout')

function check() {
    if (temp_task_dota_id) {
        startCheckingResultDota({'task_id': temp_task_dota_id});
    }
    if (temp_task_cs_id) {
        startCheckingResultCs({'task_id': temp_task_cs_id})
    }
}

check();

function startCheckingResultDota(response) {
    startCheckingResult(response, 'dota')
}

function startCheckingResultCs(response) {
    startCheckingResult(response, 'cs')
}

function startCheckingResult(response, block) {
    if (checkErrors(response)) return
    checkRes(response.task_id, block);
}

function checkErrors(response) {
    return !!response.error

}

function checkRes(task_id, block) {
    let btnsContainer
    document.querySelectorAll('.game-card__header').forEach(el => {
        if (el.closest(`.game-card_${block}`)) {
            btnsContainer = el
        }
    })
    const btn = btnsContainer.querySelector('.game-card__btn')
    btn.style.display = 'none'
    btnsContainer.insertAdjacentHTML('beforeend', '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>')
    if (block === 'dota') {
        temp_task_dota_id = task_id
    }
    if (block === 'cs') {
        temp_task_cs_id = task_id
    }
    let timerId = setInterval(function () {
        fetch(`/api/analyse/status/?task=${task_id}`)
            .then(response => response.json())
            .then(response_task => {
                if (response_task.status !== "PENDING") {
                    fetch(`/api/analyse/${block}/result`)
                        .then(response => {
                            clearInterval(timerId);
                            location.reload()
                        })
                }
            })

    }, 1000)
}

function logoutClickHandler(event) {
        const el = event.target.closest('a')
        event.preventDefault()
        if (temp_task_dota_id || temp_task_cs_id) {
            exitModal.classList.add('active')

            setTimeout(() => {
                exitModal.classList.remove('active')
            }, 2000)

            return
        }
        el.removeEventListener('click', logoutClickHandler)
        el.click()
    }

if (csAnalyseBtn) {
    csAnalyseBtn.addEventListener('click', () => {
        fetch(temp_cs_start_url, {
            method: 'POST',
            headers: {
                "X-CSRFToken": temp_csrf_token,
                "Accept": "application/json",
                'Content-Type': 'application/json'
            },
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                }
                return false
            })
            .then(response => startCheckingResultCs(response))
    })
    dotaAnalyseBtn.addEventListener('click', () => {
        fetch(temp_dota_start_url, {
            method: 'POST',
            headers: {
                "X-CSRFToken": temp_csrf_token,
                "Accept": "application/json",
                'Content-Type': 'application/json'
            },
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                }
                return false
            })
            .then(response => startCheckingResultDota(response))
    })
}

if (logoutButtons) {
    logoutButtons.forEach(el => {
        el.addEventListener('click', logoutClickHandler)
    })
}

if (talentLogout) {
    talentLogout.addEventListener('click', logoutClickHandler)
}