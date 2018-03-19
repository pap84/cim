Sistemas de detección de uso radiológico
========================================

El *Capítulo* presenta descripciones breves
respecto de los principios de funcionamiento y detalles técnicos de los
sistemas de detección de radiación más comúnmente empleados en el ámbito
de radiodiagnóstico.

En líneas generales, los detectores de radiación presentan similitudes
en cuanto a su comportamiento.

Los efectos de interacción entre la radiación y la materia son la base
que determina de modo unívoco las propiedades de los sistemas de
detección. En particular, el tipo de material del detector depende
propiamente de la clase de radiación así como de la información que es
necesario recavar.

La operatividad de los sistemas de detección deben contar con las
siguientes etapas:

-  Ingreso de la radiación al sistema de detección.

-  Interacción de la radiación con el “material sensible” que constituye
   el sistema de detección.

-  Efectos por interacción de la radiación con el material sensible:
   pérdida de toda o parte de su energía cinética por medio de
   transferencias a los electrones de los átomos del material sensible.

-  Producción de corrientes de electrones (de energías relativamente
   bajas).

-  Recolección de la corriente de electrones.

-  Anáslisis mediante circuito electrónico.

-  Procesamiento con dispositivos digitales (opcional).

En términos del tipo de radiación a detectar, puede mencionarse,
esquemáticamente:

Determinación del tipo de partícula
    Identificar el tipo de partícula (que resulta crítico en el caso de
    un campo mixto, como ocurre en procesos nucleares) es necesario
    utilizar materiales sensibles en los que ya sea la carga o la masa
    de cada tipo de partícula pueda generar efectos distintivos.

Tiempo de emisión de radiación
    Medir el tiempo en el que la radiación fue emitida rquiere de
    materiales sensibles en los que sea posible una rápida recolección
    de los pulsos de corriente de electrones producidas por las
    interacciones.

Energía de la radiación
    Determinar la energía de la radiación implica utilizar detectores en
    los que la amplitud de los pulso detectados resulte proporcional a
    la energía de la radiación que provocó el pulso. El material
    sensible debe ser de alto número de electrones disponibles de modo
    que se minimicen pérdidas y fluctuaciones.

Polarización de la radiación
    La medición del spin o la polarización requiere de detector capaces
    de separar los diferentes estados de polarización de la radiación.
    En general, no alcanza solo con materiales sensibles, sino que debe
    acudirse al diseño de arreglos específicos para detección.

Tasa de conteo de flujo
    Para determinaciones de alta tasa de conteo, es necesario emplear
    detectores de rápida recuperación capaces de reiniciar el conteo de
    eventos sucesivos. Contrariamente, para mediciones de tasas de
    conteo muy bajas, lo más importante es la minimización del ruido de
    fondo.


Procesos para la detección de radiación electromagnética
--------------------------------------------------------

Los fotones (restringiendo al campo de aplicación en radiodiagnóstico,
refiere a rayos X y :math:`\gamma`) interactuan con la materia por medio
de diferentes tipos de procesos: *scattering* Compton, creación de pares
y absorción fotoeléctrica.

A continuación se incluye una descripción brevísima estos procesos:

**Scattering Compton**

El *scattering* Compton es el proceso por el cual un fotón incidente
cambia el estado de fase, modificando potencialmente dirección de
movimiento :math:`\vec{\Omega}` y energía cinética :math:`E` por
interacciones con electrones de los orbitales atómicos, los que
inicialmente pueden considerarse prácticamente libres [1]_ adquieren
casi toda la energía cinética liberada por el fotón incidente. En este
sentido, aproximando por electrón en reposo y libre se aplica la
conservación de momento y energía para describir los cambios de fase.

**Producción de pares**

Este proceso refiere a la interacción de un fotón incidente energético
con la materia de modo de producir pares electrón-positrón como
consecuencia de acoplamiento con el campo atómico. La energía cinética
es cedida para el equivalente en masa de par partícula-antipartícula, y
eventual sobrante es transferido como energía coinética a las partículas
creadas.

Por lo tanto, existe un valor umbral para la energía por encima del cual
es posible el efecto:
:math:`E_{umbral} = 2 \, m_{e} c^{2} = 1.022 \, MeV`.

