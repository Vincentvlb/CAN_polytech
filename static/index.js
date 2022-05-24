const socket = io.connect('http://' + document.domain + ':' + location.port + '/ihm');

socket.on('ihm', function(dataServ) {
    console.log(dataServ)
});