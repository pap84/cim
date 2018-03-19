Procesamiento de imágenes con derivadas - Detección de esquinas y bordes
========================================================================

El *Capítulo* está dedicado a introducir algunos conceptos
genéricos, acompañados por métodos específicos, para detectar,
evidenciar y resaltar puntos de particular importancia en una imagen:
puntos de bordes, aristas, contornos.

Existe interés y gran practicidad en varios campos de aplicación, en
referencia a la detección de puntos de bordes, eventualmente la conexión
entre éstos que dan lugar a contornos, permitiendo así evidenciar la
presencia de objetos delimitados quie podrán luego ser oportunamente
caracterizados.


Detección de bordes utilizando derivadas
----------------------------------------

Es posible introducir conceptos análogos a la derivación de cálculo
continuo de orden 1, 2, etc. a fin de realizar procesamientos
específicos sobre imágenes de interés.

Para regiones con valores de *pixel* constantes, se anulará la derivada
primera, de modo que puede establecerse precisamente este criterio para
asociar propiedades de la región con la derivada.

Por otro lado, si existe cambio en los valores de *pixel*, se generará
una variación en la derivada, permitiendo nuevamente establecer una
asociación entre las propiedades de la región (entorno al punto de
interés) y su derivada.

Así mismo, se aplica el concepto de derivada segunda, cuyo signo
indicará la dirección (positiva o negativa, según se defina el sistema
de coordenadas) del gradiente del punto de interés.


Gradiente de una imagen
-----------------------

El operador gradiente :math:`\vec{\nabla}` aplicado a la imagen
:math:`f(m, n)` se define por medio de:

.. math::

   \begin{aligned}
       \vec{\nabla}\left[ f(m, m) \right] \equiv \left[ \begin{array}{c}  \nabla_{m} \left[ f(m, n) \right]
           \\  \nabla_{n} \left[ f(m, n) \right] \\  \end{array} \right]
       = \left[ \begin{array}{c}  \frac{f(m + \Delta m, n) - f(m - \Delta m, n)}{2 \Delta m} \\ \\
        \frac{f(m, n + \Delta n) - f(m, n - \Delta n)}{2 \Delta n} \\  \end{array} \right]
   \label{EqLXXIII}\end{aligned}

De modo que la expresión vectorial del gradiente :math:`\vec{\nabla}`
resulta:

.. math::

   \begin{aligned}
       \lvert \vec{\nabla}\left[ f(m, m) \right] \rvert = \sqrt{\nabla_{m}^2 + \nabla_{n}^2} \\ \nonumber
       \theta(m, n) = \arctan \left( \frac{\nabla_{m}}{\nabla_{n}} \right)
   \label{EqLXXIV}\end{aligned}

Nótese que, para propósitos de aplicación dado que se implementarán
métodos basados en umbralamiento -y por tanto, solo tienen relevancia
las diferencias relativas- conviene introducir una aproximación para el
módulo del gradiente dada por:

.. math::

   \begin{aligned}
       \lvert \vec{\nabla}\left[ f(m, m) \right] \rvert \approx \lvert \vec{\nabla_{m}} \left[ f(m, n) \right]
    \rvert +  \lvert \vec{\nabla_{n}} \left[ f(m, n) \right] \rvert
   \label{EqLXXV}\end{aligned}


Detección de bordes: El operador de Sobel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Utilizando la expresión `[EqLXXIII] <#EqLXXIII>`__ es posible practicar
una convolución de la imagen original :math:`f(m, n)` utilizando una
máscara :math:`\mathbf{M}` de :math:`3 \times 3` siguiendo la
definición:

.. math::

   \begin{aligned}
       \mathbf{M} \equiv \left[ \begin{array}{ccc}  M_{1, 1} & M_{1, 2} & M_{1, 3}  \\  M_{2, 1} & M_{2, 2} & M_{2, 3} \\
       M_{3, 1} & M_{3, 2} & M_{3, 3} \end{array} \right]
   \label{EqLXXVI}\end{aligned}

En particular, para el operador de Sobel :math:`M_{Sobel}` es habitual
utilizar las expresiones:

