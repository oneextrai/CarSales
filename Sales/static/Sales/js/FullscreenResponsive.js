const mainRes = document.querySelector(".res_photo_full");
const rightArrowRes = document.querySelector(".next");
const leftArrowRes = document.querySelector(".prev");
const numbers = document.querySelector(".numbers");

currentPhoto = 0;

rightArrowRes.addEventListener("click", getPreviousImage);

leftArrowRes.addEventListener("click", getNextImage);

mainRes.addEventListener("swiped-left", getPreviousImage);
mainRes.addEventListener("swiped-right", getNextImage);

function updateCurrent(index) {
    mainRes.src = photos[index];
    numbers.innerText = `${currentPhoto + 1}/${photos.length}`;
}

function getPreviousImage() {
    if (currentPhoto < photos.length) {
        currentPhoto += 1;
        updateCurrent(currentPhoto);
        leftArrowRes.classList.remove("hidden");
    };
    if (currentPhoto == photos.length - 1) {
        rightArrowRes.classList.add("hidden");
    }
};

function getNextImage() {
    if (currentPhoto > 0) {
        currentPhoto -= 1;
        updateCurrent(currentPhoto);
        rightArrowRes.classList.remove("hidden");
    };
    if (currentPhoto == photos.length - 1) {
        rightArrowRes.classList.add("hidden");
    }
    if (currentPhoto == 0) {
        leftArrowRes.classList.add("hidden");
    }
}