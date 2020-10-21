var x = document.getElementById("cars");
x.style.display = "none";

function sayHello() {
   alert("Hello World")
}

async function getList() {
    let url = Flask.url_for("my_list");
    try {
        let res = await fetch(url);
        let a = await res.json();
        return a;
    } catch (error) {
        console.log(error);
    }
}

async function renderList() {
    let my_list = await getList();
    let text = "";
    for(var i = 0; i < my_list.length; i++) {
        text += `<option value='${my_list[i]}'>${my_list[i]}</option>`
    }
    document.getElementById("cars").innerHTML = text;
    x.style.display = "block";
}