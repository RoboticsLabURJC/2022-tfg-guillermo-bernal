---
title: "Semana 2: Hacer uso del Turtlebot2 en físico"
categories:
  - Weblog
tags:
  - ROS2 Humble
  - Gazebo
  - Turtlebot2
---

La tarea de esta semana es intentar poner a funcionar los drivers del Turtlebot2 en el robot físico. Es decir, lograr que los drivers de la cámara, láser y motor funcionen en el RViz.

El soporte de estos drivers estaba ya hecho ([repo](https://github.com/IntelligentRoboticsLabs/Robots/tree/humble/kobuki)) salvo el de la cámara, por lo tanto, ha sido sencillo poder hacer que funcionen estos drivers de láser y motor.
Se puede teleoperar el robot y ver los obstáculos a través del RPLIDAR que tiene instalado en el RViz.
Solo algunas dependencias y pasos como entrar en el grupo dialout en el sistema y archivos de configuración de los drivers que se debían tener.
