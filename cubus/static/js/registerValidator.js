(function () {

    function namesValidator(input) {
        const letters = /^[A-Za-z]+$/;
        return !!input.value.match(letters);
    }

    function emailValidator(input) {
        const mail_format = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
        return !!input.value.match(mail_format);
    }

    const register_form = document.querySelector("#register_form");
    const first_name = document.getElementById("firstName");
    const last_name = document.getElementById("lastName");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirm_password = document.getElementById("confirm_password")


    let f_name_valid = false;
    let l_name_valid = false;
    let email_valid = false;
    let password_valid = false;

    first_name.addEventListener('input', function () {
        if (!namesValidator(first_name)) {
            first_name.classList.add("is-invalid");
            f_name_valid = false;
            document.getElementById('firstnameError').innerHTML = "The name can only contain uppercase and lowercase letters";
        } else {
            first_name.classList.remove("is-invalid");
            first_name.classList.add("is-valid");
            f_name_valid = true;
            document.getElementById('firstnameError').innerHTML = "";
        }
    });

    last_name.addEventListener('input', function () {
        if (!namesValidator(last_name)) {
            last_name.classList.add("is-invalid");
            l_name_valid = false;
            document.getElementById('lastnameError').innerHTML = "The last name can only contain uppercase and lowercase letters";
        }
        else {
            last_name.classList.remove("is-invalid");
            last_name.classList.add("is-valid");
            l_name_valid = true;
            document.getElementById('lastnameError').innerHTML = "";
        }
    });

    email.addEventListener('input', function () {
        if (!emailValidator(email)) {
            email.classList.add("is-invalid");
            email_valid = false;
            document.getElementById('emailError').innerHTML = "Invalid email";
        } else {
            email.classList.remove("is-invalid");
            email.classList.add("is-valid");
            email_valid = true;
            document.getElementById('emailError').innerHTML = "";
        }
    });

    confirm_password.addEventListener('input', function () {
        if(!passwordValidator()) {
            confirm_password.classList.add("is-invalid");
            password_valid = false;
            document.getElementById('confirmPasswordError').innerHTML = "Passwords don't match";
        } else {
            confirm_password.classList.remove("is-invalid");
            confirm_password.classList.add("is-valid");
            password_valid = true;
            document.getElementById('confirmPasswordError').innerHTML = "";
        }
    })

    function passwordValidator() {
        return password.value === confirm_password.value
    }

    function createButton() {
        const submit = document.querySelector("#register_submit");
        if (submit) {
            return;
        }

        const button = document.createElement("input");
        button.id = "register_submit";
        button.type = "submit";
        button.value = "Register";
        button.classList.add("btn", "btn-outline-primary", "btn-lg", "lx", "mb-3", "mt-3", "fw-bold");
        button.style.height = "50px";
        button.style.width = "150px";
        register_form.appendChild(button);
    }

    function removeButton() {
        const submit = document.querySelector("#register_submit");
        if (submit) {
            register_form.removeChild(submit);
        }
    }

    register_form.addEventListener('input', function () {
        if (f_name_valid && l_name_valid && email_valid && password_valid) {
            createButton();
        } else {
            removeButton();
        }
    });

})();