var comando = document.getElementById("comando");
var executar = document.getElementById("comando");

var socket = io.connect();

comando.addEventListener("keypress", function(evento){
    if(evento.key == "Enter"){
        evento.preventDefault();
        comando.click();
    }
})

function executarComando(){
    executar = document.getElementById("comando");

    $.ajax({
        url: "/executarComando",
        contentType: 'application/json;charset=UTF-8',
        cache: false,
        method: 'POST',
        dataType: 'json',
        data: JSON.stringify({
            comando: executar.value,
        }),
        success: function(data) {
            console.log(data);
        }
    });

    executar.value = "";
}

socket.on("listCall", async function (msg) {
    var retorno = "<p> Aciona LED: " + msg["ativar-led"] + "</p>";
    retorno += "<p> Aciona Servo: " + msg["ativar-servo"] + "</p>";
    retorno += "<p> Aciona LED durante chuva: " + msg["ativar-led-chuva"] + "</p>";
    retorno += "<p> Aciona Servo durante chuva: " + msg["ativar-servo-chuva"] + "</p>";
    retorno += "<p> <br> </p>";
    

    document.getElementById("terminal-top").innerHTML += retorno;
  });