**Absorción fotoeléctrica**

El fotón incidente es absorbido por parte del átomo de modo que uno de
los electrones atómicos, denominado fotoelectrón es liberado a expensas
de la energía cinética adquirida. Los electrones libres no pueden
absorber fotones para cumplir simultáneamente con la conservación de la
energía y el momento, motivo por el cual no se produce este efecto para
electrones libres. La energía cinética del electrón de ionización
(liberado) equivale a la energía del fotón incidente menos la energía de
ligadura del electrón eyectado.

La determinación de la probabilidad de absorción de un fotón por efecto
fotoeléctrico muestra algunas características específicas, como que es
mayor para para energías bajas [2]_, aumenta significativamente según el
número atómico :math:`Z` y disminuye según aumente la energía del fotón
incidente :math:`E`.

A partir de los procesos mencionados, se propone una cantidad para
intengrar los efectos netos denominada coeficiente de atenuación másico,
el cual se describe del siguiente modo: Se considera un haz
perfectamente colimado de fotones de energía :math:`E` producidos por
una fuente :math:`S` e incidiendo sobre un material de número atómico
:math:`Z` y espesor :math:`d` (a lo largo del *path*). Por lo tanto, en
los procesos de interacción, los fotones del haz incidente pueden sufrir
absorción fotoeléctrica, *scattering* Compton o producción de pares. De
modo que, solo parte de los fotones incidentes alcanzarán el detector
ubicado detrás [3]_ del blanco irradiado. En particular, alcanzarán el
detector los fotones que no hayan interactuado.

La probabilidad total por unidad de longitud :math:`d s` de que un fotón
incidente no alcance al detector, se denomina coeficiente de atenuación
lineal total y representa la integración de todas las probabilidades
correspondientes a cada uno de los posibles procesos de interacción
involucrados.


Procesos para la detección de neutrones
---------------------------------------

La detección de neutrones presenta algunas características similares al
caso de los fotones, debido a la propiedad de no poseer carga. Sin
embargo, por su naturaleza intrínseca, los procesos involucrados son
radicalmente diferentes.

Los neutrones no interactuan eléctricamente con los átomos, pero sí
presentan interacciones fuerte con los núcleos por medio de una amplia
variedad de procesos, entre ellos:

-  Colisiones elásticas, que son relevantes para energías
   :math:`\approx 1 MeV`, denominados neutrones rápidos.

-  Colisiones inelásticas que son relevantes para valores de energía
   superiores al umbral de excitación nuclear.

-  Captura de neutrones, proceso por el cual el núcleo captura neutrones
   incidentes constituyendo un nuevo núcleo, que eventualmente puede
   sufrir transiciones para desexcitarse. Este efecto varía según la
   velocidad de los neutrones, aproximadamente inversamente proporcional
   a ésta.

-  Otras reacciones nucleares de tipo :math:`(n,p)`, :math:`(n,d)`, etc
   que representan captura de un neutrón y emisión de partículas
   cargadas.  Este proceso ocurre en el rango de algunos eV a keV.

-  Fisión: A energías “térmicas” (del orden del eV), los neutrones se
   denominan neutrones térmicos o lentos. Este proceso da lugar a la
   fragmentación nuclear.

-  Producción de una *hadronic shower*, efecto que ocurre en el rango de
   energías por arriba de unos cientos de keV, provocando la emisión de
   partículas cargadas.

Los mecanismos de interacción de los neutrones hacen que su detección
resulte particularmente compleja.

Sin embargo, existen algunas técnicas y sistemas de detección capaces de
brindar información a cerca del campo de neutrones. Aunque, el mayor
desafío refiere a las dificultades asociadas a determinaciones en campo
mixto.


Procesos para la detección de electrones
----------------------------------------

Los electrones y los positrones interactuan por medio de *scattering*
con los electrones orbitales atómicos con las siguientes
características:

-  Algunos electrones, particularmente los emitidos en las
   desintegraciones :math:`\beta`, viajan con velocidades relativistas.