.. math::

   \begin{aligned}
       \mathbf{M_{Sobel}} = \begin{array}{c} \left[ \begin{array}{ccc}  -1 & 0 & 1  \\  -2 & 0 & 2 \\ -1 & 0 & 1 \end{array} \right]
       %\, \, \; \leftrightarrow \nabla_{m}
       \\ %\nonumber \\ \nonumber
       \left[ \begin{array}{ccc}  -1 & -2 & -1  \\  0 & 0 & 0 \\ 1 & 2 & 1 \end{array} \right] \end{array}
   \end{aligned}

donde el primer arreglo se utiliza para obtener :math:`\mathbf{\nabla_{m}}` y el segundo :math:`\mathbf{\nabla_{n}}`.

Si el bloque de la imagen original :math:`f(m, n)`, para la dimensión de la máscara (3 :math:`\times` 3) es :math:`B(k, l)` con  :math:`k \in [m - \Delta m, m + \Delta m]` y :math:`k \in [n - \Delta n, n + \Delta n]`

.. math::

   \begin{aligned}
       \mathbf{\nabla_{m}} = \left( B_{1, 3} + 2 B_{2, 3} + B_{3, 3} \right) -
   \left( B_{1, 1} + 2 B_{2, 1} + B_{3, 1} \right)
       \\ \nonumber
       \mathbf{\nabla_{n}} = \left( B_{3, 1} + 2 B_{3, 2} + B_{3, 3} \right)
    -  \left( B_{1, 1} + 2 B_{1, 2} + B_{1, 3} \right)
   \label{EqLXXVIII}\end{aligned}

La aplicación de la técnica de detección y resaltado de bordes, esquinas
y contornos por medio del método de sobel consiste en realizar la
convolución utilizando la expresión `[EqLXXVIII] <#EqLXXVIII>`__, y
luego al resultado aplicar un criterio de umbralamiento por medio de un
parámetro :math:`P_{Sobel}` de modo que:

