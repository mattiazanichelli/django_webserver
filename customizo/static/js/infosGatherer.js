(function () {

    const user = {
        firstname: " ",
        lastname: " ",
        email: " ",
        osType: " ",
        packages: [],
    }

    const firstname = document.getElementById('firstname');
    const lastname = document.getElementById('lastname');
    const email = document.getElementById('useremail');
    const osType = document.getElementById('os_type_option');
    const packages = document.getElementById('checkboxes');

    for (let elem of document.querySelectorAll('*')) {
        elem.addEventListener('click', e => {
            if (e.target.id == "register_submit") {
                submitEventHandler();
            }
        }, true);
        break;
    }

    function createDownloadableContent(jsonObject) {
        const data = new Blob([jsonObject]);
        downloadable = URL.createObjectURL(data);

        const form = document.getElementById("register_form");

        if (!document.querySelector("#downloadable")) {
            const a = document.createElement("a");
            a.setAttribute("href", downloadable);
            a.id = "downloadable";
            a.innerText = "Download";
            a.download = "customizo.json";
            form.appendChild(a);
        }
    }

    function submitEventHandler() {
        user.firstname = firstname.value;
        user.lastname = lastname.value;
        user.email = email.value;
        user.osType = osType.value;

        let array = [];
        for (let div of packages.childNodes) {
            if (div.id) {
                for (checkbox of div.childNodes) {
                    if (checkbox.checked) {
                        array.push(checkbox.id);
                    }
                }
            }
        }

        array.forEach((element, index) => {
            element = element.substr(3);
            array[index] = element;
        });

        user.packages = array;

        const userJSON = JSON.stringify(user);
        createDownloadableContent(userJSON);
    }

})();