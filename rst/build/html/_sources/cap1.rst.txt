Introducción al transporte de radiación
=======================================

En este primer capítulo se desarrollará un breve resumen dedicado a
presentar los fundamentos básicos y el formalismo necesario para contar
con un primer acercamiento a las teorías del transporte de radiación.
Los modelos que describen los procesos de transporte y colisión de
partículas se encuentran fundamentados en las llamadas *teorías del
transporte*, entre las cuales el formalismo de Boltzmann es el más
aceptado y utilizado para explicar y entender los diferentes fenómenos.

No es objetivo de este texto desarrollar en detalle el formalismo
utilizado en la física de partículas especializada, sino solo presentar
el modelado matemático necesario para la comprensión de los procesos
físicos involucrados en la formación de imágenes radiológicas. Se
presenta así, una introducción al transporte de radiación y sus
diferentes tipos de interacción con la materia, se introduce la ecuación
de transporte de Boltzmann y los modelos de interacción de diferentes
tipos de partículas. Finalmente, se expone una aproximación al caso de
los fotones, en quienes se focalizara el presente curso.

Transporte de radiación e interacciones
---------------------------------------

En términos generales, la ecuación de transporte de Boltzmann es la
representación de la distribución estadística de partículas en un
entorno fuera del equilibrio. Se aplica al estudiar de varios fenómenos
físicos como flujo de calor o carga eléctrica en medios materiales
pudiendo determinar cantidades como conductividades térmica y eléctrica.

Como primer paso se hace referencia al transporte de fotones, lo que
luego puede generalizarse por medio de desarrollos análogos que incluyan
propiedades específicas del tipo de radiación de interés.

La transferencia, absorción y dispersión de energía por parte de la
radiación hacia un medio material se determinan por medio de la ecuación
de transporte de Boltzmann y modelos específicos de interacción. Existen
diferentes expresiones y aproximaciones para la ecuación de transporte
de Boltzmann, pudiendo describirse análogamente tanto en forma
diferencial como integral.

El objetivo es determinar el flujo total de radiación :math:`\Phi_{T}` o
bien la radiancia :math:`R` de partículas emitida por una fuente y
transportada en un determinado medio material. Bajo ciertas
aproximaciones, las cantidades escalares :math:`\Phi_{T}` y :math:`R`
satisfacen:

.. math:: R\left(\vec{r}, \vec{\Omega}\right) = \frac{d^{2}\Phi_{T}}{dA\, d\Omega \cos{\theta}} \approx \frac{\Phi_{T}}{A\, \Omega \cos{\theta}}

donde :math:`\vec{r}` y :math:`\vec{\Omega}` son los vectores posición y
dirección de movimiento de la partícula que atraviesa el área :math:`A`
formando un ángulo :math:`\theta` con el versor normal a la superficie
de :math:`A`.

Desde un punto de vista matemático, la ecuación de transporte de
radiación de Boltzmann es expresada como una ecuación difusiva
integro-diferencial, cuya formulación clásica para observables
caracterizados por función de distribución :math:`\Theta` dependientes
de la posición :math:`\vec{r}` es:

.. math::

   \frac{\partial \Theta}{\partial t} \arrowvert_{\textrm{int}} - \frac{\partial \Theta}{\partial t} = \frac{\partial \Theta}{\partial r} \frac{\vec{p}}{m} + \frac{\partial \Theta}{\partial \vec{p}}\cdot \vec{V}
    \label{eq.int-dif}

donde :math:`\vec{p}` y :math:`m` son momento y la masa de la partícula,
:math:`t` indica el tiempo, :math:`\vec{V}` es el campo de fuerzas y el
subíndice :math:`\textrm{int}` hace referencia al modelo especíco de
interacción/colisión entre las partículas del sistema.