-  Los electrones sufrirán cambios significativos en la dirección de
   movimiento como consecuencia de las colisiones con otros electrones.
   Por tanto, describen trayectorias erráticas (*track*).

-  En colisiones frontales con electrones atómicos se transfiere una
   fracción muy importante de la energía cinética inicial que es
   adquirida por el electrón impactado. Además, debe destacarse que en
   estos casos, resulta indistinguible el electrón incidente del
   eyectado.

-  Debido a cambios abruptos en dirección de movimiento y módulo de la
   velocidad (energía cinética), el electrón sufre grandes
   aceleraciones. Como consecuencia, se emite radiación electromagnética
   conocida como *Bremsstrahlung*.


Procesos para la detección de partículas cargadas pesadas
---------------------------------------------------------

Debido a que los núcleos del material del detector ocupan solamente en
torno a 10-15 del volumen de sus átomos, resulta unos tres órdenes más
probable para una partícula el colisionar con un electrón que con un
núcleo. Por tanto, el mecanismo de pérdida de energía dominante para las
partículas cargadas es el *scattering* Coulombiano por los electrones
atómicos del material sensible que compone el detector.

Si bien el *scattering* Coulombiano de partículas cargadas por los
núcleos, denominado *scattering* Rutherford, es un proceso importante en
física nuclear, tiene poca influencia en la pérdida de energía de las
partículas cargadas a lo largo de su trayectoria dentro del detector.

Se aplican los principios de conservación de la energía y momento en
colisiones frontal elásticas entre partículas pesadas incidentes de masa
:math:`M` y electrones de masa :math:`m_{e}`, supuestos en reposo, para
determinar así las probabilidades de los efectos de interacción que dan
lugar a las secciones eficaces.

La gran cantidad de eventos de colisión entre partícula cargada masiva y
electrones del medio material oriogina, entre otras consecuencias:

-  Una gran cantidad de colisiones antes de que la partícula ceda toda
   su energía cinética. Colisiones frontales generan la máxima
   transferencia posible de energía. En el resto de las colisiones, la
   transferencia en general será mucho menor.

-  En colisiones entre una partícula cargada pesada y un electrón, la
   partícula cargada pesada es desviada un ángulo despreciable, por lo
   que ésta sigue una trayectoria prácticamente rectilínea.

-  Dado que la fuerza Coulombiana es de alcance infinito, la partícula
   cargada masiva interactua de modo simultaneo con muchos electrones a
   la vez, de modo que pierde energía continua y gradualmente durante la
   trayectoria. Habiendo recorrido cierta distancia, denominada rango,
   perderá toda la energía cinética.


Detectores gaseosos
-------------------

Existen diferentes tipos de sistemas de detcción gaseosos. Esta
denominación proviene del hecho de que el material sensible utilizado
para la detección es un gas.


Cámaras de ionización
~~~~~~~~~~~~~~~~~~~~~

Los detectores basados en ionización están formados esencialmente por un
recinto donde se encuentra un gas a presión controlada, allí se colocan
dos electrodos separados una cierta distancia, a los que se aplica una
tensión de polarización.

El gas dentro del recinto no es conductor eléctrico en condiciones
normales, por lo tanto no circula corriente eléctrica entre los
electrodos. Cuando una partícula del haz ionizante interactúa con el gas
pueden generarse efectos de ionización produciendo pares ión-electrón.
El campo eléctrico someterá a las cargas liberadas de modo que se muevan
hacia el electrodo de signo contrario; los electrones hacia el ánodo y
los iones hacia el cátodo.

La colección de estas cargas se logra utilizado un dispositivo eléctrico
asociado al detector, sea midiendo la corriente media que se generada en
el detector debido a la interacción de varias partículas (cámaras que
operan en modo corriente) o bien formando un pulso con cada golpe de
carga que recogen los electrodos (cámaras que operan en modo impulso).

Para aplicaciones dosimétricas, la cámara de ionización es un dosímetro
denominado *standard primario*, ya que además de ser el sistemas más
difundido y utilizado universalmente con buena *performance*, sus
propiedades permiten obtener mediciones confiables y estables en base a
un sistema relativamente simple lo que, sumado a teorías sólidas
respecto de sus principios de funcionamiento, representa una importante
ventaja en términos de estabilidad y confiabi- lidad. En este sentido,
visto que el funcionamiento del sitema dosimétrico está sustentado por
teoría de cavidad, como Bragg-Gray, resulta que una de las principales
características es el volumen sensible requiere ser determinado de
manera particularmente precisa.

