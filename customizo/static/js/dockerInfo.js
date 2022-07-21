function createTextBox() {
    const dockerImage = document.createElement('div');
    dockerImage.classList.add('form-floating', 'mb-3',);

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.classList.add('form-control');
    const inputId = 'userInput';
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

const docker_images = document.getElementById('docker_images');
function image_validator() {
    console.log(docker_images)
}

(function () {

    const form = document.getElementById('')
    const dockerSwitch = document.getElementById('dockerSwitch');
    const dockerImages = document.getElementById('dockerImages');

    // check_image_existance('ubuntu');

    dockerSwitch.addEventListener('click', function (){
        if(dockerSwitch.checked) {
            const addImage = dockerImages.appendChild(createAddImageBtn());
            document.getElementById('warnings').style.display = '';
            addImage.addEventListener('click', function () {
                console.log("I'm inside dockerInfo.js");
                const image = createTextBox();
                dockerImages.appendChild(image);
            });
        } else {
            document.getElementById('warnings').style.display = 'none';
            dockerImages.innerHTML = '';
        }
    });
})();