import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.title('Multiple language abstracts')
with st.sidebar:
    st.subheader('Jorge P. Rodríguez, PhD') 
    image = Image.open('./pic.jpeg',"rb")
    st.write('pass')
    st.image(image,width=200)
    st.write('[Home](http://jorgeprodriguezg.github.io)')
    st.write('[Multiple language abstracts](https://jorgeprodriguezg-jorgeprodriguezg-github-io-mlamla-mq0osn.streamlitapp.com/)')
    st.write('[Data and code](http://jorgeprodriguezg.github.io/data_and_code.html)')
    st.write('[CV](https://jorgeprodriguezg.github.io/CV_May22.pdf)')
lans = ['English','Español','中文']
language = st.selectbox('Please select your language',lans)

L = lans.index(language)
if L == 0:
    st.write('Available abstracts in English')

    with st.expander("Comprehensive analytical approaches reveal species specific search strategies in sympatric apex predatory sharks"):
        st.write("Animals follow specific movement patterns and search strategies to maximize encounters with essential resources (e.g. prey, favourable habitat) while minimizing exposures to suboptimal conditions (e.g. competitors, predators). While describing spatiotemporal patterns in animal movement from tracking data is common, understanding the associated search strategies employed continues to be a key challenge in ecology. Moreover, studies in marine ecology commonly focus on singular aspects of species’ movements, however using multiple analytical approaches can further enable researchers to identify ecological phenomena and resolve fundamental ecological questions relating to movement. Here, we used a set of statistical physics-based methods to analyze satellite tracking data from three co-occurring apex predators (tiger, great hammerhead and bull sharks) that predominantly inhabit productive coastal regions of the northwest Atlantic Ocean and Gulf of Mexico. We analyzed data from 96 sharks and calculated a range of metrics, including each species’ displacements, turning angles, dispersion, space-use and community-wide movement patterns to characterize each species' movements and identify potential search strategies. Our comprehensive approach revealed high interspecific variability in shark movement patterns and search strategies. Tiger sharks displayed near-random movements consistent with a Brownian strategy commonly associated with movements through resource-rich habitats. Great hammerheads showed a mixed-movement strategy including Brownian and resident-type movements, suggesting adaptation to widespread and localized high resource availability. Bull sharks followed a resident movement strategy with restricted movements indicating localized high resource availability. We hypothesize that the species-specific search strategies identified here may help foster the co-existence of these sympatric apex predators. Following this comprehensive approach provided novel insights into spatial ecology and assisted with identifying unique movement and search strategies. Similar future studies of animal movement will help characterize movement patterns and also enable the identification of search strategies to help elucidate the ecological drivers of movement and to understand species’ responses to environmental change.")
        st.write("[More](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ecog.05953)")
        
    with st.expander("The global network of ports supporting high seas fishing"):
        st.write("Fisheries in waters beyond national jurisdiction (“high seas”) are difficult to monitor and manage. Their regulation for sustainability requires critical information on how fishing effort is distributed across fishing and landing areas, including possible border effects at the exclusive economic zone (EEZ) limits. We infer the global network linking harbors supporting fishing vessels to fishing areas in high seas from automatic identification system tracking data in 2014, observing a modular structure, with vessels departing from a given harbor fishing mostly in a single province. The top 16% of these harbors support 84% of fishing effort in high seas, with harbors in low- and middle-income countries ranked among the top supporters. Fishing effort concentrates along narrow strips attached to the boundaries of EEZs with productive fisheries, identifying a free-riding behavior that jeopardizes efforts by nations to sustainably manage their fisheries, perpetuating the tragedy of the commons affecting global fishery resources.")
        st.write("[More](https://www.science.org/doi/10.1126/sciadv.abe3470)")
        
    with st.expander("Design of deployment strategies to monitor the movement of animals with passive electronic devices"):
        st.write("Current animal monitoring systems have improved our knowledge of quantitative animal ecology. There are many electronic tracking technologies such as VHF/UHF telemetry, light-level geolocation, ARGOS satellite telemetry and GPS tracking. To reach the desired level of information retrieval requires the planning of adequate equipment effort and coverage, which depends on the properties of the system. We propose an equipment arrangement model consisting of a given number of receiver stations in a two-dimensional space in which the animals move according to a central place movement model. The objective is to characterize how the transmission of tracking data depends on the movement of the animals and the design of the equipment deployment: quantity and location of the receiver stations and their associated reception radius. We also implement the model using real trajectories of southern elephant seals and Australian sea lions publicly available online and tracked during the years 2010–2012. We characterize the data transmission based on different equipment configurations and we obtained analogous results to the theoretical model.")
        st.write("[More](https://doi.org/10.3390/s21020326)")
    
    with st.expander("Risk of secondary infection waves of COVID-19 in an insular region: the case of the Balearic Islands, Spain"):
        st.write("The Spanish government declared the lockdown on March 14th, 2020 to tackle the fast-spreading of COVID-19. As a consequence, the Balearic Islands remained almost fully isolated due to the closing of airports and ports, these isolation measures and the home-based confinement have led to a low prevalence of COVID-19 in this region. We propose a compartmental model for the spread of COVID-19 including five compartments (Susceptible, Exposed, Presymptomatic Infective, Diseased, and Recovered), and the mobility between municipalities. The model parameters are calibrated with the temporal series of confirmed cases provided by the Spanish Ministry of Health. After calibration, the proposed model captures the trend of the official confirmed cases before and after the lockdown. We show that the estimated number of cases depends strongly on the initial dates of the local outbreak onset and the number of imported cases before the lockdown. Our estimations indicate that the population has not reached the level of herd immunization necessary to prevent future outbreaks. While the low prevalence, in comparison to mainland Spain, has prevented the saturation of the health system, this low prevalence translates into low immunization rates, therefore facilitating the propagation of new outbreaks that could lead to secondary waves of COVID-19 in the region. These findings warn about scenarios regarding after-lockdown-policies and the risk of second outbreaks, emphasize the need for widespread testing, and could potentially be extrapolated to other insular and continental regions.")
        st.write("[More](https://doi.org/10.3389/fmed.2020.563455)")
        
    with st.expander("Overhauling ocean spatial planning to improve marine megafauna conservation"):
        st.write("Tracking data have led to evidence-based conservation of marine megafauna, but a disconnect remains between the many 1000s of individual animals that have been tracked and the use of these data in conservation and management actions. Furthermore, the focus of most conservation efforts is within Exclusive Economic Zones despite the ability of these species to move 1000s of kilometers across multiple national jurisdictions. To assist the goal of the United Nations General Assembly’s recent effort to negotiate a global treaty to conserve biodiversity on the high seas, we propose the development of a new frontier in dynamic marine spatial management. We argue that a global approach combining tracked movements of marine megafauna and human activities at-sea, and using existing and emerging technologies (e.g., through new tracking devices and big data approaches) can be applied to deliver near real-time diagnostics on existing risks and threats to mitigate global risks for marine megafauna. With technology developments over the next decade expected to catalyze the potential to survey marine animals and human activities in ever more detail and at global scales, the development of dynamic predictive tools based on near real-time tracking and environmental data will become crucial to address increasing risks. Such global tools for dynamic spatial and temporal management will, however, require extensive synoptic data updates and will be dependent on a shift to a culture of data sharing and open access. We propose a global mechanism to store and make such data available in near real-time, enabling a holistic view of space use by marine megafauna and humans that would significantly accelerate efforts to mitigate impacts and improve conservation and management of marine megafauna.")
        st.write("[More](https://doi.org/10.3389/fmars.2019.00639)")
        
    with st.expander("Particle velocity controls phase transitions in contagion dynamics"):
        st.write("Interactions often require the proximity between particles. The movement of particles, thus, drives the change of the neighbors which are located in their proximity, leading to a sequence of interactions. In pathogenic contagion, infections occur through proximal interactions, but at the same time, the movement facilitates the co-location of different strains. We analyze how the particle velocity impacts on the phase transitions on the contagion process of both a single infection and two cooperative infections. First, we identify an optimal velocity (close to half of the interaction range normalized by the recovery time) associated with the largest epidemic threshold, such that decreasing the velocity below the optimal value leads to larger outbreaks. Second, in the cooperative case, the system displays a continuous transition for low velocities, which becomes discontinuous for velocities of the order of three times the optimal velocity. Finally, we describe these characteristic regimes and explain the mechanisms driving the dynamics.")
        st.write("[More](https://www.nature.com/articles/s41598-019-42871-x)")
        
    with st.expander("Deciphering the interdependence between ecological and evolutionary networks"):
        st.write("Biological systems consist of elements that interact within and across hierarchical levels. For example, interactions among genes determine traits of individuals, competitive and cooperative interactions among individuals influence population dynamics, and interactions among species affect the dynamics of communities and ecosystem processes. Such systems can be represented as hierarchical networks, but can have complex dynamics when interdependencies among levels of the hierarchy occur. We propose integrating ecological and evolutionary processes in hierarchical networks to explore interdependencies in biological systems. We connect gene networks underlying predator–prey trait distributions to food webs. Our approach addresses longstanding questions about how complex traits and intraspecific trait variation affect the interdependencies among biological levels and the stability of meta-ecosystems.")
        st.write("[More](https://doi.org/10.1016/j.tree.2018.04.009)")
        
    with st.expander("Convergence of marine megafauna movement patterns in coastal and open oceans"):
        st.write("The extent of increasing anthropogenic impacts on large marine vertebrates partly depends on the animals’ movement patterns. Effective conservation requires identification of the key drivers of movement including intrinsic properties and extrinsic constraints associated with the dynamic nature of the environments the animals inhabit. However, the relative importance of intrinsic versus extrinsic factors remains elusive. We analyze a global dataset of ∼2.8 million locations from >2,600 tracked individuals across 50 marine vertebrates evolutionarily separated by millions of years and using different locomotion modes (fly, swim, walk/paddle). Strikingly, movement patterns show a remarkable convergence, being strongly conserved across species and independent of body length and mass, despite these traits ranging over 10 orders of magnitude among the species studied. This represents a fundamental difference between marine and terrestrial vertebrates not previously identified, likely linked to the reduced costs of locomotion in water. Movement patterns were primarily explained by the interaction between species-specific traits and the habitat(s) they move through, resulting in complex movement patterns when moving close to coasts compared with more predictable patterns when moving in open oceans. This distinct difference may be associated with greater complexity within coastal microhabitats, highlighting a critical role of preferred habitat in shaping marine vertebrate global movements. Efforts to develop understanding of the characteristics of vertebrate movement should consider the habitat(s) through which they move to identify how movement patterns will alter with forecasted severe ocean changes, such as reduced Arctic sea ice cover, sea level rise, and declining oxygen content.")
        st.write("[More](https://doi.org/10.1073/pnas.1716137115)")
        
    with st.expander("Diversity of hysteresis in a fully cooperative coinfection model"):
        st.write("We propose a fully cooperative coinfection model in which singly infected individuals are more likely to acquire a second disease than susceptible ones and doubly infected individuals are also assumed to be more contagious than singly infected ones. The dynamics of such a fully cooperative coinfection model is investigated through the well-mixed approach. In particular, discontinuous outbreak transitions from the disease free state or the low prevalence state to the high prevalence state can be separately observed as a disease transmission rate crosses a threshold α<sub>o</sub> from the below when the epidemic is still in the early stages. Moreover, discontinuous eradications from the high prevalence state to the low prevalence or disease free state are also separately seen as the transmission rate reaches a threshold α<sub>e</sub>(<α<sub>o</sub>) from the above when the outbreak occurs. Such phenomena constitute three types of hysteresis, where only one type has been identified before. Complete characterization of these three types of hysteresis in terms of parameters measuring the uniformity of the model is both analytically and numerically provided.",unsafe_allow_html=True)
        st.write("[More](https://doi.org/10.1063/1.4996807)")
        
    with st.expander("Risk of coinfection outbreaks in temporal networks: a case study of a hospital contact network"):
        st.write("We study the spreading of cooperative infections in an empirical temporal network of contacts between people, including health care workers and patients, in a hospital. The system exhibits a phase transition leading to one or several endemic branches, depending on the connectivity pattern and the temporal correlations. There are two endemic branches in the original setting and the non-cooperative case. However, the cooperative interaction between infections reinforces the upper branch, leading to a smaller epidemic threshold and a higher probability for having a big outbreak. We show the microscopic mechanisms leading to these differences, characterize three different risks, and use the influenza features as an example for this dynamics.")
        st.write("[More](https://doi.org/10.3389/fphy.2017.00046)")
        
    with st.expander("Big data analyses reveal patterns and drivers of the movements of southern elephant seals"):
        st.write("The growing number of large databases of animal tracking provides an opportunity for analyses of movement patterns at the scales of populations and even species. We used analytical approaches, developed to cope with “big data”, that require no ‘a priori’ assumptions about the behaviour of the target agents, to analyse a pooled tracking dataset of 272 elephant seals (Mirounga leonina) in the Southern Ocean, that was comprised of >500,000 location estimates collected over more than a decade. Our analyses showed that the displacements of these seals were described by a truncated power law distribution across several spatial and temporal scales, with a clear signature of directed movement. This pattern was evident when analysing the aggregated tracks despite a wide diversity of individual trajectories. We also identified marine provinces that described the migratory and foraging habitats of these seals. Our analysis provides evidence for the presence of intrinsic drivers of movement, such as memory, that cannot be detected using common models of movement behaviour. These results highlight the potential for “big data” techniques to provide new insights into movement behaviour when applied to large datasets of animal tracking.")
        st.write("[More](https://www.nature.com/articles/s41598-017-00165-0)")
        