En términos de su uso práctico, la cámara de ionización se utiliza
colocándola expuesta al haz de radiación o bien introducida en un medio
material, fantoma, para determinar exposición en aire o bien dosis
absorbida en el medio material, típicamente agua o medios similares en
cuanto a las propiedades de absorción/dispersión de radiación ionizante
en los rangos de interés. Este tipo de medios materiales se denomina
“tejido-equivalentes”. Por tanto, resulta importante también conocer las
propiedades del medio material gaseoso en el que se producen los
procesos que permiten determinar la dosis absorbida en la cavidad
gaseosa.

Existen distintos tipos de cámaras de ionización. Las más utilizadas son
la cámara tipo dedal, comúnmente denominada cámara de tipo *Farmer* y,
aunque en menor medida, también la cámara de ionización de tipo
plano-paralela.

De hecho, las cámaras de ionización pueden clasificarse, según su
diseño, o más específicamente según la forma de los electrodos: existen
configuraciones planas o cilíndri- cas, según la disposición de los
electrodos, que pueden ser planos-paralelos (cámara plano-paralela
usualmente denominada Markus), o bien cilíndricos, constituídos por un
electrodo hueco de forma de cilíndrica y otro interior en forma de
alambre o varilla en dispuesto coaxialmente (cámara de tipo dedal
usualmente llamada Farmer).

El volumen sensible de las cámaras de ionización se rellenan típicamente
con una variedad de gases que puede ser aire a presión atmosférica o
bien gases nobles, especialmente argón.

El rendimiento de detección, definido como la fracción de de radiación
detectada res- pecto del total que atraviesa el volumen sensible del
detector, es muy próxima al 100% para la cámara de ionización para el
caso de la detección de partículas :math:`\alpha` (núcleos de helio) y
:math:`\beta` (electrones y positorones), mientras que para fotones el
rendimiento ronda solo el 1%, debido a las propiedades intrínsecas de
los mecanismos de interacción de cada tipo de radiación.

La cámara de ionización forma parte de una categoría de detectores
denominados gaseosos normalmente llamados también “detectores de
ionización”, debido a que este tipo de dispositivos responden a la
radiación por medio de corrientes inducidas por ionización.

Además de la cámara de ionización, cabe destacar otros dos tipos de
detectores gaseosos, hisórica y aún frecuentemente utilizados.


Contador proporcional
~~~~~~~~~~~~~~~~~~~~~

En el caso de la cámara de ionización, el voltage aplicado resulta ser
aquel suficiente para colectar solo las cargas liberadas por acción
directa de la raiación incidente. Sin embargo, si se aumenta aún más el
voltaje aplicado, los iones atraidos ganan tanta energía que podrían
generar ionizaciones adicionales durante el recorrido hacia los
electrodos, y los electrones producidos por estas ionizaciones pueden, a
su vez, generar otros, constituyendo un efecto en cascada, lo que se
conoce como *efecto de amplificación de la carga por el gas*. El factor
por el cual la ionización original es “multiplicada” se denomina *factor
de amplificación del gas*. El valor de esta factor aumenta rápidamente
al aumentar el voltage aplicado y puede llegar a valores cercanos a
:math:`10^{6}`. Los detectores que operan en este regimen se conocen
como contadores proporcionales, y la carga neta puede obtenerse de
:math:`Q=W*f`, donde :math:`f` es el factor de amplificación del gas.
Por lo tanto la carga total producida resulta proporcional a la energía
depositada por la radiación ionizante incidente. En general, los
contadores proporcionales utilizan gases que permiten la migración los
iones producidos con muy alta eficiencia, como los gases nobles, entre
lo cuales Ar y Xe son los mas comúnmente empleados.


Contador Geiger-Müller
~~~~~~~~~~~~~~~~~~~~~~

Los detectores Geiger-Müller son detectores gaeosos diseñados para
obtener la máxima amplificación posible.

