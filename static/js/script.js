const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function openWildberriesLogin() {
    window.open('https://www.wildberries.ru/lk', '_blank');
}

function toggleActive(img) {
    img.classList.toggle('active');
}

document.getElementById("importButton").onclick = function() {
    window.open("D:/BiTry/Альфа банк/Modern-Login/kabinet.html", "_blank");}

    document.getElementById("register").onclick = function() {
        document.getElementById("productTable").style.display = "table";
    }
    document.getElementById("back").onclick = function() {
        window.open("index.html");
    };