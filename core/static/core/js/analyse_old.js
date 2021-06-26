function check() {
    if (temp_task_dota_id) {
        start_checking_result_dota({'task_id': temp_task_dota_id});
    }
    if (temp_task_cs_id) {
        start_checking_result_cs({'task_id': temp_task_cs_id})
    }
}

check();

$('#dota_process').click(function () {
    $.ajax({
        type: "POST",
        url: temp_dota_start_url,
        data: {'csrfmiddlewaretoken': temp_csrf_token},
        dataType: "json",
        success: start_checking_result_dota,
        error: function (rs, e) {
            {
                // alert(rs.responseText);
            }
        }
    });
})

$('#cs_process').click(function () {
    $.ajax({
        type: "POST",
        url: temp_cs_start_url,
        data: {'csrfmiddlewaretoken': temp_csrf_token},
        dataType: "json",
        success: start_checking_result_cs,
        error: function (rs, e) {
            {
                // alert(rs.responseText);
            }
        }
    });
})

function start_checking_result_dota(response) {
    start_checking_result(response, 'dota')
}

function start_checking_result_cs(response) {
    start_checking_result(response, 'cs')
}

function start_checking_result(response, block) {
    if (check_errors(response, block)) return;

    hide_score(block);
    update_message("В процессе обработки...", block);

    check_res(response.task_id, block);
}

function check_res(task_id, block) {
    var timerId = setInterval(function () {
        $.ajax({
            type: "GET",
            url: "/api/analyse/status/",
            data: {'task': task_id},
            dataType: "json",
            success: function (response_task) {
                if (response_task.status !== "PENDING") {
                    console.log(1)
                    $.ajax({
                        type: "GET",
                        url: `/api/analyse/${block}/result`,
                        dataType: "json",
                        success: function (response) {
                            console.log(response);
                            if (response.error) {
                                check_errors(response, block);
                                clearInterval(timerId);
                            } else {
                                update_score(block, JSON.parse(response.result));
                                hide_message(block);
                                clearInterval(timerId);
                            }
                        },
                        error: function (rs, e) {
                            {
                                // alert(rs.responseText);
                            }
                        }
                    });
                }
            },
            error: function (rs, e) {
                {
                    // alert(rs.responseText);
                }
            }
        });

    }, 1000);
}

function update_message(message, block) {
    show_message(block);
    document.getElementById(`${block}-info`).innerText = message;
}

function show_message(block) {
    document.getElementById(`${block}-info`).style.display = "";
}

function hide_message(block) {
    document.getElementById(`${block}-info`).style.display = "none";
}

function show_score(block) {
    document.getElementById(`${block}-score`).style.display = "";
}

function hide_score(block) {
    document.getElementById(`${block}-score`).style.display = "none";
}

function update_score(block, score) {
    show_score(block);
    console.log(score)
    for (const [key, value] of Object.entries(score)) {
        console.log(key, value)
        document.getElementById(`${block}-${key}-score`).innerText = value;
    }
}

function check_errors(response, block) {
    if (response.error) {
        update_message(response.error, block)
        return true;
    }
    return false;
}