El ánodo central es mantenido a muy alto potencial en relación al
cilindro exterior (cátodo). Al producirse ionizaciones dentro de la
cavidad de gas por interacción de la radiación incidente, los electrones
son acelerados hacia el ánodo central y los iones positivos al cátodo
exterior. En este proceso ocurre la amplificación del gas. Pero, debido
a que el voltaje aplicado es tan alto, los electrones colectados pueden
causar excitaciones de las moléculas del gas. Estas moléculas se
desexcitan rápidamente (:math:`\approx 10^{-9}`\ s) emitiendo fotones
visibles o UV. Si alguno de estos fotones UV interactúa con en el gas o
en el cátodo, puede ocurrir fotoabsorción, lo cual genera otro electrón
para contribuir en el efecto cascada.

En el caso de los dispositivos de Geiger Müller se presenta el problema
de que durante la trayectoria de los iones, éstos pueden ser acelerados
y alcanzar el ánodo con la suficiente energía para liberar electrones y
empezar el proceso de nuevo. Esto se debe a la naturaleza del proceso de
avalancha múltiple en el tubo Geiger, basta con un electrón para crear
un pulso de salida. Para evitar este efecto, se acostumbra a agregar un
segundo gas denominado *quenching gas*, o gas de extinción, compuesto
por moléculas orgánicas complejas [4]_. Se utiliza concentraciones
típicas de 90% de gas primario y 10% de gas de extinción.


Detectores de estado líquido y sólido
-------------------------------------

Estudiados los detectores gaseosos, resulta que presentan algunas
desventajas, principalmente asociadas a baja eficiencia para muchos
tipos de radiaciones, por ejemplo rayos :math:`\gamma` de 1 MeV, ya que
en aire recorre unos 100 m.

Los detectores de estado sólido, que presentan densidades mucho mayores,
cuentan con la probabilidad de absorción en dimensiones razonables de
tamaño de detección.

La principal característica de los detectores de estado sólido es el uso
de matriales sólidos para el sensor, es decir material sensible. Desde
un punto de vista general, la utilización de materiales sensibles de
mayor densidad, prové *a priori* mayor eficiencia en la detección en
cuanto mayor resulta la cantidad de eventos de interacción,
relativamente al caso de materiales gaseosos. Sin embargo, debido a los
requerimientos específicos para producir efectos secundarios mensurables
capacer de ser directa y unívocamente correlacionados con la energía
absotbida por el material, resulta que solo algunos pocos materiales de
estado sólido son útiles como material sensible.

Para crear un detector de estado sólido debe estudiarse el compromiso
entre:

#. El material debe ser capaz de soportar un campo eléctrico grande, de
   manera que los electrones y los iones puedan ser recogidos para
   formar un pulso electrónico. Además en ausencia de radiación el flujo
   de corriente debe ser mínimo o nulo para que el ruido de fondo sea
   bajo.

#. Los electrones deben ser fácilmente extraídos de los átomos del
   material sensible y en gran número. Electrones e iones deben ser
   capaces de viajar fácilmente en el material.

La primera condición parece exigir un material aislante, mientras que la
segunda sugiere usar un conductor. El compromiso, en definitiva, es un
semiconductor. Materiales semiconductores de tamaño suficientemente
grande para construir detectores de radiación (de algunas decenas de
:math:`cm^{3}`) recién estuvieron disponibles a partir de la década de
1960.


Detectores centelladores
~~~~~~~~~~~~~~~~~~~~~~~~

Durante la década de 1950, debido a la imposibilidad de disponer de
materiales semiconductores de dimensiones apropiadas para detección de
radiación, se desarrollaron los detectores basados en materiales
centellantes para aplicaciones en dispositivos de espectroscopía nuclear
logrando razonable alta eficiencia resolución.

**Detectores semiconductores**

Los detectores semiconductores son, escencialmente, análogos a los
detectores gaseosos. Sin embargo, los materiales sólidos de los
semiconductores ofrecen importantes ventajas comparativas, ya que
cuentan con densidad muy superior a la de los gases [5]_. Por lo tanto,
presenta valores mucho mas altos para el *stopping power*, resultando
materiales mucho mas eficientes para la detección de radiación.

