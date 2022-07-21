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

// function createDockerImagesDiv() {
//     const dockerImages = document.createElement('div');
//     dockerImages.setAttribute('id', 'dockerImages');
//     dockerImages.classList.add('form-floating', 'mb-3', 'col-lg-4', 'text-dark');
//
//     return dockerImages;
// }

// function checkIfImageExists(dockerImage) {
//     const promise = fetch(`https://hub.docker.com/_/${dockerImage}`);
//     console.log(promise);
//     let request = new XMLHttpRequest();
//     request.open('GET', `https://hub.docker.com/_/${dockerImage}`, true);
//     request.onreadystatechange = function() {
//         if(request.readyState === 4) {
//             if(request.status === 404) {
//                 console.log("Oh no, it does not exist!")
//                 // alert("Oh no, it does not exist!");
//             }
//         }
//     };
//     request.send();
// }


function insertWarning(parent) {
    const typoWarning = document.createElement('p');
    typoWarning.classList.add('text-warning');
    typoWarning.textContent = 'Try to insert docker images correctly!' +
        'Any docker image not correctly specified will not be insluded in the final system!';

    const repoWarning = document.createElement('p');
    repoWarning.classList.add('text-warning');
    const link = document.createElement('a');
    link.setAttribute('href', 'https://hub.docker.com/search?q=&operating_system=linux');
    link.textContent = 'Docker Hub';
    repoWarning.textContent = 'Please refer to the official' + link +
        ' for information about images names';

    parent.appendChild(typoWarning);
    parent.appendChild(repoWarning);
}

(function () {

    const form = document.getElementById('')
    const dockerSwitch = document.getElementById('dockerSwitch');
    const dockerImages = document.getElementById('dockerImages');

    dockerSwitch.addEventListener('click', function (){
        if(dockerSwitch.checked) {
            const addImage = dockerImages.appendChild(createAddImageBtn());
            document.getElementById('warnings').style.display = '';
            addImage.addEventListener('click', function () {
               dockerImages.appendChild(createTextBox());
            });
        } else {
            document.getElementById('warnings').style.display = 'none';
            dockerImages.innerHTML = '';
        }
    });
})();