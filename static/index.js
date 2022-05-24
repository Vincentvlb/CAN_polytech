const socket = io.connect('http://' + document.domain + ':' + location.port + '/ihm');

function reset_div(){
    let div_1 = document.getElementById("div_1");
    let div_2 = document.getElementById("div_2");
    let div_3 = document.getElementById("div_3");
    let div_4 = document.getElementById("div_4");
    let div_5 = document.getElementById("div_5");
    let div_6 = document.getElementById("div_6");
    div_1.innerHTML = '';
    div_2.innerHTML = '';
    div_3.innerHTML = '';
    div_4.innerHTML = '';
    div_5.innerHTML = '';
    div_6.innerHTML = '';
}

socket.on('ihm', function(dataServ) {
    reset_div();
    if("joystick" in dataServ){
        let div_3 = document.getElementById("div_3");
        let node = document.createTextNode(dataServ["joystick"]);
        div_3.appendChild(node);
    }
    if("btn" in dataServ){
        let div_1 = document.getElementById("div_1");
        let p = document.createElement("p");
        let txt = document.createTextNode(dataServ["btn"]);
        p.classList.add(dataServ["btn"])
        p.appendChild(txt);
        div_1.appendChild(p);
    }
    console.log(dataServ)
});