Los semiconductores son, en general, pobres conductores de corriente
eléctrica, sin embargo cuando están ionizados por acción de la radiación
incidente, por ejemplo, la carga eléctrica producida puede colectarse
por medio de la aplicación de un voltaje externo. Los materiales más
comunes para construir detectores semiconductores son silicio y
germanio, aunque más recientemente se está estableciendo también el
teluro de cadmio. Para estos materiales, una ionización ocurre cada 3 a
5 eV de energía absorbida de la radiación incidente, aproximadamente, lo
cual constituye otra importante ventaja comparativa respecto de los
detectores gaseosos. Además, la amplitd de la señal eléctrica detectada
está relacionado proporcionalmente con la energía absorbida, y por ello
pueden ser utilizados para discriminar en energía.

Algunas desventajas o inconvenientes de estos dispositivos son: generan
corrientes no despreciables a temperatura ambiente, lo cual genera un
ruido tipo *background* en la señal medida, y por tanto deben ser
operados a bajas temperaturas. Otro inconveniente es la presencia de
impurezas en la matriz del material, lo cual arruina la configuración
cristalina pura. Estas impurezas crean “trampas” electrónicas que pueden
atrapar electrones generados en ionizaciones, evitando que sean
colectados por los electrodos. Este efecto puede resultar en una
apreciable disminución en la señal eléctrica medida y limita el espesor
práctico del material sensible a tamaños no mayores a 1cm,
aproximadamente. Y, debido al bajo número atómico de Si y Ge, este hecho
limita la posibilidad de emplearlos para detectar fotones, o incluso
partículas cargadas, de alta energía.

El paso de la radiación ionizante a través de los materiales genera
ionizaciones y/o excitaciones. En el caso particular en que las especies
producidas, o residuos, (ionizadas o excitadas) sufran procesos de
recombinación, se obtiene como resultado la liberación de energía. En
general, la mayor parte de esta energía es disipada en el medio como
energía térmica, por medio de vibraciones moleculares, en el caso de
gases y líquidos, o vibraciones de red en el caso de sólidos
cristalinos. Sin embargo, existen materiales en los que parte de esta
energía es transferida a emisión de luz visible. Estos materiales
particulares se denominan centelladores y los detectores de radiación
que los utilizan son llamados detectores centelladores.

Los materiales mas comúnmente utilizados para detectores de aplicación
en medicina son de tipo orgánico (substancias orgánicas diluidas en
solución líquida) o inorgánicos (substancias inorgánicas en forma de
sólido cristalino). Si bien los mecanismos precisos de centelleo son
diferentes para estos dos tipos de materiales, comparten características
comunes. La cantidad de luz producida como consecuencia de la
interacción con un único rayo incidente (RX, :math:`\gamma`,
:math:`\beta`, etc.) resulta proporcional a la energía depositada por la
partícula incidente en el material centellador. La cantidad de luz neta
producida es pequeña, típicamente unos pocos cientos (a lo sumo miles)
de fotones por cada interacción de partícula incidiendo con energía de
entre 70 y 511 keV.

Originalmente, se utilizaban cuartos oscuros para observar la luz
emitida por este tipo de materiales [6]_ y contabilizar así la
producción de ionizaciones. Esta metodología presenta insalvables
limitaciones y fue posteriormente reemplazada por tecnologías de
dispositivos electrónicos ultrasensibles a la luz, como los
fotomultiplicadores.

Los detectores por centelleo, generalmente requieren de dispositivos
extra para mejorar la eficiencia de lectura. Comúnmente se utilizan
técnicas electrónicas basadas en arreglo de tubos fotomultiplicadores.
Básicamente, un tubo fotomultiplicador es un dispositivo electrónico, en
forma de tubo, que produce un pulso de corriente eléctrica al ser
estimulado por señales muy débiles, como el centelleo producido por RX,
:math:`\gamma` o :math:`\beta`, etc. en un detector centellador.

Se coloca una película de material fotoemisor en la ventana de vidrio de
entrada, esta sunstancia [7]_ ejecta electrones cuando son alcanzados
por fotones visibles. La superficie de fotoemisión se denomina
fotocátodo, y los electrones ejectados sono fotoelectrones.

