function createTextBox(id) {
    const dockerImage = document.createElement('div');
    dockerImage.classList.add('form-floating', 'mb-3',);

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.classList.add('form-control');
    const inputId = 'userInput' + id;
    input.setAttribute('id', inputId);
    input.setAttribute('name', 'dockerImage');
    input.setAttribute('placeholder', 'Docker image');

    const label = document.createElement('label');
    label.setAttribute('for', inputId);
    label.textContent = 'Docker image';

    dockerImage.appendChild(input);
    dockerImage.appendChild(label);

    return dockerImage;
}

function createAddImageBtn() {
    const addImage = document.createElement('button');
    addImage.setAttribute('type', 'button');
    addImage.classList.add('btn', 'btn-outline-primary', 'mb-3');
    addImage.textContent = 'Add image';

    return addImage;
}

function image_validator(image) {
    return docker_images.includes(image);
}

(function () {

    const form = document.getElementById('')
    const dockerSwitch = document.getElementById('dockerSwitch');
    const dockerImages = document.getElementById('dockerImages');

    // check_image_existance('ubuntu');

    let count = 0
    dockerSwitch.addEventListener('click', function (){
        if(dockerSwitch.checked) {
            const addImage = dockerImages.appendChild(createAddImageBtn());
            document.getElementById('warnings').style.display = '';

            addImage.addEventListener('click', function () {
                dockerImages.appendChild(createTextBox(count));
                const input = document.getElementById('userInput' + count);
                input.addEventListener('input', function () {
                    if(!image_validator(input.value)) {
                        input.classList.add('is-invalid')
                    } else {
                        input.classList.remove("is-invalid");
                        input.classList.add('is-valid')
                    }
                });
                count++;
            });
        } else {
            document.getElementById('warnings').style.display = 'none';
            dockerImages.innerHTML = '';
        }
    });
})();