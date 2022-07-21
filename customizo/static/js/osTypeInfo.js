function additionalInfo() {
    let info = document.createElement("p");
    info.classList.add("mt-3", "align-text-center");
    return info;
}

function createCheckBox(content) {
    let div = document.createElement("div");
    div.classList.add("form-check", "text-start", "mb-3", "col-sm-4");
    let divID = "div_" + content;
    div.setAttribute("id", divID);

    let input = document.createElement("input");
    input.setAttribute("type", "checkbox");
    let checkboxID = "cb_" + content;
    input.setAttribute("id", checkboxID);
    input.setAttribute("name", content);
    input.classList.add("form-check-input");

    let label = document.createElement("label");
    label.setAttribute("for", checkboxID);
    label.classList.add("form-check-label");
    label.innerHTML = content

    div.appendChild(input);
    div.appendChild(label);

    return div;
}

(function () {

    const select = document.getElementById('osType');
    const form = document.getElementById('register_form');
    const checkboxes = document.getElementById('checkboxes');
    const info = document.getElementById('additional_info');

    select.addEventListener('input', function () {
        let osType = select.options[select.selectedIndex].value;

        if (osType == 1 /* INTRUSION DETECTION **/) {
            info.innerHTML = " ";
            info.append(additionalInfo());
            checkboxes.innerHTML = " ";
            checkboxes.appendChild(createCheckBox("aide"));
            checkboxes.appendChild(createCheckBox("iwatch"));
            checkboxes.appendChild(createCheckBox("kismet"));
            checkboxes.appendChild(createCheckBox("packit"));
            checkboxes.appendChild(createCheckBox("samhain"));
            checkboxes.appendChild(createCheckBox("snort"));
            checkboxes.appendChild(createCheckBox("tiger"));

        } else if (osType == 2 /* NETWORK MONITORING **/) {
            info.innerHTML = " ";
            info.append(additionalInfo());
            checkboxes.innerHTML = " ";
            checkboxes.appendChild(createCheckBox("etherape"));
            checkboxes.appendChild(createCheckBox("icinga2"));
            checkboxes.appendChild(createCheckBox("nagios4"));
            checkboxes.appendChild(createCheckBox("ssldump"));
            checkboxes.appendChild(createCheckBox("wireshark"));
            checkboxes.appendChild(createCheckBox("wmnet"));
        }
    });
})();