La eficiencia de conversión de luz visible en electrones liberados se
denomina eficiencia cuántica, y es típicamente de entre 1 a 3
fotoelectrones por cada 10 fotones visibles que interactúan con el
fotocátodo. Claramente, la eficiencia cuántica dependende de la energía
de la luz incidente.

Los dínodos son mantenidos a diferentes valores de potencial (creciente)
para atraer a los electrones producidos, y los secundarios que éstos
generan, de modo de producir el efecto de multiplicación. Este proceso
se repite usualmente unas 10 veces antes de que la corriente de
electrones resultante sea colectada por el ánodo. Los factores de
multiplicación que se obtienen son significativos por dínodo, resultando
en un factor global típico de :math:`10^{7}`, aproximadamente. Los tubos
fotomultiplicadores se sellan herméticamente y se mantienen en vacío; y
se construyen en diferentes formas y tamaño.

Existen también detectores de centelleo denominados “centelladores
inorgánicos”, ya que consisten en sólidos cristalinos que centellean
debido a características específicas de la estructura cristalina. Por
ello, átomos o moléculas individuales de estas substancias no
centellean, se requiere el arreglo cristalino.

Algunos cristales inorgánicos, como el NaI a temperaturas de N líquido,
son centella- dores en su estado puro, aunque la mayoría son “activados
con impurezas”, y por ello los átomos de impurezas [8]_ en la matriz
cristalina, responsables del centelleo, se denominan ‘’centros de
activación’’.

A diferencia del caso de materiales inorgánicos, los detectores basados
en materia les centelladores orgánicos, producen el efecto de centelleo
debido a propiedad inherente de la molécula de la substancia. El
centelleo es un mecanismo de excitación molecular/desexcitación al
interactuar con la radiación. Este tipo de substancias producen
centelleo en estado gaseoso, líquido o sólido, aunque se utilizan
normalmente líquidos [9]_. En los centelladores orgánicos líquidos se
disuelve el material centellador en un solvente dentro de un contenedor
típicamente de vidrio o plástico y se agrega también la substancia
radioactiva a esta mezcla. Se coloca el contenedor entre un par de tubos
fotomultiplicadores y de este modo se detecta la luz emitida que guarda
correlación con la energía impartida por el material radioactivo.

Las soluciones de centelladores orgánicos líquidos consisten de 4
componentes:

#. Solvente orgánico, que compone la mayor parte de la solución. Debe
   disolver el material centellador y también la muestra radioactiva.

#. Soluto primario, que absorbe energía del solvente y emite luz.
   Algunos materiales centelladores típicamente utilizados son
   difenil-oxazol y metilestireno-benceno.

#. A veces las emisión del soluto primario no es la mas adecuada para
   ser detectada por los fototubos, y entonces se utiliza un soluto
   secundario, cuya función es absorber la emisión del soluto primario y
   re-emitir fotones, de mayor longitud de onda que los del soluto
   primario, beneficiando la detectabilidad de la luz por parte de los
   fototubos.

#. Frecuentemente se incorporan aditivos a la mezcla para mejorar
   ciertas propiedades como la eficiencia de tradferencia de energía.

El caso particular del detector de NaI(Tl), frecuentemente diseñado en
forma de campana está formado por el cristal de NaI(Tl) ahuecado en un
extremo para la inserción de la muestra.

La transferencia de luz entre el cristal de NaI(Tl) y el
fotomultiplicador resulta ser muy eficiente, aunque existen algunas
pérdidas debido dispersión dentro del detector.

La eficiencia de detección :math:`D` de un contador de NaI(Tl) en forma
de campana para un amplio rango de energías, principalmente debido a que
la disposición geométrica adoptada implica un eficiencia geométric
:math:`g` muy buena. Entonces, la combinación con una alta eficiencia de
detección y un bajo nivel de *background* en el conteo, generan un
detector muy eficiente, que puede utilizarse para muestras conteniendo
cantidades chicas (Bq-kBq) de actividad de emisores :math:`\gamma`. La
eficiencia geométrica :math:`g` para muestra de alrededor de 1ml es del
93%, aproximadamente.


