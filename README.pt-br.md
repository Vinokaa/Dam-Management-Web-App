# Aplicação Web para Monitoramento de Barragens

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Vinokaa/Dam-Management-Web-App/blob/main/README.md)

Esse projeto foi feito por mim e meu grupo da universidade para a matéria de Experiência Criativa: Criando Soluções Computacionais, e sua premissa é de monitorar e controlar o nível da água em barragens, buscando evitar seu vazamento.

Para isso, nós utilizamos um sensor de distância (HC-SR04) e um sensor de umidade (DHT22) para monitorar o nível da água¹ e ter um controle mais rigoroso quando estiver chovendo. Além disso, nós também utilizamos dois atuadores, um LED para representar um aviso sobre o nível da água e um Servo motor para ativar uma válvula de drenagem se o nível da água atingir valores perigosos.

Nós utilizamos o dispositivo ESP32, o qual é muito comum em aplicações IoT (Internet of Things), em conjunto com o software MicroPython, o qual nos permitiu escrever o código para os microcontroladores em Python. O uso do ESP32 nos possibilitou utilizar a internet, por meio do protocolo MQTT, WebSockets e JQuery, para comunicação bidirecional entre a aplicação web e os sensores e atuadores.

A aplicação web foi feita majoritariamente com o framework Flask com Python, e o WebSockets foi uma solução que achamos para compensar um problema que tivemos utilizando o Flask, que é o fato de que o Flask não consegue atualizar dados no website sem antes recarregá-lo, mas o WebSockets consegue criar uma conexão entre o Flask, o qual possui os dados lidos pelos sensores, e o JavaScript, o qual consegue atualizar os dados no website em tempo real.

Link para a implementação do código do ESP32 para simulação: https://wokwi.com/projects/395606807700840449

> ¹ Por conta do comportamento refletivo da água, posicionar o sensor de distância no nível máximo da barragem apontado para a água seria inviável. Como uma solução alternativa, o HC-SR04 e o ESP32 devem ficar em um recipiente à prova d'água e posicionado em uma parte específica da barragem que tenha uma superfície sólida no nível máximo da água, ou seja, conforme o nível da água sobe, a superfície com o HC-SR04 se aproxima da superfície sólida que representa o nível máximo de água da barragem, e uma leitura de 0 cm de distância significaria que a água atingiu seu nível máximo.

# Página Principal

Eu e meu grupo implantamos um sistema de controle por cargos, ou seja, cada cargo possui uma página principal diferente.
<br> <br>

<img src="https://github.com/user-attachments/assets/6266360a-0858-442a-b49a-2c4d17612b01">

<p align="center"><i> Página principal do admin, com todas as opções disponíveis </i></p>
<br>

<img src="https://github.com/user-attachments/assets/20061829-954e-4c6a-a11e-369e8acf7211">
<p align="center"><i> Página principal do cargo Estatístico, tendo acesso à visualização de dados em tempo real </i></p>
<br>

<img src="https://github.com/user-attachments/assets/af369d18-456c-499e-9b15-94890edeaa6a">
<p align="center"><i> Página principal do cargo Operador, tendo acesso à execução de comandos remotos </i></p>
<br> <br>

# Funcionamento

Nós definimos dois valores de referência, se a leitura do nível da água pelo sensor atinge o primeiro valor de referência (valor de aviso), o LED é ativado, alertando que a água atingiu o nível de aviso, e se a leitura atinge o segundo valor de referência (valor de emergência), o Servo (válvula de escoamento) é ativado.
<br> <br>

<img src="https://github.com/user-attachments/assets/40d68cb4-e609-4310-9d4f-47632a11e826">
<br> <br>

O valores de aviso e emergência podem ser facilmente modificados através do console por um operador ou admin, sem necessitar acessar o ESP32 manualmente.
<br> <br>

<img src="https://github.com/user-attachments/assets/63d75462-6f21-4723-a5fd-ae5b67ce49ad">
<br> <br>

Alguns dados, como leituras de sensores, execuções de comandos, login/logout são armazenados em memória, e podem ser visualizados a qualquer momento por um estatístico ou admin.
<br> <br>

<img src="https://github.com/user-attachments/assets/012dc2f2-93f6-4965-909a-43edfe22b35c">
