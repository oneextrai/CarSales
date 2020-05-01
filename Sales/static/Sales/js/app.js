/* -- SELECTORS -- */
const cards = document.querySelectorAll(".card");
const contents = document.querySelector(".content");
const navBar = document.querySelector(".responsive_header");
const burger = document.querySelector(".burger");
const searchField = document.querySelector("select");

/* -- EVENT LISTENERS -- */
cards.forEach(card => {
    card.addEventListener("mouseover", () => {
        card.children[1].classList.remove("hidden");
    })
    card.addEventListener("mouseout", () => {
        card.children[1].classList.add("hidden");
    })
});

burger.addEventListener("click", () => {
    navBar.classList.toggle("active");
})

window.addEventListener("resize", () => {
    if (window.innerWidth >= 1024) {
        navBar.classList.remove("active");
    }
});

searchField.onchange = () => {
    cards.forEach(card => {
        if (searchField.value == "*") {
            card.classList.remove("inactive");
        }
        else if (!card.classList.contains(searchField.value.split(' ')[0])) {
            console.log(card);
            card.classList.add("inactive");
        }
        else {
            card.classList.remove("inactive");
        }
    });
};

window.onload = () => {
    const photos = document.querySelectorAll(".photo");
    console.log(photos);
}