Films radiográficos
~~~~~~~~~~~~~~~~~~~

Los films, originalmente radiográficos, en términos dosimétricos de
pobre capacidad, actualmente son reemplazados por films de tipo
radiocrómico que son detectores básicamente del tipo químico. El diseño
consiste en el depósito de una delgada capa de material sensible sobre
una película inactiva típicamente plástica que proporciona sostén. El
material sensible consiste en una dilución de sales, usualmente se
emplea haluros de plata.

El principio de funcionamiento se basa en reacciones químicas
catalizadas por la energía absorbida por el material. Los residuos de
reacción, que son substancias con propiedades químicas diferentes al
material sensible en su estado no reactivo, poseen la particular
característica de presentar afinidad química con otros compuestos con
los que el material sensible no reactivo no tiene esa afinidad.

Se utiliza entonces procesos posteriores a la irradiación en los que se
induce la reacción entre los residuos de formación a partir del material
sensible -debido a la absorción de energía- y compuestos con afinidad
que una vez unidos producen diferencias en absorción/transmisión de luz
visible, es decir presentan diferente opacidad allí donde se produce la
combinación entre los productos de reacción por absorción de radiación y
los solutos con afinidad. Este proceso se denomina usualmente revelado
radiográfico.

Una vez realizado el proceso de revelado es necesario implementar un
método de lectura. Para este fin se aprovecha la manifestación evidente
en la diferencia de propiedades de absorción/transmisión de luz visible
y resulta posible cuantificar estas diferencias empleando técnicas de
densitometría óptica.

La respuesta del sistema es, en definitiva, la lectura densitométrica. Y
es ésta la que debe correlacionarse con la dosis absorbida, lo cual se
realiza típicamente mediante métodos empíricos de calibración.

En el caso de los films radiográficos, la capacidad dosimétrica es muy
pobre al punto que este tipo de detectores se emplean reservándolos casi
exclusivamente para determinaciones espaciales de absorción de
radiación; mientras que los films radiocrómicos -más modernos- permiten
una cuantificación confiable en términos dosimétricos proveyendo también
información espacial.

Cabe mencionar que la tejiso-equivalencia de los films radiográficos es
muy mala, mientras que esta propiedad mejora para el caso de los films
radiocrómicos.

A partir de análisis cuantitativos y determinaciones empíricas, resulta
que ;la dependencia típica de la lactura :math:`L` de un film (densidad
óptico) presenta una dependencia polinomial (usualmente aproximada por
orden 3) respecto de la dosis absorbida. De manera que, en condiciones
de requerir lineridad es necesario acotar el intervalo (rango de valores
de dosis) y determinar un ajuste lineal para la zona de interés.

En cualquier caso, ambos tipos de films presentan dificultades en cuanto
a la dependencia de la calidad del haz y de la dirección de incidencia,
aunque debe destacarse que estos problemas son menosres para el film
radiocrómico.


Adaptación de sistemas de detección al radiodiagnóstico médico
--------------------------------------------------------------

.. [1]
   Las energías de ligadura típicas son mucho menores a las del fotón
   incidente

.. [2]
   Energías menores a 100keV, aproximadamente.

.. [3]
   En el sentido del haz incidente.

.. [4]
   El gas de material sensible, gas primario, es típicamente aire o un
   gas noble como argón

.. [5]
   entre 2 y 5 mil veces mayor, aproximadamente. Por ejemplo:
   :math:`\rho_{Si(Li)}=2.33gcm^{-3}`,
   :math:`\rho_{Ge(Li)}=5.32gcm^{-3}`,
   :math:`\rho_{Cd(Te)}=6.06gcm^{-3}` y
   :math:`\rho_{Aire}=0.001297gcm^{-3}`

.. [6]
   Por entonces típicamente centelladores de sulfuro.

.. [7]
   ejemplo típico es el CsSb antomonio de cesio o materiales alcalinos.

.. [8]
   Indicado como el elemento entre paréntesis en la notación del
   compuesto.

.. [9]
   Más recientemente han cobrado importancia los centelladores plástico
