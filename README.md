# Dam Management Web Application

[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Vinokaa/Dam-Management-Web-App/blob/master/README.pt-br.md)

This project was made by me and my university group for the Creative Experience: Creating Computing Solutions classes (originally Experiência Criativa: Criando Soluções Computacionais), and it's purpose is to manage and control the water level of dams, aiming to keep it from overflowing.

In order to achieve that, we used a distance sensor (HC-SR04) and a humidity sensor (DHT22) to monitor the water level¹ and have a more strict control when it's raining. In addition to that, we also used two actuators, one LED to represent a minor warning about the water level and a Servo to activate an emergency drainage pipe if the water reaches dangerous levels.

We used the ESP32 device, which is very common in IoT applications, along with the MicroPython software, which let us write the code for the microcontrollers in Python. The usage of the ESP32 made it possible for us to use the internet, via MQTT protocol, WebSockets and JQuery, for bidirectional communication between the web application and the sensors and actuators.

The web app was mainly made using the Flask framework for Python, and WebSockets was a solution that we found to overcome the only problem that we faced using Flask, which is that Flask can't update data in the website without reloading it, but WebSockets can create a connection between Flask, that has the data collected by the sensor, and JavaScript, which can update data in the website in real-time.

Link to the implementation of the ESP32 code for simulation: https://wokwi.com/projects/395606807700840449

> ¹ Due to water's wave reflecting behavior, placing the distance sensor at the dam's max level aimed at the water would be unfeasible. As an alternate solution, the HC-SR04 and the ESP32 would be made waterproof and placed in a specific part of the dam in a floating surface that would have a solid surface at the dam's max water level, meaning that, as the water level goes up, the floating surface with the HC-SR04 would get closer to the solid surface that represents the dam's max level, and a 0 cm reading would mean that it's reached the max level.

# Main Page

Me and my group implemented a role control system, meaning that every role has a different main page.
<br> <br>

<img src="https://github.com/user-attachments/assets/6266360a-0858-442a-b49a-2c4d17612b01">

<p align="center"><i> Admin's main page with all the options available </i></p>
<br>

<img src="https://github.com/user-attachments/assets/20061829-954e-4c6a-a11e-369e8acf7211">
<p align="center"><i> Statistics' main page, having access to real-time data visualization </i></p>
<br>

<img src="https://github.com/user-attachments/assets/af369d18-456c-499e-9b15-94890edeaa6a">
<p align="center"><i> Operator's main page, having access to remote command execution </i></p>
<br> <br>

# How It Works

We set two reference values, if the sensor read that the water level reached the first reference value (warning value), the LED would activate, alerting that the water has reached a minor warning level, and if it reached the second reference value (emergency value), the Servo (drainage pipe) would activate.
<br> <br>

<img src="https://github.com/user-attachments/assets/40d68cb4-e609-4310-9d4f-47632a11e826">
<br> <br>

The warning and emergency values can easily be modified through the operator or admin's console, without needing to access the ESP32 manually.
<br> <br>

<img src="https://github.com/user-attachments/assets/63d75462-6f21-4723-a5fd-ae5b67ce49ad">
<br> <br>

Some of the data, like sensor readings, command executions, login/logout are always stored in memory, and can be visualized at any moment by the statistics or admin role.
<br> <br>

<img src="https://github.com/user-attachments/assets/012dc2f2-93f6-4965-909a-43edfe22b35c">