if L == 1:
    st.write('Resúmenes disponibles en español')
    
    with st.expander("Comprehensive analytical approaches reveal species specific search strategies in sympatric apex predatory sharks"):
        st.write("Los animales siguen patrons específicos de movimiento y estrategias de búsqueda para maximizar el hallazgo de recursos esenciales (e.g., presas, hábitats favorables), mientras que minimizan la exposición a condiciones subóptimas (e.g., competidores, depredadores). Mientras describir los patrones espacio-temporales del movimiento animal con datos de seguimiento es común, entener las estrategias de búsqueda asociadas a ellos continúa siendo un desafío en la ecología. Además, los estudios de ecología marina se centran frecuentemente en aspectos específicos del movimiento de las especies, de tal forma que usar múltiples enfoques analíticos puede aumentar los recursos de los investigadores para identificar los fenómenos ecológicos y resolver preguntas ecológicas fundamentales relacionadas con el movimiento. En este trabajo, nosotros utilizamos un conjunto de métodos basados en la física estadística para analizar datos satelitales de seguimiento de tres depredadores que coexisten (los tiburones tigre, martillo gigante y toro) que habitan mayoritariamente en las zonas productivas coasteras del noroeste del océano Atlático y el golfo de México. Analizamos datos de 96 tiburones y calculamos varias medidas, incluyendo para cada especie los desplazamientos, los ángulos de giro, la dispersión, el uso del espacio y los movimientos de patrón entre comunidades espaciales para cadacterizar los movimientos de cada especie y las estrategias de búsqueda. Los tiburones tigre desplegaron movimientos casi aleatorios compatibles con una estrategia Browniana comúnmente asociada con movimientos a través de hábitats ricos en recursos. Los gigantes martillo mostraron una estrategia de movimiento mixta incluyendo movimientos Brownianos y de tipo residente, sugiriendo la adaptación a la disponibilidad de recursos tanto extensos como localizados. Los tiburones toro siguieron una estrategia de movimiento residente como movimientos restringidos indicando la alta disponibilidad de recursos localizados. Nosotros planteamos la hipótesis de que estas estrategias de búsqueda específicas para cada especie que identificamos aquí pueden facilitar la coexistencia de estos depredadores simpátricos. El seguimiento de este planteamiento comprensivo proporcionó nuevas ideas de la ecología espacial y ayudó a identificar estrategias de movimiento y búsqueda únicas. Estudios futuros similares del movimiento animal ayudarán a caracterizar los patrones de movimiento y también facilitarán la identificación de estrategias de búsqueda para clarificar los factores condicionantes del movimiento y entender las respuestas de las especies al cambio medioambiental.")

    with st.expander("The global network of ports supporting high seas fishing"):
        st.write("Las zonas de pesca en aguas fuera de jurisdicción nacional son difíciles de monitorear y administrar. Su regulación para la sostenibilidad requiere información crítica sobre cómo se distribuye el esfuerzo pesquero entre las zonas de pesca y de desembarco, incluyendo los posibles efectos de frontera en los límites de las Zonas Económicas Exclusivas (ZEE). Inferimos la red global conectando los puertos que dan apoyo a los barcos de pesca en aguas internacionales de los datos de seguimiento del sistema de identificación automática en 2014, observando una estructura modular, con los barcos procedentes de un puerto pescando mayoritariamente en una única provincia. El 16% de los puertos más frecuentados presta apoyo al 84% del esfuerzo pesquero en aguas internacionales, con los puertos de países de ingresos medios y bajos situados entre los mayores apoyos. El esfuerzo pesquero se concentra a lo largo de pequeñas bandas adjuntas a las fronteras de las ZEEs con zonas de pesca productivas, identificando un libre comportamiento que perjudica a los esfuerzos de las naciones para administrar sus zonas de pesca de forma sostenible, perpetuando la tragedia de los comunes que afecta a los recursos globales de pesca")
        st.write("[More](https://www.science.org/doi/10.1126/sciadv.abe3470)")
    
    with st.expander("Design of deployment strategies to monitor the movement of animals with passive electronic devices"):
        st.write("Los actuales sistemas de monitoreo de animales han mejorado nuestro conocimiento en la ecología cuantitativa de los animales. Hay muchas tecnologías de seguimiento como telemetría VHF/UHF, geolocalización por intensidad de luz, telemetría satelital ARGOS y seguimiento por GPS. Para alcanzar el nivel deseado de información, la recolección de los datos requiere planear el esfuerzo adecuado de equipamiento y la cobertura, que depende de las propiedades del sistema. Proponemos un modelo de disposición de equipamiento que consiste en un determinado número de estaciones receptoras en un espacio bidimensional en el que los animales se mueven de acuerdo con el modelo de movimiento alrededor de un lugar central. El objetivo es caracterizar cómo la transmisión de los latos de localización depende en el movimiento de los animales y el diseño de la disposición del equipamiento: la cantidad y la localización de las estaciones receptoras y su radio de recepción asociado. También implementamos nuestro modelo utilizando trayectorias reales de elefantes marinos del sur y leones marinos australianos, disponibles públicamente, y localizados durante los años 2010-2012. Caracterizamos la transmisión de datos basados en diferentes configuraciones del equipamiento y obtenemos resultados análogos a los del modelo teórico.")
        st.write("[Más información](https://doi.org/10.3390/s21020326)")
    
    with st.expander("Risk of secondary infection waves of COVID-19 in an insular region: the case of the Balearic Islands, Spain"):
        st.write("El gobierno español declaró un confinamiento el 14 de marzo de 2020 para afrontar la rápida propagación de la COVID-19. Como consecuencia de ello, las islas Baleares permanecieron casi totalmente aisladas debido al cierre de puertos y aeropuertos, con estas medidas de aislamiento junto al confinamiento en hogares conducioendo a una baja prevalencia de COVID-19 en esta región. Proponemos un modelo compartimental para la propagación de la COVID-19 incluyendo cinco compartimentos (Susceptible, Expuesto, Infectivo Presintomático, Enfermo y Recuperado), y la movilidad entre municipios. Los parámetros del modelo son calibrados utilizando las series temporales de casos confirmados proporcionadas por el Ministerio de Sanidad de España. Después del calibrado, el modelo propuesto captura la tendencia del número de casos oficiales antes y después del confinamiento. Mostramos que el número de casos estimado depende fuertemente de la fecha de inicio del brote local y el número de casos importados antes del confinamiento. Nuestras estimaciones indican que la población no ha alcanzado el nivel de inmunidad de rebaño necesario para prevenir futuros brotes. Mientras que la baja prevalencia, en comparación con la España peninsular, ha prevenido la saturación del sistema sanitario, esta baja prevalencia se traduce en bajas tasas de inmunización, facilitando entonces la propagación de nuevos brotes que podrían conducir a olas secundarias de COVID-19 en la región. Estos resultados nos alertan de posibles escenarios con respecto a intervenciones post-confinamiento y el riesgo de brotes secundarios, enfatizando la necesidad de la realización de tests masivos, que podrían ser potencialmente extrapolados a otras regiones insulares y continentales.")
        st.write("[Más información](https://doi.org/10.3389/fmed.2020.563455)")
        
    with st.expander("Overhauling ocean spatial planning to improve marine megafauna conservation"):
        st.write("Los datos de seguimiento han favorecido la conservación basada en evidencias de la megafauna marina, pero hay una brecha que todavía separa los miles de individuos animales que se han seguido y el uso de esos datos en acciones de conservación y administración. Además, la atención de la mayoría de los esfuerzos de conservación se centra en las Zonas Económicas Exclusivas aunque estas especies pueden moverse miles de kilómetros a lo largo de múltiples zonas de jurisdicción nacional. En ayuda al reciente esfuerzo de la Asamble General de las Naciones Unidas para negociar un tratado global para la conservación de la biodiversidad en alta mar, proponemos el desarrollo de una nueva estrategia para la administración espacial marina. Argumentamos que una propuesta que combine los movimientos rastreados de la megafauna marina y las actividades humanas en el mar, y use actuales y nuevas tecnologías (e.g., a través de nuevos dispositivos de seguimiento y técnicas de big data) puede ser aplicada para proporcionar diagnósticos en tiempo casi real sobre los riesgos existentes y las amenazas para mitigar los riesgos globales de la megafauna marina. Dado que se espera que los desarrollos tecnológicos de la próxima decada catalicen el potencial para inspeccionar a los animales marinos y las actividades humanas con incluso más detalle y a escalas globales, el desarrollo de herramientas dinámicas de predicción basadas en el seguimiento a tiempo casi real y los datos medioambientales será clave para afrontar riesgos crecientes. Estas herramientas globales para la administración dinámica en el espacio y el tiempo, sin embargo, requerirán actualizaciones sinópticas y extensivas en tiempo casi real, facilitando un punto de vista holístico del uso del espacio por la megafauna marina y los humanos que aceleraría de forma sustancial los esfuerzos para mitigar los impactos y mejorar la conservación y la administración de la megafauna marina.")
        st.write("[Más información](https://doi.org/10.3389/fmars.2019.00639)")
        
    with st.expander("Particle velocity controls phase transitions in contagion dynamics"):
        st.write("Las interacciones tienen como requisito típicamente la proximidad entre las partículas. El movimiento de las partículas, entonces, controla el cambio de vecinos que se sitúan en sus proximidades, creando una secuencia de interacciones. En el contagio patogénico, las infecciones ocurren a través de interacciones de proximidad pero, a la vez, el movimiento facilita la ubicación simultánea de diferentes cepas. Analizamos cómo la velocidad de las partículas influye en las transiciones de fase en los procesos de contagio de tanto una única infección como de dos infecciones que cooperan. En primer lugar, identificamos una velocidad óptima (cerca de la mitad del rango de interacción normalizada por el tiempo de recuperación) asociada con el umbral epidémico mayor, de tal forma que disminuir la velocidad por debajo del valor óptimo conduce a broter mayores. En segundo lugar, en el caso cooperativo, el sistema muestra una transición de fase continua para bajas velocidades, que se convierte en discontinua para velocidades del orden de magnitud de tres veces la velocidad óptima. Finalmente, describimos estos regímenes característicos y explicamos los mecanismos que controlan la dinámica.")
        st.write("[Más información](https://www.nature.com/articles/s41598-019-42871-x)")
    
    with st.expander("Deciphering the interdependence between ecological and evolutionary networks"):
        st.write("Los sistemas biológicos están compuestos por elementos que interactúan dentro y a través de niveles jerárquicos. Por ejemplo, las interacciones entre los genes determinan los rasgos de los individuos, las interacciones cooperativas y competitivas entre individuos influyen en la dinámica de poblaciones, y las interacciones entre especies modifican la dinámica de comunidades y los procesos de los ecosistemas. Sistemas como éstos se pueden representar como redes jerárquicas, pero pueden tener complejas dinámicas cuando hay interdependencias entre niveles jerárquicos. Proponemos integrar los procesos ecológicos y evolucionarios en redes jerárquicas para explorar las interdependencias de los sistemas biológicos. Conectamos redes genéticas subyacentes de los rasgos de depredadores y presas con redes tróficas. Nuestro enfoque aborda preguntas recurrentes sobre cómo los rasgos complejos y la variación de rasgos intraespecífica influyen en las interdependencias entre niveles biológicos y la estabilidad de meta-ecosistemas.")
        st.write("[Más información](https://doi.org/10.1016/j.tree.2018.04.009)")
        
    with st.expander("Convergence of marine megafauna movement patterns in coastal and open oceans"):
        st.write("El alcance de los crecientes impactos antropogénicos en grandes vertebrados marinos depende parcialmente de los patrones de movimiento de los animales. Una conservación efectiva necesita la identificación de los controladores clave del movimiento incluyendo propiedades internas y ligaduras externas asociadas con la naturaleza dinámica de los entornos habitados por los animales. Sin embargo, la importancia relativa de los factores internos y externos no está caracterizada todavía. Analizamos un conjunto de datos global de ∼2.8 millones de localizaciones de >2600 individuos marcados de 50 vertebrados marinos separados evolucionalmente por millones de años y que utilizan distintos medios de locomoción (vuelan, nadan, caminan). Sorprendentemente, los patrones de movimiento muestran una convergencia destacable, permanenciendo estables entre espedies e independientemente de la masa o el tamaño corporal, aunque estas características se expanden a lo largo de más de 10 órdenes de magnitud entre las especies estudiadas. Esto representa una diferencia fundamental entre los vertebrados marinos y terrestres que no se ha identificado antes, probablemente relacionada con los costes de locomoción reducidos en el agua. Los patrones de movimiento se explican fundamentalmente por las características específicas de las especies y los hábitats por los que se desplazan, de forma que el movimiento es complejo cuando se mueven cerca de la costa comparado con patrones más previsibles cuando lo hacen en océanos abiertos. Esta diferencia puede estar asociada con una mayor complejidad en los microhábitats costeros, destacando el papel crítico del hábitat preferido para determinar los movimientos globales de los vertebrados marinos. Los esfuerzos para desarrollar el conocimiento de las características del movimiento vertebrado deberían considerar el habitat a través del que se mueven para identificar cómo los patrones de movimiento cambiarán con océanos previsiblemente más severos, como una reducida capa de hielo ártico el aumento del nivel del mar o la disminución del contenido de oxígeno.")
        st.write("[Más información](https://doi.org/10.1073/pnas.1716137115)")

    with st.expander("Diversity of hysteresis in a fully cooperative coinfection model"):
        st.write("Proponemos un modelo de coinfección totalmente cooperativa en el que los individuos infectados con una enfermedad son más propensos a adquirir una segunda enfermedad que los susceptibles y los individuos infectados con dos enfermedades son considerados como más infectivos que los infectados con una. La dinámica de este modelo de coinfección totalmente cooperativa se investiga a través de una aproximación de buena mezcla. En concreto, transiciones epidémicas discontinuas desde el estado libre de infección o de baja prevalencia al estado de alta prevalencia pueden observarse de forma independiente cuando la tasas de tranmisión de la enfermedad cruza un umbral α<sub>o</sub> desde abajo cuando la epidemica está todavía en un estado temprano. Además, supresiones discontinuas desde el estado de alta prevalencia al de baja prevalencia o libre de enfermedad se observan de forma separada cuando la tasa de transmisión alcanza un umbral α<sub>e</sub>(<α<sub>o</sub>) desde arriba cuando ocurre el brote. Estos fenómenos se resumen en tres tipos de histéresis, donde solo uno de ellos se ha identificado antes. Aquí, caracterizamos de forma completa estos tres tipos de histéresis en términos de parámetros que miden la uniformidad del modelo de forma analítica y numérica.",allow_unsafe_html=True)
        st.write("[Más información](https://doi.org/10.1063/1.4996807)")
        
    with st.expander("Risk of coinfection outbreaks in temporal networks: a case study of a hospital contact network"):
        st.write("Estudiamos la propagación de infecciones cooperativas en una red temporal empírica de contactos entre personas, incluyendo trabajadores sanitarios y pacientes en un hospital. El sistema muestra una transición de fase que conduce a una o dos ramas, dependiendo del patrón de conectividad y de las correlaciones temporales. Hay dos ramas endémicas en el caso cooperativo y en el no cooperativo. Sin embargo, la interacción cooperativa entre las infecciones refuerza la rama superior, conduciendo a un umbral epidémico menor y a una mayor probabilidad de tener un gran brote. Mostramos los mecanismos microscópicos que conducen a estas diferencias, carazatizamos tres riesgos diferentes y usamos las caracterísiticas de la gripe como un ejemplo de esta dinámica.")
        st.write("[Más información](https://doi.org/10.3389/fphy.2017.00046)")
        
    with st.expander("Big data analyses reveal patterns and drivers of the movements of southern elephant seals"):
        st.write("El creciente número de bases de datos masivas sobre seguimiento de animales representa una oportunidad para el análisis de los patrones de movimiento a las escalas de poblaciones e incluso especies. Hemos utilizado métodos analíticos, desarrollados para analizar datos masivos, que no implican hipótesis ‘a priori’ sobre el comportamiento de los agentes, para analizar un conjunto de datos agregado de 272 elefantes marinos (Mirounga leonina) en el océano del Sur, compuesto por > 500,000 estimaciones de localizaciones obtenidas a lo largo de más de una década. Nuestros análisis muestran que los desplazamientos de estas focas se describen por una ley de potencias truncada a lo largo de varias escalas espaciales y temporales, con indicios de un movimiento dirigido. Este patrón es evidente cuando analizamos trayectorias agregadas, pese a la amplia variedad de trayectorias individuales. Tambien identificamos las provincias marinas que describen los hábitats migratorio y de búsqueda de estas focas. Nuestro análisis proporciona evidencias de la presencia de controladores internos del movimiento, como la memoria, que no pueden ser detectados mediante el uso de los frecuentes modelos de comportamiento en el movimiento. Estos resultados resaltan el potencial de las técnicas de ‘big data’ para proporcionar nuevas ideas sobre el comportamiento en el movimiento cuando se aplican a conjuntos de datos masivos sobre seguimiento de animales.")
        st.write("[Más información](https://www.nature.com/articles/s41598-017-00165-0)")



if L == 2:
    st.write('Available abstracts in Chinese Mandarin')
    with st.expander("Big data analyses reveal patterns and drivers of the movements of southern elephant seals"):
        st.write("追蹤動物在資料庫中的數據成長提供了一個機會，用於分析群體遷移模式甚至能用於整個物種。我們使用分析法開發處理\"大數據\"，不需要對目標代理的行為假設進行\"a priori\"；分析南大洋272隻海豹 (Mirounga leonina)匯總追蹤數據，此數據集是由十多年來超過500,000個位置估計值組成。我們的分析上顯示，這些海豹的移動是透過幾個空間和時間尺度上的截斷冪律分佈來描述的，具有明確的方向移動特徵。這個模式是個證據，當分析聚合軌跡時儘管個體的軌跡多種多樣。我們還確認了海洋區域，描述這些海豹遷徙和覓食棲息地。我們的分析為移動的內在驅動因素（例如記憶）的存在提供了證據，這是使用常見的移動行為模型無法檢測到的。這些結果凸顯了“大數據”技術在應用於大型動物追蹤數據集時為移動行為提供新見解的潛在性。")
        st.write("[More](https://www.nature.com/articles/s41598-017-00165-0)")
