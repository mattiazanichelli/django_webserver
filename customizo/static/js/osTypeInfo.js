function additionalInfo() {
    let info = document.createElement("p");
    info.classList.add("mt-3", "align-text-center");
    return info;
}

function createCheckBox(content) {
    let div = document.createElement("div");
    div.classList.add("form-check", "mb-3");
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
    const checkboxes = document.getElementById('checkboxes');
    const info = document.getElementById('additional_info');

    select.addEventListener('input', function () {
        let osType = select.options[select.selectedIndex].value;

        if (osType == 1 /* INTRUSION DETECTION **/) {
            info.innerHTML = " ";
            info.append(additionalInfo());
            checkboxes.innerHTML = " ";
            // Padding left to match Network Monitoring positions
            checkboxes.setAttribute("style", "padding-left: 52px")
            checkboxes.appendChild(createCheckBox("aide"));
            checkboxes.appendChild(createCheckBox("checksecurity"));
            checkboxes.appendChild(createCheckBox("iwatch"));
            checkboxes.appendChild(createCheckBox("packit"));
            checkboxes.appendChild(createCheckBox("snort"));
            checkboxes.appendChild(createCheckBox("stenographer"));
            checkboxes.appendChild(createCheckBox("suricata"));
            checkboxes.appendChild(createCheckBox("tiger"));
            checkboxes.appendChild(createCheckBox("tripwire"));

        } else if (osType == 2 /* NETWORK MONITORING **/) {
            info.innerHTML = " ";
            info.append(additionalInfo());
            checkboxes.innerHTML = " ";
            checkboxes.removeAttribute("style")
            checkboxes.appendChild(createCheckBox("etherape"));
            checkboxes.appendChild(createCheckBox("fierce"));
            checkboxes.appendChild(createCheckBox("icinga2"));
            checkboxes.appendChild(createCheckBox("nagios4"));
            checkboxes.appendChild(createCheckBox("netcat"));
            checkboxes.appendChild(createCheckBox("netsed"));
            checkboxes.appendChild(createCheckBox("nmap"));
            checkboxes.appendChild(createCheckBox("ssldump"));
            checkboxes.appendChild(createCheckBox("wireshark"));
            checkboxes.appendChild(createCheckBox("wmnet"));
        }
    });
})();