En este sentido, hay diferentes modos de interacción entre el flujo de
partículas y el medio material. A este propósito, es útil introducir la
probabilidad de ocurrencia de una cierta interacción :math:`i`, definida
físicamente por la sección eficaz :math:`\sigma_{i}` , referida al
i-ésimo mecanismo de interacción. Por tanto, la probabilidad total
:math:`\sigma_{T}` de ocurrencia de una interacción, de cualquier tipo,
se obtiene por medio de la suma de todas las contribuciones por parte de
cada uno de los procesos de inteacción. A nivel macroscópico, la sección
eficaz total macroscópica :math:`\Sigma_{T}` se define mediante:

.. math:: \Sigma_{T} \equiv N \sigma_{T}

donde :math:`N` es la densidad de centros dispersores por unidad de
volumen, por lo que la unidad de :math:`N` resulta de la forma
:math:`cm^{-3}`.

Los procesos de interacción incluyen absorción y dispersión (o
*scattering*), por lo que:

.. math:: \Sigma_T = \Sigma_{abs} + \Sigma_{sca}

donde :math:`\Sigma_{abs}` y :math:`\Sigma_{sca}` representan las
componentes de absorción y *scattering* respectivamente.

La distribución de la cantidad de colisiones :math:`n` a lo largo de la
trayectoria recorrida (*path*) así como la distanciamedia entre
colisiones sucesivas :math:`\lambda` se obtienen de:

.. math::

   \frac{dn}{ds} = -\Sigma n \Rightarrow n(s) = n(0) e^{-\Sigma s} \Rightarrow \lambda \equiv \frac{\int_{0}^{\infty} s e^{-\Sigma s} ds}{\int_{0}^{\infty} e^{-\Sigma s} ds} = \frac{1}{\Sigma_T}
    \label{dn}

La distancia media entre colisiones sucesivas obtenida a partir de esta
distribución :math:`\lambda` es el camino libre medio o *mean free path*
(mpf) y queda determinado por medio de la sección eficaz total.

Estado de fase en transporte de radiación
-----------------------------------------

Una partícula de momento :math:`p` con longitud de onda :math:`\hbar/p`
transportada en un medio material de espesor :math:`x` tal que
:math:`x << \hbar/p` estará completamente determinada (en su espacio de
fase) por la posición :math:`\vec{r}`, la dirección de movimiento
:math:`\vec{\Omega}`, la energía :math:`E` y el tiempo :math:`t`.

Sea :math:`N(\vec{r}, \vec{\Omega}, E, t)` la densidad angular de
partículas en estados de fase :math:`[(x, y, z); (\theta, \phi); E;t]`,
que representa la densidad de partículas en el volumen :math:`d\vec{r}`
alrededor de :math:`\vec{r}`, viajando en direcciones
:math:`d\vec{\Omega}` entorno a :math:`\vec{\Omega}` con energía
:math:`E` a tiempo :math:`t`.

El flujo vectorial angular de partículas :math:`\vec{\Psi}` puede
obtenerse a partir de la densidad angular y la velocidad :math:`\vec{v}`
de las partículas:

.. math::

   \vec{\Psi} = \vec{v}N(\vec{r}, \vec{\Omega}, E, t)
    \label{eq.flujo.vec}

El flujo angular escalar (o simplemente flujo angular) :math:`\Psi` se
obtiene a partir de la expresión `[eq.flujo.vec] <#eq.flujo.vec>`__, y
sus unidades son :math:`cm^{-2}\, s^{-1} \, str^{-1}` .

Integrando el flujo angular :math:`\Psi` en todas direcciones para
valores dados de :math:`E`, :math:`\vec{r}` y :math:`t` se obtiene una
cantidad proporcional a la tasa de población-ocupación del estado
:math:`(\vec{r}, R,t)`, a veces denominado tasa de “reacción” o
“creación”. A partir de esto, puede determinarse el flujo escalar (o
simplemente flujo) :math:`\Phi_T` dado por:

.. math:: \Phi_T \equiv \int_{4\pi} \Psi d\Omega

La tasa de ocurrencia de eventos (por unidad de volumen), en términos de
la probabilidad de cada j-ésimo tipo de interacción :math:`\Lambda`
queda determinada por:

.. math:: \Lambda \equiv \Sigma_j \Phi_T

La fluencia angular se obtiene a partir de la integral en el tiempo del
flujo, y representa el número total de partículas por unidad de área por
unidad de energía atravesando el punto :math:`\vec{r}` con dirección
:math:`d\Omega` entorno a :math:`\Omega`.

Así mismo, puede calcularse la fluencia escalar (o fluencia total)
:math:`J(\vec{r}, E,t)` que resulta de integrar la fluencia angular para
todas las direcciones posibles:

.. math:: J = |J(\vec{r}, E,t)| = \int_{4\pi} \vec{v} N(\vec{r}, \vec{\Omega}, E, t) d\vec{\Omega}\cdot\hat{n}

donde :math:`|\vec{J}|` es la corriente de partículas y :math:`\hat{n}`
representa un versor en dirección arbitraria para el cálculo de la
fluencia escalar :math:`J`.

A partir de esto, puede plantearse la ecuación de transporte de
radiación de Boltzmann, dada por:

.. math::

   \frac{1}{\vec{v}}\frac{\partial}{\partial t}\Psi(\vec{r}, \vec{\Omega}, E, t) + \vec{\Omega}\cdot \vec{\nabla}\Psi - S = \int \int_{4\pi} \Psi(\vec{r}, \vec{\Omega'}, E', t) K(\vec{\Omega'}, E' \rightarrow \vec{\Omega}, E) dE' d\vec{\Omega'}
    \label{ETB}

donde :math:`S` es la fuente de radiación y
:math:`K(\vec{\Omega'}, E' \rightarrow \vec{\Omega}, E)` es el operador
del kernel que cambia el estado de fase de las “coordenadas” primadas
:math:`(\vec{\Omega'}, E')` a las sin primar :math:`(\vec{\Omega}, E)`
debido a los procesos de *scattering* en la posición :math:`\vec{r}`.

Bases para el cálculo de observables a partir de la ecuación de transporte de radiación
---------------------------------------------------------------------------------------

Para un sistema estacionario *steady state* puede aplicarse el teorema
de Liouville [1]_ en una aproximación clásica [2]_ para mostrar que un
sistema de partículas evoluciona según la mecánica clásica cuya densidad
de estados se representa en un espacio de las fases constante
:math:`\Re^{3}\wp^{3}`, donde :math:`\Re` y :math:`\wp` refieren a los
espacios de posición :math:`\vec{r}` y de momento :math:`\vec{p}`,
respectivamente.

En estado de equilibrio térmico la probabilidad de ocurrencia de un
estado se determina por medio de la estadística de Fermi-Dirac para la
cual la función de distribución del sistema homogéneo depende únicamente
de la energía :math:`E`.

La expresión `[eq.int-dif] <#eq.int-dif>`__ de la ecuación de Boltzmann
puede simplificarse para situaciones en que el término de interacciones
:math:`\frac{\partial \Theta}{\partial t}|_\textrm{int}` sea
proporcional a la diferencia entre la función de distribución
:math:`\Theta` en presencia de efetos externos :math:`\vec{V}` y la
función de distribución en equilibrio térmico. Esta condición es
equivalente a asumir que una vez cesen los efectos externos, el sistema
retorna al equilibrio, debido a las interacciones, con velocidad
determinada (proporcional expecíficamente) por la desviación inicial
respecto de la condición de equilibrio. Como se mencionó, a partir de
estas consideraciones puede calcularse cantidades como tiempo de
relajación (inclusive pesado por energía de sistema), conductividad
térmica/eléctrica y difusividad, entre otros.

Densidad de fluencia energética
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Como ejemplo de la aplicación del formalismo para el estudio de
observables, se considera el caso de la energía :math:`E`, que es
típicamente la cantidad más importante a fines dosimétricos ya que
determina la dosis absorbida.

Sea :math:`\bar{E}` el valor de expectación de la energía :math:`E`, sin
considerar la componente de energía en reposo, portada por todos los
quanta que constituyen el haz :math:`N_q`. La fluencia energética
:math:`\Psi` se define por:

.. math:: \Psi \equiv \frac{d\bar{E}}{dA}

Entonces, para un haz monocromático se tiene
:math:`\bar{E} = E_{0}N_{q}` , como se espera. Y, por tanto,
:math:`\Psi = E_{0}\Phi`.

Para el estudio de la evolución de sistemas debido a perturbaciones
externas, es conveniente considerar el tiempo :math:`t_0` en ausencia de
fluencia energética :math:`\Psi(t_0) = 0` y el tiempo :math:`t_{max}`
que se corresponde con el máximo de fluencia energética
:math:`\Psi(t_{max}) = \Psi_{max}`.

La tasa de fluencia energética :math:`\Upsilon` puede calcularse para
cualquier tiempo :math:`t` en el intervalo :math:`(t_0 ,t_{max})`, y se
calcula a partir de:

.. math:: \Upsilon = \frac{d\Psi}{dt} = \frac{d}{dt} \left(\frac{d\bar{E}}{dA}\right) \Longrightarrow \Psi(t_0,t) = \int_{t_{0}}^{t}{\Upsilon(t')dt'}

Por tanto, manteniendo constante la tasa de fluencia energética
:math:`\Psi(t_0 ,t) = \Upsilon(t - t_0 )` resulta que la tasa de
fluencia energética, también denominada densidad de flujo energético,
:math:`\Upsilon` es proporcional a la densidad de flujo :math:`\Phi` si
el haz es monocromático :math:`\Upsilon = E_0 \Phi`.

De modo que para determinar observables, experimentalmente, por medio de
mediciones a tiempo :math:`t` en la posición :math:`\vec{r}`, en
términos de la energía :math:`E` dirección de movimiento :math:`\Omega`
dado por los ángulos polar y azimutal :math:`(\theta, \phi)`, resulta
que la densidad de flujo diferencial es
:math:`\Upsilon(E, \theta, \phi)` y la densidad de flujo se obtiene de:

.. math:: \Upsilon = \int_{0}^{\pi}{\int_{0}^{2\pi}{\int_{0}^{E}{\Upsilon(E', \theta', \phi')\sin{\theta'}d\theta'}d\phi'}dE'}

En unidades de inversa de área y tiempo, :math:`cm^{-2}` :math:`s^{-1}`
, típicamente.

Modelos de interacción de partículas con la materia a partir de la ecuación de transporte de Boltzmann
------------------------------------------------------------------------------------------------------

Esta sección presenta, de modo extremadamente escueto, los resultados
principales para los fenómenos de interacción debido al paso de
partículas por un medio material.

Cada uno de los modelos se obtiene de la aplicación de la ecuación de
transporte, sujeto a las consideraciones necesarias en cada caso [3]_.
En particular, para cada tipo de radiación y material con el que se
interactúa, el problema consiste en describir las propiedades de la
fuente de radiación (el término :math:`S` en la expresión
`[ETB] <#ETB>`__) e introducir los modelos físicos que determinan el
operador *kernel*
:math:`K(\vec{\Omega'}, E' \rightarrow \vec{\Omega}, E)` a partir de las
funciones de distribución de probabilidades asociadas a cada tipo de
proceso de interacción posible. Para el caso de radiación primaria, el
término :math:`S` representa completamente la fuente, mientras que para
la radiación secundaria, scattering en general, la producción misma de
partículas debido a las interacciones de radiación primaria.

Como resultado de las interacciones de partículas cargadas de velocidad
:math:`v = \beta c` se producen péridas energéticas en cada colisión
:math:`\Delta E`, y correspondiente pérdida de energía por unidad de
camino :math:`\frac{dE}{dy}` recorrido , donde y es la dirección a lo
largo del track.

Una vez se realizan los modelos de interacción, se determinan las
funciones de distribución de probabilidades que dan cuenta de las
características estadísticas de los procesos físicos, que quedan
determinados por las secciones eficaces :math:`\sigma`.

A partir de las expresiones `[dn] <#dn>`__ y `[ETB] <#ETB>`__ puede
calcularse el número medio de colisiones con pérdida energética entre
:math:`E_{loss}` y :math:`E_{loss} + \Delta E_{loss}` al recorrer la
distancia :math:`\delta y`:

.. math:: \frac{dE}{dy} = \rho_{e} \delta y \frac{d\sigma}{dE} dE

donde :math:`\rho_{e}` es la densidad electrónica.

La determinación del operador *kernel*
:math:`K(\vec{\Omega'}, E' \rightarrow \vec{\Omega}, E)` requiere del
conocimiento de los mecanismos por los cuales se produce en cambio de
energía y las deflexiones angulares.

Pérdidas energéticas en interacciones de partículas cargadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cuando las interacciones ocurren con los electrones orbitales de los
átomos blanco, se producen en general ionizaciones, excitación atómica o
bien excitación colectiva. En medios absorbentes delgados las colisiones
que se producen presentan varianzas grandes.

Para partículas cargadas pesadas (de carga :math:`Z_{p}` y masa molar
:math:`M_{p}` ) interactuando con un material homogéneo constituido por
átomos de número atómico :math:`Z_{A}` y masa molar :math:`M_{A}` , la
pérdida de energía por colisiones pueden obtenerse a partir de la teoría
de Bethe-Bloch, que permite determinar el *stopping power* a lo largo
del *track* (:math:`\frac{dE}{dy}`):

.. math::

   \frac{dE}{dy} = 4 r^{2}_{e} \rho m_{e} c^{2} \frac{Z_{A}}{M_{A}} \frac{Z_{p}^{2}}{\beta^{2}} \times 
           \left[
           \frac{1}{2} \ln{\left(
                   2 m_{e} c^{2} \beta^{2} W_{max} \gamma^{2}
                   \right)}
                   - \beta^{2} - \ln{I} - \frac{C}{Z_{A}} - \frac{\delta}{2}
           \right]

donde :math:`r_e` y :math:`m_e` son el radio clásico y masa de electrón
en reposo, respectivamente.

Los últimos tres términos entre corchetes representan los efectos de
potencial medio de ionización :math:`I`, coeficiente de apantallamiento
nuclear :math:`C` y efecto de densidad :math:`\delta`.

Efectos angulares por interacciones de partículas cargadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las partículas cargadas sufren deflexiones angulares al atravesar e
interactuar con un medio material. Existen desviaciones pequeñas debidas
a interacciones de tipo Coulombianas en el *scattering* con el campo
nuclear [4]_.

El efecto de dispersión angular por efecto Coulombiano es representado
por la teoría de Molière, produciendo distribuciones de deflexiones
prácticamente Gaussianas :math:`P(\theta)`, de acuerdo con:

.. math::

   \begin{split}
     P(\theta) &= \frac{1}{2 \pi {\theta^{*}}^{2}} e^{-\left[\frac{1}{2}\left(\frac{\theta}{\theta^{*}}\right)^{2}\right]} d\Omega \\
           &= \frac{1}{\sqrt{2 \pi} \theta^{*}} e^{-\left[\frac{1}{2}\left(\frac{\theta_{plano}}{\theta^{*}}\right)^{2}\right]} d\theta_{plano}
    \end{split}

donde :math:`\theta^{*}` es la media de la distribución Gaussiana y
:math:`\theta_{plano}` representa la proyección planar del ángulo polar
que forma el ángulo sólido :math:`d\Omega` y se trabaja en la
aproximación a bajo ángulo, de modo que
:math:`\theta^{2} \approx \theta_{x}^{2} + \theta_{y}^{2}` , para las
proyecciones planares en los ejes :math:`x` e :math:`y`, siendo
:math:`\theta_{x}^{2}` y :math:`\theta_{y}^{2}` independientes pero
respetando la misma distribución.

Determinación de distancias de interacción
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La distancia atravesada dentro del medio material se denomina *radiation
length* :math:`X`, típicamente medida en :math:`g \cdot cm^{-2}`.

A modo de ejemplo, para el caso particular de electrones de enegías
altas, la pérdida de energía dominante es por medio de radiación de
*Bremsstrahlung* y producción de pares. En este caso, la *radiation
length* para estos dos procesos se denomina :math:`X_{0}` y se calcula a
partir de la teoría de Tsai:

.. math:: X_{0} = \frac{B}{4 \alpha r_{e}^{2} N_{A}} \frac{1}{Z^{2}[L_{rad} - f(Z)] + Z L'_{rad}}

Los parámetros :math:`L_{rad}` y :math:`L'_{rad}` son coeficientes que
pueden determinarse para cada tipo de átomo. Por otro lado, la función
parametrizada :math:`f(Z)` se obtiene de:

.. math::

   f(Z) = (\alpha Z)^{2} \left\{
               \left[1 + (\alpha Z)^{2}]^{-1} + 0.202 - 0.0369 (\alpha Z)^{2} + 0.008 (\alpha Z)^{4} - 0.002 (\alpha Z)^{6} \right]
                  \right\}

Para el caso de moléculas, se utilizan modelos de composición efectiva,
y la *radiation length* :math:`X_{0,mol}` de compuestos formados por
componentes con pesos relativos :math:`q_{k}` , puede calcularse de modo
aproximado utilizando:

.. math:: \frac{1}{X_{0, mol}} = \sum_{k} \frac{q_{k}}{X_{k}}

Aproximaciones para el transporte de fotones en medios materiales
-----------------------------------------------------------------

En el caso particular que se estudiará en el presente curso, el interés
está en los procesos físicos involucrados en la interacción de rayos
:math:`X` de radiodiagnóstico, con medios materiales de interés
biológico.

Si se consideran las configuraciones típicas, y los procesos más
probables en las geomtrías usuales en radiodiagnóstico, resulta que la
radiación primaria proviene de la fuente :math:`S` que en este caso se
trata del haz de rayos :math:`X` utilizado.

Los procesos de interacción suceden dentro del paciente y el haz
emergente, determinado por la ecuación de transporte de Boltzmann,
formado tanto por radiación primaria (proveniente de la fuente
:math:`S`) y radiación de *scattering* generada por interacciones dentro
del paciente, llega en definitiva al sistema de detección para formar la
imagen radiológica.

Según la energía del haz de la fuente :math:`S`, y las propiedades de
absorción/dispersión, así como de las dimensiones físicas del paciente,
resultará que la mayor parte del flujo ergente se corresponderá con la
componente primaria o de *scattering*.

Incorporando los modelos de interacción radiación-materia que
corresponden a fotones con energías de kilovoltaje, típicas de
radiodiagnóstico, tejidos biológicos y para dimensiones típicas de
pacientes, resulta que en el flujo emergente la componente de radiación
primaria es prácticamente todo el flujo, existiendo contribuciones del
orden del :math:`2 \%` por parte del *scattering*. Por tanto, la
descripción del transporte de la componente primaria del flujo emergente
proporciona una buena aproximación del flujo de radiación que alcanzará
el detector para dar lugar a la formación de la imagen.

Para modelar el transporte de radiación primaria, utilizando la ecuación
de transporte de Boltzmann en la expresión `[ETB] <#ETB>`__, se
introducen algunas aproximaciones a fin de facilitar la resolución del
problema aplicable a las condiciones propias del proceso radiológico
típico.

La primera condición es considerar el problema en estado estacionario,
ya que se admite el equilibrio del flujo
incidente/interactuante/emergente. De este modo, se tiene que se anula
el primer término de la expresión `[ETB] <#ETB>`__, ya que
:math:`\frac{\partial}{\partial t} \Psi = 0`.

Suponiendo que el transporte se realiza, principalmente, en una
dirección, denominada :math:`z`, el segundo término en la expresión
`[ETB] <#ETB>`__ resulta :math:`\Omega\cdot\vec{\nabla} = \frac{d}{dz}`.

El problema así planteado presenta simetría azimutal, por lo que
resulta:
:math:`\int \int_{4\pi} dE' d\Omega' = \int dE' 2\pi \int \sin \theta d\theta`.

Si el haz emergente está compuesto, casi exclusivamente por radiación
primaria, ésta debe haber atravesado el material (paciente)
prácticamente sin colisiones, es decir, que la integral aplicada al
operador del *kernel*
:math:`\int dE' 2\pi \int \sin \theta d\theta K(\vec{\Omega'}, E' \rightarrow \vec{\Omega}, E) ~ 0`
(operador nulidad).

Por lo tanto, la ecuación de transporte de Boltzmann se reduce a:

.. math:: \frac{d}{dz} \Psi^{*} - S = 0

Para :math:`\Psi^{*}` a lo largo del eze :math:`z`.

Además, la fuente de radiación :math:`S` es el flujo emitido por una
fuente de modo tal que emergen rayos quasi paralelos con distribución
quasi uniforme del frente onda, considerado plano y homoéneo. Es decir,
:math:`S = \Psi_{source} (z) = \Psi^{*}`.

A partir de la expresión 20 es inmediato que
:math:`\Psi^{*}(z) = \Psi(z = 0) e^{-cz}`, conocida como ecuación de
Lambert-Beer y describe la conocida relación de atenuación exponencial
por parte de la radiación al atravesar un medio material. El análogo de
este proceso a nivel microscópico es la penetración cuántica de la
barrera de potencial, cuya solución coincide, como es de esperar.

De este modo, se obtiene a partir de la ecuación de transporte de
Boltzmann una expresión significativamente útil para describir, de modo
aproximado, el comportamiento de los procesos de interacción en el
ámbito de radiología. Bajo estas aproximaciones, se asume que las
contribuciones de *scattering* son despreciables, que el haz de
radiación proviene de una fuente que emite luz en un frente de onda
plano paralelo uniforme y en fase, así como que el medio irradiado es
homogéneo e isotrópico.

En definitiva, la relación encontrada, gracias a las relaciones unívocas
descritas al inicio del capítulo, permite cuantificar flujo, fluencia
(si se conocen las características energéticas del haz) y demás
cantidades vinculadas. Por ejemplo, la intensidad del haz transmitido
:math:`I` satisface:

.. math:: I(z) = I(z=0) e^{-\int dE dz \mu} = I(0) e^{- \int dE \mu(E) \Delta z} = I(0) e^{-\mu(E_{0}\Delta z}

donde la última igualdad es válida para haces monocromáticos y
:math:`\mu` se denomina coeficiente de absorción lineal.

.. raw:: latex

   \CitationPrefix{\thechapter.}

.. [1]
   Aplicado a sistemas conservativos.

.. [2]
   Válido también para mecánica Hamiltoniana.

.. [3]
   Las derivaciones específicas respecto de la ecuación de transporte no
   se presentan por encontrarse fuera del alcance de este texto.

.. [4]
   Para el caso particular de haces de hadrones, las interacciones
   fuertes contribuyen también a los efectos de dispersión múltiple
   (*multiple scattering*).
