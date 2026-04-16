<img src="https://upload.wikimedia.org/wikipedia/commons/1/10/Columbia_University_1754.svg" width="400" valign="left">

# Finite Element Analysis: Bending of a Concrete Beam with Holes

## Descripción del Proyecto
[cite_start]Este proyecto analiza el comportamiento de dos diseños de vigas de hormigón en voladizo con diferentes formas de huecos bajo una carga uniforme[cite: 316]. [cite_start]El objetivo principal es evaluar y comparar la deformación y la distribución de esfuerzos utilizando el método de elementos finitos[cite: 44, 343].

Los dos diseños analizados son:
* [cite_start]**Diseño 1:** Viga con dos huecos circulares[cite: 13].
* [cite_start]**Diseño 2:** Viga con dos huecos cuadrados rotados[cite: 13].

## Metodología
[cite_start]El análisis computacional se llevó a cabo utilizando el software de simulación Abaqus[cite: 59]. 
* [cite_start]**Elementos:** Se utilizaron elementos triangulares de 3 nodos bajo condiciones de tensión plana[cite: 60].
* [cite_start]**Mallado:** Se ejecutaron modelos con dos densidades de malla diferentes (una malla gruesa de ~1120 elementos y una malla fina de ~2000 elementos) para evaluar la convergencia y precisión de los resultados[cite: 61, 62].
* [cite_start]**Validación:** Los resultados de los esfuerzos axiales ($\sigma_{xx}$) se compararon con los resultados teóricos calculados mediante la teoría de vigas de Euler-Bernoulli[cite: 63, 310].

## Resultados Destacados
* [cite_start]**Desplazamiento:** Ambas vigas mostraron una respuesta global similar, presentando los mayores desplazamientos en el extremo libre[cite: 317]. [cite_start]La viga con huecos circulares mostró deflexiones ligeramente mayores, indicando una menor rigidez para ese diseño[cite: 318].
* [cite_start]**Esfuerzos de Von Mises:** La concentración de esfuerzos más alta se produjo cerca de los soportes fijos, donde la flexión es mayor[cite: 319]. [cite_start]La diferencia de esfuerzo máximo entre los agujeros circulares y cuadrados fue mínima, lo que indica que la carga global gobernó la distribución más que la forma del agujero[cite: 302].
* [cite_start]**Refinamiento de Malla:** La comparación demostró que la malla fina capturó de manera mucho más precisa los gradientes de esfuerzo agudos y las concentraciones locales alrededor de los huecos, algo que las ecuaciones clásicas y la malla gruesa tienden a suavizar[cite: 325, 326].

## Contexto Académico
[cite_start]Este proyecto fue desarrollado para el curso *ENMEE3332 - Finite Elements* en la Universidad de Columbia (Otoño 2025)[cite: 8, 332].
