(function () {

    const create_form = document.querySelector("#create_form");
    const iso_name = document.getElementById('isoName')
    const select = document.getElementById('osType');


    let entered_name = false;
    let option_selected = false;


    function check_name_presence() {
        return iso_name.value !== ""
    }


    iso_name.addEventListener('input', function() {
        if(iso_name.value === "") {
            iso_name.classList.add("is-invalid");
            entered_name = false;
            document.getElementById('isoNameError').innerHTML = "Please enter a name for your custom ISO";
        } else if(iso_name.value === "ubuntu-22.04-live-server-amd64") {
            iso_name.classList.add("is-invalid");
            entered_name = false;
            document.getElementById('isoNameError').innerHTML = "Please choose another name for your custom ISO";
        } else {
            iso_name.classList.remove("is-invalid");
            iso_name.classList.add("is-valid");
            entered_name = true;
            document.getElementById('isoNameError').innerHTML = "";
        }
    });


    select.addEventListener('input', function() {
        const value = select.options[select.selectedIndex].value;

        if (value == 1 || value == 2) {
            option_selected = true;
        } else {
            option_selected = false;
        }
    })

    function createButton() {
        const submit = document.querySelector("#create_submit");
        if (submit) {
            return;
        }

        const button = document.createElement("input");
        button.id = "create_submit";
        button.type = "submit";
        button.value = "Generate ISO";
        button.classList.add("btn", "btn-outline-primary", "btn-lg", "t-3", "p-3", "mb-3");
        create_form.appendChild(button);
    }

    function removeButton() {
        const submit = document.querySelector("#create_submit");
        if (submit) {
            create_form.removeChild(submit);
        }
    }

    create_form.addEventListener('input', function () {
        entered_name = check_name_presence();

        if (entered_name && option_selected) {
            createButton();
        } else {
            removeButton();
        }
    });

})();