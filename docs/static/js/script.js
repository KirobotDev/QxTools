let wbstrct = document.getElementById("wbstrct")
let dsclogo = document.getElementById("dsclogo")
let web = document.getElementById("wb")
let wbe = document.getElementById("wbe")
let wbee = document.getElementById("wbbe")
let btng = document.getElementById("aigejagij")
const result = document.getElementById("rslt");

wbstrct.addEventListener('click', (e) => {
    window.open("https://github.com/kirobotdev/Qxtools")
})

dsclogo.addEventListener('click', (e) => {
    window.open("https://discord.gg/sorry-i-dont-have-discord")
})

btng.addEventListener("click", (e) => {
    e.preventDefault();

    const el = document.getElementById("rslt");

    const y = el.getBoundingClientRect().top + window.pageYOffset;

    window.scrollTo({
        top: y,
        left: 0,
        behavior: "smooth"
    });
});

setInterval(() => {
    web.style.opacity = "100%"
}, 1000);

setInterval(() => {
    wbe.style.opacity = "100%"
}, 3000);

setInterval(() => {
    wbee.style.opacity = "100%"
}, 5000);

setInterval(() => {
    web.style.opacity = "0%"
    wbe.style.opacity = "0%"
    wbee.style.opacity = "0%"
}, 10000);


window.addEventListener("wheel", function (e) {
    e.preventDefault();

    window.scrollBy({
        top: e.deltaY * 0.1, 
        behavior: "auto"
    });
}, { passive: false });