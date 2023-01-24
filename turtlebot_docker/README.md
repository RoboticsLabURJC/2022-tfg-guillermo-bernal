Para crear la imagen:
(Recordar dar permisos de ejecución antes, que a mí siempre se me olvida)

```
./build.sh
```

Y para correr el docker:
```
./run.sh
```
El script no tiene flag de --cpus all porque yo no tengo activa la aceleracion gráfica pero se puede poner sin problema

Cuando estes dentro ve al workspace del turtlebot y ejecuta para lanzar el robot simulado en Gazebo con RViz2::

```
./empty_world_robot
```

Hay otro workspace que es donde se lanza el brain, dentro de ese hay que ejecutar antes:

```
source install/setup.bash
```

Y tras eso ya se puede ejecutar el nodo

```
ros2 run brain_turtle brain
```

Y ya.




