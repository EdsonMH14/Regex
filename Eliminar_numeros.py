import re

def eliminar_horas(texto):
    # Expresión regular para encontrar patrones de "00:00"
    patron = r'\b\d{1,2}:\d{2}\b'
    # Reemplazar los patrones encontrados con una cadena vacía
    texto_limpio = re.sub(patron, '', texto)
    # Eliminar líneas vacías que puedan quedar después del reemplazo
    texto_limpio = '\n'.join([linea for linea in texto_limpio.splitlines() if linea.strip()])
    return texto_limpio

# Ejemplo de entrada
entrada = """
er recuerda en la primera parte nos
0:22
centramos en entender que era una
0:23
neurona artificial componente básico
0:25
dentro de una red neuronal vimos como
0:27
matemáticamente una neurona se definía
0:29
como una suma ponderada en sus valores
0:31
de entrada y como esto es equivalía al
0:32
modelo de regresión lineal
0:34
hablamos de nacho hits de realidad
0:35
virtual sí en serio y con esto
0:38
planteamos un ejemplo en el que
0:39
comprobamos que el uso de una neurona
0:41
podría modelar la información de una
0:43
puerta
0:43
andy y lo visualizamos e hicimos lo
0:45
mismo con una puerta ahora y con una
0:47
puerta son buenos con la puerta sur no
0:49
pudimos y es que también comprobamos que
0:51
con una sola neurona no se podía separar
0:53
linealmente a una nube de puntos
0:55
distribuidos de esta manera ese será
0:57
nuestro punto de partida en el vídeo de
0:59
hoy para solucionar el problema de la
1:01
puerta sur vimos que la solución venía
1:03
por duplicar a nuestras neuronas para
1:05
así poder tener dos separadores que de
1:06
forma combinada nos separaban
1:08
correctamente ambas clases una
1:10
demostración muy clara de cómo añadiendo
1:12
neuronas
1:12
podíamos empezar a modelar información
1:15
más compleja en el vídeo de hoy vamos a
1:17
desarrollar este concepto y veremos qué
1:19
ventajas podemos obtener de juntar cada
1:21
vez más y más neuronas es decir hoy nos
1:24
centraremos en entender la red de una
1:26
red neuronal
1:28
[Música]
1:33
empecemos a juntar neuronas si te lo
1:36
planteas hay dos formas diferentes de
1:37
organizar a estas neuronas de aquí una
1:39
manera sería colocarlas en la misma
1:41
columna o llamado de forma más correcta
1:43
en la misma capa como se puede ver dos
1:45
neuronas que se encuentran en la misma
1:47
capa recibirán la misma información de
1:49
entrada de la capa anterior y los
1:50
cálculos que realicen los pasarán a la
1:52
capa siguiente a la primera capa donde
1:55
están las variables de entrada se le
1:56
denomina capa de entrada y a la última
1:58
capa de salida a las capas intermedias
2:01
se le denominan capas ocultas vale de
2:04
momento parece sencillo pero no nos
2:06
quedemos sólo con eso como nos gusta
2:08
hacer en este canal vamos a intentar
2:09
entender de forma intuitiva qué es lo
2:11
que ocurre cuando colocamos las neuronas
2:12
de una manera u otra
2:15
como hemos dicho cuando colocamos dos
2:16
neuronas de forma secuencial una de
2:19
ellas recibe la información procesada
2:20
por la neurona anterior y qué ventajas
2:23
nos aporta esto bueno pues con esto lo
2:25
que conseguimos es algo muy importante
2:27
que la red puede aprender conocimientos
2:30
jerarquizado fíjate si recuerdas el
2:33
ejemplo de la primera parte te acordarás
2:34
que teníamos dos variables de entrada
2:36
nachos y realidad virtual y que con una
2:39
sola neurona conseguíamos modelar si
2:40
pasaríamos una noche entretenida o no es
2:43
decir nuestra neurona ha procesado la
2:45
información de entrada y el resultado de
2:46
salida nos aporta una información más
2:48
elaborada y compleja y por qué no
2:51
utilizar esta información para elaborar
2:53
algo más complejo aún a lo mejor lo que
2:55
queremos que aprenda nuestra red no es
2:57
saber si estaremos entretenidos el
2:58
viernes noche sino la nota que sacaremos
3:01
en el examen de la semana que viene a lo
3:03
mejor tenemos otras dos variables de
3:05
entrada que son motivación por la
3:07
asignatura y dificultad del examen
3:08
siendo así ésta podría ser una posible
3:11
arquitectura de nuestra red ahora de
3:13
forma jerarquizada la red neuronal
3:15
podría aprender conocimientos más
3:16
básicos las primeras capas como por
3:18
ejemplo que esta neurona se especializa
3:20
en saber si vas a estar entretenido
3:21
el viernes por la noche y esta otra
3:23
neurona que se especializa en saber cuál
3:25
es tu motivación de cara al examen el
3:27
conocimiento elaborado en esta capa será
3:29
procesado nuevamente por la siguiente
3:30
escapa elaborando cada vez conocimientos
3:33
más complejos abstracto e interesante
3:35
esta neurona de aquí podría descubrir
3:37
que si tu motivación de cara al examen
3:39
es baja y tu noche del viernes
3:40
posiblemente sea entretenida quizás vaya
3:42
a estudiar poco y desempeñar el examen
3:44
sea más bajo no entiendes cómo ves entre
3:48
más capas añadimos más complejo puede
3:50
ser el conocimiento que elaboremos esta
3:52
profundidad en la cantidad de capas es
3:53
lo que da nombre al aprendizaje profundo
3:55
el live learn in pero bueno eso que hay
4:00
un pero pero un pero muy importante para
4:03
alcanzar este aprendizaje profundo hemos
4:05
dicho que queremos conectar múltiples
4:06
neuronas de forma secuencial y si
4:09
recuerdo de la primera parte al final lo
4:10
que hace cada una de estas neuronas es
4:12
un problema de regresión lineal es decir
4:14
que lo que estamos haciendo si lo
4:16
planteamos matemáticamente es concatenar
4:18
diferentes operaciones de regresión
4:19
lineal el problema aquí es que
4:21
matemáticamente se puede comprobar que
4:23
el efecto de sumar muchas operaciones de
4:25
regresión lineal es decir sumar muchas
4:27
líneas rectas
4:28
equivale a solamente haber hecho una
4:29
única operación es decir da como
4:32
resultado otra línea recta o visto de
4:34
otra manera tal y como está planteada la
4:36
red de momento hace que toda la
4:38
estructura que queríamos conseguir
4:39
colapse hasta ser equivalente a tener
4:42
una única neurona para conseguir que
4:44
nuestra red no colapse necesitamos que
4:46
esta suma de aquí dé como resultado algo
4:48
diferente a una línea recta y para eso
4:50
necesitaríamos que cada una de estas
4:52
líneas sufra alguna manipulación no
4:54
lineal que las distorsiones como lo
4:56
conseguimos entran en escena las
4:59
funciones de activación la función de
5:02
activación es la última componente que
5:04
nos faltó ver en la estructura de la
5:05
neurona básicamente si en nuestra
5:07
neurona lo que hacíamos era calcular
5:08
cómo valor de salida una suma ponderada
5:10
de nuestras entradas lo que queremos
5:12
hacer ahora es pasar dicho valor de
5:14
salida por nuestra función de activación
5:16
lo que hará la función de activación
5:18
será distorsionar nuestro valor de
5:20
salida añadiéndole deformaciones no
5:22
lineales para que así podamos encadenar
5:24
de forma efectiva la computación de
5:26
varias neuronas y como son estas
5:28
deformaciones bueno pues depende de la
5:30
función de activación vamos a ver
5:32
algunas de ellas realmente ya en el
5:34
vídeo anterior habíamos visto una
5:36
primera función de activación cuando
5:38
decíamos que una vez hubiéramos obtenido
5:39
el resultado de la suma asignaremos 01
5:42
en función de si el valor era mayor o
5:43
menor que el umbral
5:44
lo que estamos haciendo era transformar
5:46
el valor de salida es decir estamos
5:48
pasando a nuestro resultado por una
5:50
función de activación más concretamente
5:52
esta función es la función escalonada
5:54
esta de aquí como veis lo que nos cuenta
5:57
esta función es que para un valor de
5:58
entrada mayor al umbral el output es 1 y
6:01
si es inferior es igual a 0
6:04
se llama escalonada porque el cambio de
6:05
valor se produce instantáneamente y no
6:07
de forma gradual produciendo así un
6:10
escalón algo que como veremos en el
6:11
próximo vídeo no favorece el aprendizaje
6:13
por tanto esta función de activación no
6:15
nos interesa sin embargo esta función de
6:18
aquí es más interesante esta es la
6:20
función sigmoide y como vemos la
6:22
distorsión que produce hace que los
6:23
valores muy grandes se saturan en uno y
6:25
los valores muy pequeños se saturan en
6:27
cero por tanto con esta función
6:29
sigmoides no sólo conseguimos añadir la
6:30
deformación que estamos buscando sino
6:32
que también nos sirve para representar
6:34
probabilidades que siempre vienen en el
6:36
rango de 0 a 1 similar a esta tenemos
6:38
también la función tangente hiperbólica
6:40
cuya forma similar a la sigmoides pero
6:42
cuyo rango varía de menos uno a uno y
6:45
finalmente otro tipo de función de
6:46
activación muy utilizada es la unidad
6:48
rectificada lineal relu para los colegas
6:51
que básicamente se comporta como una
6:53
función lineal cuando es positiva y
6:55
constante a cero cuando el valor de
6:57
entrada es negativo cada una de estas
6:58
funciones además de aportar la no
7:00
linealidad que estamos buscando también
7:02
ofrecen diferentes beneficios
7:04
dependiendo de cuando las utilicemos
7:05
temario que queda para otro vídeo aparte
7:08
al añadir estas deformaciones no
7:10
lineales damos por solucionado el
7:12
problema de poder encadenar varias
7:13
neuronas como no quiero que me creas
7:15
sino que realmente lo entiendas vamos a
7:17
ver un ejemplo bueno mira realmente ya
7:20
llevo hablando un rato así que mejor lo
7:21
buscas en internet y yo creo que me va a
7:24
echar un rato al sofá a ver qué tiene la
7:26
tele
7:32
dios
7:34
[Música]
7:42
y sigues aquí bueno quizás estés
7:46
comiendo algún spoiler del juego de
7:47
tronos estamos en el punto de este de la
7:49
batalla con nieve en la que están
7:51
rodeados
7:53
pero bueno luego todo al final sale bien
7:54
y se largan volando en águilas para
7:56
destruir al anillo y bueno yo que sé no
7:58
soy dai o script vale pero madre mía que
8:02
batalla es decir están completamente
8:04
rodeados todos estos de aquí son los
8:06
malos y estos de aquí son los buenos
8:08
usos vaya movida por cierto ahora que me
8:11
fijo y si quisiéramos salvarlos usando
8:14
una red neuronal que no me mires así no
8:17
te olvides que esto no deja de ser un
8:18
canal sobre inteligencia artificial mira
8:20
vamos a aplicar toda la teoría que hemos
8:22
visto en el vídeo para intentar separar
8:23
estas dos nubes de puntos quizás este
8:26
ejemplo te parezca muy tonto pero en la
8:27
realidad este mismo problema podría ser
8:29
el de clasificar en una imagen que
8:31
células son cancerígenas y cuáles no
8:33
como lo hacemos para que lo puedas ver
8:36
claro voy a intentar enseñarte a la
8:37
interpretación geométrica de lo que
8:39
ocurre en una red neuronal esto ya lo
8:41
empezamos a ver en el vídeo anterior
8:42
recuerdas esta gráfica de aquí aquí
8:44
podríamos ver el resultado del
8:45
procesamiento de una neurona operando en
8:47
una tarea de clasificación
8:49
pero antes te he dicho que aquí ya
8:50
estábamos haciendo uso de una función de
8:51
activación escalonada cuya forma es esta
8:53
de aquí y como podríamos ver
8:55
geométricamente el efecto de esta
8:57
función de activación en nuestra gráfica
8:59
donde se esconden pues fíjate bien aquí
9:03
está efectivamente el efecto de la
9:06
función de activación es el de
9:07
distorsionar el plano generado por la
9:09
neurona toda la geometría de este plano
9:11
distorsionado que sea superior a este
9:13
plano de aquí pertenecer a un grupo en
9:15
este caso en verde y lo que quede debajo
9:17
pertenecer al otro grupo en rojo y como
9:21
sería esta misma figura si hubiéramos
9:22
utilizado las otras funciones pues aquí
9:24
lo puedes ver cómo ves podemos encontrar
9:26
en la silueta del plano la forma
9:28
original de nuestras funciones de
9:29
activación
9:32
aún así fíjate que de momento en los
9:34
tres casos nuestra frontera no deja de
9:35
ser una línea recta
9:37
debido a la intersección de la figura
9:38
geométrica con el plano entonces si sólo
9:41
conseguimos una línea recta como podemos
9:43
encontrar una frontera curva que pueda
9:44
solucionar este problema esto lo vamos a
9:46
solucionar
9:47
aprovechando que gracias a las funciones
9:48
de activación ahora ya podemos encadenar
9:50
varias neuronas al mismo tiempo
9:53
una posible solución al problema sería
9:55
la siguiente vamos a colocar en la
9:57
primera capa oculta de nuestra red una
9:59
neurona con una función sigmoide como ya
10:02
es capaz de reconocer la función
10:03
sigmoide tiene esta forma de aquí y en
10:05
realidad su forma la podemos ir variando
10:07
según ajustamos los parámetros de
10:08
nuestra red podemos ver que cambiando
10:10
los parámetros podemos conseguir incluso
10:12
cambiar la orientación de la figura y
10:14
esto nos puede servir en vez de una sola
10:17
neurona vamos a colocar cuatro y cada
10:19
una de ellas con una orientación
10:20
diferente
10:22
si te fijas con una nueva neurona
10:24
podemos construir la combinación de
10:26
estas cuatro figuras geométricas de aquí
10:27
obteniendo como resultado una superficie
10:29
plana con un bulto en medio esta figura
10:32
es la solución a nuestro problema porque
10:35
como se puede ver la intersección del
10:37
plano con esta montaña produce la
10:39
frontera circular que estábamos buscando
10:41
nuestro problema de clasificación está
10:43
resuelto y jon nieve y sus amigos están
10:45
salvados con este ejemplo espero haberte
10:47
convencido de que las redes neuronales
10:49
son capaces de desarrollar soluciones
10:50
muy complejas gracias a la unión de
10:52
muchas y muchas neuronas si tras ver
10:54
este vídeo la única duda con la que te
10:56
quedas es porque sigo empeñado en decir
10:57
yo nieves en vez de iones nou entonces
11:00
significa que ya estás preparado para lo
11:01
que nos falta por ver en la tercera
11:03
parte de esta serie porque claro todo
11:05
esto que hemos visto que pueda hacer la
11:06
red neuronal lo tiene que aprender a
11:08
hacer ella por sí sola quieres saber
11:10
cómo te lo cuento en el próximo vídeo
"""

# Procesar la entrada
salida = eliminar_horas(entrada)

# Mostrar la salida
print(salida)