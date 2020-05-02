const leftPreviewFull = document.querySelector(".left_preview");
const rightPreviewFull = document.querySelector(".right_preview");
const mainPhotoFull = document.querySelector(".main_photo_full");
const previewsFull = document.querySelector(".previews_full");
const rightArrowMain = document.querySelector(".right_main");
const leftArrowMain = document.querySelector(".left_main");
const exit = document.querySelectorAll(".exit");
let currentPhoto = 0;

page = 1;
updatePreviewsFull(page);

rightArrowMain.addEventListener("click", () => {
    if (currentPhoto < finalPhotos[page-1].length - 1) {
        currentPhoto += 1;
        mainPhotoFull.src = finalPhotos[page-1][currentPhoto];
    }
    else {
        try {
            currentPhoto = 0;
            page += 1;
            updatePreviewsFull(page);
        }
        catch {
            
        }
    }
})

leftArrowMain.addEventListener("click", () => {
    if (currentPhoto > 0) {
        currentPhoto -= 1;
        mainPhotoFull.src = finalPhotos[page-1][currentPhoto];
    }
    else if (page > 1) {
        try {
            currentPhoto = 0;
            page -= 1;
            updatePreviewsFull(page);
        }
        catch {
            
        }
    }
})

leftPreviewFull.addEventListener("click", () => {
    if (page > 1) {
        page -= 1;
    }
    updatePreviewsFull(page);
});

rightPreviewFull.addEventListener("click", () => {
    page += 1;
    updatePreviewsFull(page);
})

document.addEventListener("keydown", (e) => {
    if (e.key == "Escape") {
        document.querySelector(".slideshows").classList.add("inactive")
    }
});

exit.forEach(e => {
    e.addEventListener("click", () => {
        document.querySelector(".slideshows").classList.add("inactive")
    })
})


mainPhoto.addEventListener("click", () => {
    document.querySelector(".slideshows").classList.remove("inactive");
    updateCurrent(0);
});

function updatePreviewsFull(pageNumber) {
    if (page == 1) {
        leftPreviewFull.classList.add("hidden");
    }
    if (page < finalPhotos.length) {
        rightPreviewFull.classList.remove("hidden");
    }
    if (page == finalPhotos.length) {
        rightPreviewFull.classList.add("hidden");
    }
    if (page > 1) {
        leftPreviewFull.classList.remove("hidden");
    }
    
    let old = previewsFull.children;
    if (old.length > 1) {
        for (i = 0; i < old.length; i) {
            previewsFull.removeChild(old[i]);
        }
    }
    let currentPage = finalPhotos[pageNumber - 1];
    
    currentPage.forEach(element => {
        if (element != undefined) {
            let newImg = document.createElement("img");
            newImg.src = element;
            newImg.className = "photo";
            newImg.addEventListener("click", () => {
                updateCurrentPhotoFull(newImg);
            })
            previewsFull.appendChild(newImg);
        }
    });
    mainPhotoFull.src = currentPage[0];
}

function updateCurrentPhotoFull(photo) {
    mainPhotoFull.src = photo.src;

    let old = document.querySelector(".selected");
    if (old != undefined) {        
        old.classList.remove("selected");
    }
    photo.classList.add("selected");
}
