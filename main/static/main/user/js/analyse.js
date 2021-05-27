const csAnalyseBtn = document.querySelector('.analyse_csgo')
const dotaAnalyseBtn = document.querySelector('.analyse_dota')
const overwatchAnalyseBtn = document.querySelector('.analyse_overwatch')

if (csAnalyseBtn) {
    csAnalyseBtn.addEventListener('click', () => {
        const btnsContainer = csAnalyseBtn.closest('.main__game-buttons')
        btnsContainer.querySelectorAll('.main__game-button').forEach(btn => {
		    btn.classList.add('hidden')
	    })
        btnsContainer.insertAdjacentHTML('afterbegin', '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>')
        fetch(url=temp_cs_start_url, {
            data: {'csrfmiddlewaretoken': temp_csrf_token},
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                }
                return false
            })
            .then(data => {
                location.reload()
                // btnsContainer.querySelector('.lds-ellipsis').remove()
                // btnsContainer.querySelectorAll('.main__game-button').forEach(btn => {
		        //     btn.classList.remove('hidden')
	            // })
                // btnsContainer.querySelector('.main__game-button_a').classList.add('hidden')
                //
                //
            })
    })
    dotaAnalyseBtn.addEventListener('click', () => {
        const btnsContainer = dotaAnalyseBtn.closest('.main__game-buttons')
        btnsContainer.querySelectorAll('.main__game-button').forEach(btn => {
		    btn.classList.add('hidden')
	    })
        btnsContainer.insertAdjacentHTML('afterbegin', '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>')
        fetch(url=temp_dota_start_url, {
            data: {'csrfmiddlewaretoken': temp_csrf_token},
        })
            .then((response) => {
                if (response.ok) {
                    return response.json()
                }
                return false
            })
            .then(data => {
                location.reload()
            })
    })
    overwatchAnalyseBtn.addEventListener('click', () => {
        const btnsContainer = overwatchAnalyseBtn.closest('.main__game-buttons')
        btnsContainer.querySelectorAll('.main__game-button').forEach(btn => {
		    btn.classList.add('hidden')
	    })
        btnsContainer.insertAdjacentHTML('afterbegin', '<div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>')
        fetch(url=temp_overwatch_start_url, {
            data: {'csrfmiddlewaretoken': temp_csrf_token},
        })
            .then((response) => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                location.reload()
            })
    })
}

