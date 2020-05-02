/* -- SELECTORS -- */
const previews = document.querySelector(".previews");
const mainPhoto = document.querySelector(".main_photo");
const leftArrow = document.querySelector(".left.arrow");
const rightArrow = document.querySelector(".right.arrow");

/* -- PAGINATION -- */
let page = 1;
let finalPhotos = [];
let tempPhotos = [];
let perPage = 5;
for (i = 0; i < photos.length; i += perPage) {
    for (x = 0; x < perPage; x++) {
        try {
            tempPhotos.push(photos[i + x]);
        } 
        catch (error) {
            break;
        }
    }
    finalPhotos.push(tempPhotos);
    tempPhotos = [];
}

/* -- EVENT LISTENERS -- */
leftArrow.addEventListener("click", () => {
    if (page > 1) {
        page -= 1;
    }
    if (page == 1) {
        leftArrow.classList.add("hidden");
    }
    if (page < finalPhotos.length) {
        rightArrow.classList.remove("hidden");
    }
    updatePreview(page);
});

rightArrow.addEventListener("click", () => {
    page += 1;
    if (page == finalPhotos.length) {
        rightArrow.classList.add("hidden");
    }
    if (page > 1) {
        leftArrow.classList.remove("hidden");
    }
    updatePreview(page);
})

window.onload = updatePreview(1);

/* -- FUNCTIONS -- */
function updatePreview(pageNumber) {
    let old = previews.children;
    if (old.length > 1) {
        for (i = 0; i < old.length; i) {
            previews.removeChild(old[i]);
        }
    }
    let currentPage = finalPhotos[pageNumber - 1];
    
    currentPage.forEach(element => {
        if (element != undefined) {
            let newImg = document.createElement("img");
            newImg.src = element;
            newImg.className = "photo";
            newImg.addEventListener("click", () => {
                updateCurrentPhoto(newImg);
            })
            previews.appendChild(newImg);
        }
    });
}

function updateCurrentPhoto(photo) {
    mainPhoto.src = photo.src;

    let old = document.querySelector(".selected");
    if (old != undefined) {        
        old.classList.remove("selected");
    }
    photo.classList.add("selected");
}