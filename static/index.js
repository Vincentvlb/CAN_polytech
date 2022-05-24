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
    if("couleur" in dataServ){
        let div_5 = document.getElementById("div_5");
        let p = document.createElement("div");
        p.classList.add(dataServ["couleur"])
        p.classList.add("couleur")
        div_5.appendChild(p);
    }
    if("vitesse" in dataServ){
        let div_4 = document.getElementById("div_4");
        let p = document.createElement("p");
        let txt = document.createTextNode(dataServ["vitesse"]);
        p.appendChild(txt);
        div_4.appendChild(p);
    }
    if("force" in dataServ){
        let div_6 = document.getElementById("div_6");
        let p = document.createElement("p");
        let txt = document.createTextNode(dataServ["force"]+" %");
        p.appendChild(txt);
        div_6.appendChild(p);
    }
    if("msg_look" in dataServ){
        let regardez = document.getElementById("regardez");
        let avdj = document.getElementById("avdj");
        if(dataServ["msg_look"]){
            regardez.style.display = null; 
            avdj.style.display = "none";
        }else{
            avdj.style.display = null;  
            regardez.style.display = "none";
        }
    }
    console.log(dataServ)
});