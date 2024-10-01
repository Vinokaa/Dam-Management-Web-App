# Monitoramento de Barragens

Esse projeto foi feito por mim e meu grupo da universidade, e sua premissa é de monitorar e controlar o nível de barragens, buscando evitar o seu vazamento. Para isso, utilizamos um sensor de distância (HC-SR04) e um sensor de umidade (DHT22) para monitorar a distância e ter um controle mais rigoroso caso esteja chovendo. Além disso, também utilizamos dois atuadores, um LED para indicar um nível de alerta do nível da água e um Servo Motor para ativar um válvula de escoamento de água caso a água atinja níveis emergenciais.

Utilizamos o dispositivo ESP32, que é um dispositivo muito comum em aplicações IoT (Internet of Things), possibilitando uma comunicação via internet, e assim utilizamos o protocolo MQTT, WebSockets e jQuery para comunicação bidirecional entre o site e os sensores e atuadores conectados na ESP32.

O site foi feito majoritariamente por meio do framework Flask para Python, o qual facilita o desenvolvimento do back-end.

Link do código da ESP32 implementado no site Wokwi para simulação: https://wokwi.com/projects/395606807700840449

# Página Inicial

Eu e meu grupo implantamos um sistema de controle de cargos, logo, cada cargo possui uma tela inicial diferente.
<br> <br>

![Captura de Tela (161)](https://github.com/user-attachments/assets/6266360a-0858-442a-b49a-2c4d17612b01)
<p align="center"><i> Página inicial do admin com todas as opções </i></p>
<br>

![Captura de Tela (160)](https://github.com/user-attachments/assets/20061829-954e-4c6a-a11e-369e8acf7211)
<p align="center"><i> Página inicial do cargo estatístico, podendo vizualizar os dados em tempo real </i></p>
<br>

![Captura de Tela (159)](https://github.com/user-attachments/assets/af369d18-456c-499e-9b15-94890edeaa6a)
<p align="center"><i> Página inicial do cargo operador, podendo executar comandos remotos </i></p>
<br> <br>

# Funcionamento

Definimos dois valores, um valor para ativar o LED de alerta caso a água atinja esse nível e um valor para ativar o Servo (Válvula de escoamento) caso a água atinja níveis extremos.
<br> <br>

![Funcionamento](https://github.com/user-attachments/assets/40d68cb4-e609-4310-9d4f-47632a11e826)
<br> <br>

Como dito anteriormente, foram definidos valores de alerta e emergência, porém esses valores podem ser alterados a qualquer momento à distância por meio de um console.
<br> <br>

![Comandos](https://github.com/user-attachments/assets/63d75462-6f21-4723-a5fd-ae5b67ce49ad)
<br> <br>

Alguns dados, como leituras de sensores, execução de comandos, login/logout são todos salvos em um banco de dados para a persistência de dados, podendo ser consultados posteriormente.
<br> <br>

![Historico](https://github.com/user-attachments/assets/012dc2f2-93f6-4965-909a-43edfe22b35c)