.. math::

   \begin{aligned}
       \mathbf{M_{Sobel}} \otimes f(m, n) = \left\{ \begin{array}{ll}
       1 & \mbox{$\lvert \vec{\nabla} \left[ f(m, n) \right] \rvert > P_{Sobel}$}\\
       0 & \mbox{$\lvert \vec{\nabla} \left[ f(m, n) \right] \rvert \le P_{Sobel}$}.\end{array} \right.
   \label{EqLXXIX}\end{aligned}


Detección de bordes: El operador de Prewitt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este operador también está definido a partir de la aplicación de
derivadas primeras. De hecho, conceptualmente es similar al operador de
Sobel, excepto por los valores específicos de los elementos de matriz de
la máscara de convolución :math:`M_{Prewitt}`, dada por:

.. math::

   \begin{aligned}
       \mathbf{M_{Prewitt}} = \begin{array}{c} \left[ \begin{array}{ccc}  -1 & 0 & 1  \\  -1 & 0 & 1 \\ -1 & 0 & 1 \end{array} \right]
       \\ \nonumber \\ \nonumber
       \left[ \begin{array}{ccc}  1 & 1 & 1  \\  0 & 0 & 0 \\ -1 & -1 & -1 \end{array} \right] \end{array}
   \label{EqLXXX}\end{aligned}

donde el primer arreglo se utiliza para obtener
:math:`\mathbf{\nabla_{m}}` y el segundo :math:`\mathbf{\nabla_{n}}`.


Detección de bordes: El operador de Roberts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La particularidad de este operador es que, diferenciándose de los
operadores de Sobel y Prewitt, posee la capacidad de evidenciar puntos
de borde pero no así la orientación de éstos.

El operador de Roberts se implementa utilizando las diagonales
correspondientes al *pixel* de interés, a izquierda :math:`D_{Iz}` y a
derecha :math:`D_{De}`, definidas según:

.. math::

   \begin{aligned}
       D_{Iz} \equiv f(m, n) - f(m-1, n-1) \\ \nonumber
       D_{De} \equiv f(m, n) - f(m-1, n+1)
   \label{EqLXXXI}\end{aligned}

De modo que el operador de Roberts :math:`M_{Roberts}` consiste en
determinar para cada *pixel* la cantidad:

.. math::

   \begin{aligned}
       M_{Roberts} \equiv \sqrt{D_{Iz}^2 + D_{De}^2} \, \, \, \rightarrow \, \,
       M_{Roberts} \approx \lvert D_{Iz} \rvert + \lvert D_{De} \rvert
   \label{EqLXXXII}\end{aligned}


Detección de bordes: Operador de Kirsch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El método de Kirsch consiste en introducir máscaras :math:`M_{Kirsch}`
que representan 8 rotaciones en las direcciones principales, es decir 4
direcciones en filas y columnas (rotaciones de :math:`0`,
:math:`\frac{\pi}{2}`, :math:`\pi` y :math:`\frac{3 \pi}{2}`), y otras 4
rotaciones respecto de las diagonales principales (rotaciones de
:math:`\frac{\pi}{4}`, :math:`\frac{3 \pi}{4}`, :math:`\frac{5 \pi}{4}`
y :math:`\frac{7 \pi}{4}`).

Las máscaras de Kirsch se definen como sigue:

.. math::

   \begin{aligned}
       \mathbf{M_{Kirsch}} \equiv \left\{
       \begin{array}{cccc}
       \left[ \begin{array}{ccc}  -3 & -3 & 5  \\  -3 & 0 & 5 \\ -3 & -3 & 5 \end{array} \right] &
       \left[ \begin{array}{ccc}  -3 & 5 & 5  \\  -3 & 0 & 5 \\ -3 & -3 & -3 \end{array} \right] &
       \left[ \begin{array}{ccc}  5 & 5 & 5  \\  -3 & 0 & -3 \\ -3 & -3 & -3 \end{array} \right] &
       \left[ \begin{array}{ccc}  5 & 5 & -3  \\  5 & 0 & -3 \\ -3 & -3 & -3 \end{array} \right]
       \\ 0 & \frac{\pi}{4} & \frac{\pi}{2} & \frac{3 \pi}{4}
       \\ \nonumber
        \left[ \begin{array}{ccc}  5 & -3 & -3  \\  5 & 0 & -3 \\ 5 & -3 & -3 \end{array} \right] &
        \left[ \begin{array}{ccc}  -3 & -3 & -3  \\  5 & 0 & -3 \\ 5 & 5 & -3 \end{array} \right] &
        \left[ \begin{array}{ccc}  -3 & -3 & -3  \\  -3 & 0 & -3 \\ 5 & 5 & 5 \end{array} \right] &
        \left[ \begin{array}{ccc}  -3 & -3 & -3  \\  -3 & 0 & 5 \\ -3 & 5 & 5 \end{array} \right]
       \\ \pi & \frac{5 \pi}{4} & \frac{3 \pi}{2} & \frac{7 \pi}{4}
       \end{array} \right.
   \label{EqLXXXIII}\end{aligned}



Detección de bordes: Operadores de Robinson y Frei-Chen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El *set* de máscaras de Robinson es similar al de Kirsch, con la
diferencia en los valores de máscara para cada uno de los ángulos. En
particular, para ángulo 0\ :math:`^{o}`, el operador de máscara de
Robinson es:

.. math::

   \begin{aligned}
       \mathbf{R_{0}} = \left[ \begin{array}{ccc}  -1 & 0 & 1  \\  -2 & 0 & 2 \\ -1 & 0 & 1 \end{array} \right]
   \end{aligned}

El *set* de máscaras de Frei-Chen constituye una autobase, por lo que
las 9 componentes del *set* permiten expandir, con los pesos
correspondientes, cualquier matriz 3 :math:`\times` 3. Por lo tanto, las
máscaras de Fri-Chen, representan una generalización de los métodos de
*image mask*. Las expresiones de las máscaras de Fri-Chen
(:math:`\mathbf{FC_{k}} \; \; k \in [1, 9]`) son:

.. math::

   \begin{aligned}
       \mathbf{ FC_{1} \; \; FC_{2} \; \; FC_{3} }  =  \nonumber \\
       \frac{1}{2 \sqrt{2}} \left\{
       \begin{array}{cccc}
       \left[  \begin{array}{ccc}  1 & \sqrt{2} & 1  \\  0 & 0 & 0 \\ -1 & -\sqrt{2} & -1 \end{array} \right] &
       \left[ \begin{array}{ccc}  1 & 0 & -1  \\  \sqrt{2} & 0 & -\sqrt{2} \\ 1 & 0 & -1 \end{array} \right] &
       \left[ \begin{array}{ccc}  -1 & 0 & 1  \\  0 & 0 & 0 \\ 1 & 0 & -1 \end{array} \right] &
       \end{array} \right\} \nonumber
   \end{aligned}

.. math::

   \begin{aligned}
       \mathbf{ FC_{4} \; \; FC_{5} \; \; FC_{6} }  =  \nonumber \\
       \frac{1}{2 \sqrt{2}} \left\{
       \begin{array}{cccc}
       \left[  \begin{array}{ccc}  \sqrt{2} & -1 & 0  \\  -1 & 0 & 1 \\ 0 & 1 & -\sqrt{2} \end{array} \right] &
       \left[ \begin{array}{ccc}  0 & 1 & 0  \\  -1 & 0 & -1 \\ 0 & 1 & 0 \end{array} \right] &
       \left[ \begin{array}{ccc}  0 & -1 & \sqrt{2}  \\  1 & 0 & -1 \\ -\sqrt{2} & 1 & 0 \end{array} \right] &
       \end{array} \right\} \nonumber
   \end{aligned}

.. math::

   \begin{aligned}
       \mathbf{ FC_{7} \; \; FC_{8} }  =  \nonumber \\
       \frac{1}{6} \left\{
       \begin{array}{cccc}
       \left[  \begin{array}{ccc}  1 & -2 & 1  \\  -2 & 4 & 2 \\ 1 & -2 & 1 \end{array} \right] &
       \left[ \begin{array}{ccc}  -2 & 1 & -2  \\  1 & 4 & 1 \\ -2 & 1 & -2 \end{array} \right] &
       \end{array} \right\} \nonumber
   \end{aligned}

.. math::

   \begin{aligned}
       \mathbf{ FC_{9} }  =  \nonumber \\
       \frac{1}{3} \left\{
       \begin{array}{cccc}
       \left[  \begin{array}{ccc}  1 & 1 & 1  \\  1 & 1 & 1 \\ 1 & 1 & 1 \end{array} \right] &
       \end{array} \right\}
   \end{aligned}

El modo de aplicar la :math:`M` a la Imagen :math:`I`, que provee el
resultado :math:`R`, se obtiene operando del siguiente modo:

.. math::

   \begin{aligned}
       R = \sum _{j=1} ^{9} M_{j} \, I_{j} = \lvert M \rvert \; \lvert I \rvert \; \cos(\theta) = V_{M}^{T} \; V_{I}
   \label{EqAAF}\end{aligned}

donde :math:`^{T}` indica la transpuesta y los vectores :math:`V_{M}` y
:math:`V_{I}` (de dimensión 1 :math:`\times` 9) se corresponden con el
reordenamiento de la matriz en manera vectorial.

El *set* de máscaras de Frei-Chen pueden utilizarse para la detección de
bordes, identificando que, en virtud de constituir una autobase, un
subespacio arbitrario se asocia con “proyecciones” de la imagen (o
bloque) en el subespacio de interés.


Extensión de los operadores
---------------------------

Puede verse que uno de los problemas usuales en los métodos de detección
de bordes, como en general en cualquier técnica de procesamiento, es que
la presencia de señal espúrea como ruido, perjudica y limita
significativamente la capacidad y *performance* de los métodos de
procesamiento.

Un intento para reducir los efectos limitantes de la presencia de ruido
se basa en el concepto de “extensión de operadores”, que consiste en
implementar un procedimiento previo a aplicar operadores de detección de
bordes con el objeto conseguir una reducción del ruido en la señal.
Pero, en lugar de realizar procesos tipicos de filtrado de ruido, como
alguno de los descritos en el Capítulo `[CapII] <#CapII>`__, se propone
una “expansión” de los operadores de detección de bordes, que consiste
básicamente en aumentar la dimensión de la máscara correspondiente sin
alterar las propiedades de simetría y operación de dicha máscara.

A modo de ejemplo, la extensión o expansión del operador de Sobel sería:

.. math::

   \begin{aligned}
       %\begin{array}{ccccccc}
       \left[  \begin{array}{ccccccc}  -1 & -1 & -1  & -2 & -1 & -1 & -1\\  -1 & -1 & -1  & -2 & -1 & -1 & -1 \\
       -1 & -1 & -1  & -2 & -1 & -1 & -1 \\ 0 & 0 & 0  & 0 & 0 & 0 & 0 \\ 1 & 1 & 1  & 2 & 1 & 1 & 1 \\
       1 & 1 & 1  & 2 & 1 & 1 & 1 \\ 1 & 1 & 1  & 2 & 1 & 1 & 1
       \end{array} \right] %&
       %\end{array}    \right\}
   \label{EqAAG}\end{aligned}

El cálculo del gradiente por fila :math:`G_{X}` o por columna
:math:`G_{y}` se obtienen por correspondencia de rotaciones
:math:`\frac{\pi}{2}` del operador, en el ejemplo el de Sobel.

La extensión de los operadores, originalmente de 3 :math:`\times` 3
puede realizarse hacia cualquiera dimensión, aunque típicamente se
realiza para 11 :math:`\times` 11, 9 :math:`\times` 9 y 7 :math:`\times`
7.

El método de Canny: Algoritmo
-----------------------------

El operador de detección de bordes de Canny desarrollado durante los ’80
se basa en un algoritmo de múltiples fases capaz de detectar bordes de
diferentes características. Representa,de hecho, el operador más
utilizado en la detección de bordes.

El objetivo ideal del método propuesto por Canny consistía en hallar un
algoritmo óptimo para detectar bordes. [1]_ El concepto básico es que un
buen mecanismo de detección óptimo es aquel algoritmo capaz de marcar
tantos bordes reales como sea posible, una buena localización, y los
bordes marcados deben estar lo más cerca posible del borde en la imagen
real. Además, procurar que un borde dado debe ser marcado sólo una vez y
donde sea posible el ruido presente en la imagen no debería crear falsos
bordes.

La implementación del método de Canny permite optimizar la detección de
bordes diferenciales y consta de tres etapas principales: filtrado,
decisión inicial, e histéresis.

La primera etapa consiste en un filtrado de convolución de la derivada
primera de una función Gaussiana normalizada discreta sobre la imagen,
realizada en dos direcciones: horizontal y vertical. La función
Gaussiana posee dos parámetros fundamentales, valor medio :math:`M` y
desviación típica :math:`\sigma`. En este caso, el valor medio es nulo,
por lo tanto la ecuación que define el filtro Gaussiano :math:`G(x)` es:

.. math::

   \begin{aligned}
       G(x) = k \, \: e^\frac{-x^2}{2 \, \sigma^2}
   \label{EqAA}\end{aligned}

donde el parámetro :math:`k` se determina de manera que el máximo de
:math:`G(x)` sea la unidad en su versión discreta.

Para la realización del filtro utilizado en la primera etapa, se deriva
la expresión `[EqAA] <#EqAA>`__, obteniéndose:

.. math::

   \begin{aligned}
       \frac{d \, G(x)}{d \, x} = -\frac{k}{\sigma^2} \, \: x \, \; e^\frac{-x^2}{2 \, \sigma^2}
   \label{EqAB}\end{aligned}

La versión discreta del filtro se define de modo análogo y se considera
que :math:`x` asume valores en :math:`[-5 \sigma, 5 \sigma]` con
diferencias de 1 pixel entre muestras consecutivas.

obviamente, por razones de eficiencia de cómputo, es preferible derivar
directamente la versión discreta de `[EqAA] <#EqAA>`__, con el fin de
obtener el valor de :math:`k`.

.. [1]
   Véase, por ejemplo *Mammography image detection processing for
   automatic micro-calcification recognition* Quintana et al. y
   *Mammography image quality optimisation: a Monte Carlo study* Tirao
   et al. donde se encuentran ejemplos del cálculo y uso de operadores
   de Canny por medio de gradientes por fila y columna.
