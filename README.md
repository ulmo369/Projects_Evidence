# Projects_Evidence
# Diego Emilio Barrera Hernández

 **What does this repository have?:**
- My biggest project

 **Descripción:**
 
 El programa nos muestra una simulación de un juego de pelea, dónde tu eres el que interactúa para que la batalla siga avanzando.
 Serás un héroe de cualquier juego y vencerás al Jefe Final de ese juego.
 Solo tienes un Tilt Attack y un Smash Attack,
 el Tilt Attack puede fallar o puede ser un ataque crítico; pero solo es un 30% de tener eso,
 el Smash Attack se cargará cada tres turnos; el jefe tiene un 30% de pegar y el heroe un 70%,
 y por ultimo el Smash Attack del jefe vale 100 y el Smash Attack del héroe tu lo puedes escoger, tal vez de 50 o tal vez de 25.
 Cuando tú y tu oponente alcancen el %300 de su daño el juego terminará.
 El ganador será el jugador que tenga menos porcentaje de daño al final de la partida.

# Funcionalidad
 Solo se permite un heroe y su enemigo, lo cual puede haber únicamente dos casos:
 
 TLOZELDA con su enemigo GANONDORF o FINALFANTASY con su enemigo SEPHIROTH
 
 Las clases estan hechas para mostrar su información y poder hacer las acciones de los ataques que suben el daño
 
 Consta de un menu con las opciones para que siga corriendo la batalla y corre sobre consola.

# Tipos de practica en programación orientada a objetos
* **Clase abstracta y Herencia (papá):**  
    * CHARACTER.h

* **Herencia(hijas) y Sobrescritura de un metodo "ShowInfoGame":**  
    * TLOZELDA.H
    * FINALFANTASY.H
    * GANONDORF.H
    * SEPHIROTH.H
    
* **Polimorfismo, Composición y Apuntadores:**  
    * GAME.h

* **UML:**  
    * POO2_CORRECCION.pdf
    
# Consideraciones

 El programa solo corre en la consola y esta hecho con c++ en Windows 10
 
 Compilar con: "g++ GAME.h CHARACTER.h TLOZELDA.h GANONDORF.h FINALFANTASY.h SEPHIROTH.h MAIN.cpp"

 windows: "MAIN.exe"

 linux: "/a.out"
