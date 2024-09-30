var root = document.querySelector(":root");

var socket = io.connect();

function fill(last_fill, new_fill){
    root.style.setProperty("--start", last_fill);
    root.style.setProperty("--stop", new_fill);
}

socket.on("updateSensorData", async function (msg) {
    console.log("Received sensorData :: " + msg.last_dist + " :: " + msg.new_dist);

    document.getElementById("HC-SR04").innerHTML = msg.value + "cm";
    document.getElementById("DHT22").innerHTML = msg.dht22 + "%";
    document.getElementById("LED").innerHTML = msg.led;
    document.getElementById("Servo").innerHTML = msg.servo + "º";

    fill(msg.last_dist, msg.new_dist)

    var container = document.getElementById("arco");
    var content = container.innerHTML;
    container.innerHTML = content;

    var circleText = document.getElementById("arco-text");
    var inicio = parseInt(circleText.innerHTML.replace("cm", ""));
    var fim = msg.value;

    if(fim > inicio){
        for(var i = inicio; i < fim; i++){
            circleText.innerHTML = i + "cm";
            await new Promise(r => setTimeout(r, 2000 / (fim-inicio)));
        }
    }else{
        for(var i = inicio; i > fim; i--){
            circleText.innerHTML = i + "cm";
            await new Promise(r => setTimeout(r, 2000 / (inicio-fim)));
        }
    }
  });