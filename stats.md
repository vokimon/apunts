Descriptive statistics
- Cuando hay muchos datos y quieres simplificarla o extraer significado
- Media, Varianza...

Inferencial statistics:
- Cuando no puedes comprobar todos los datos y tomas una muestra para extrapolar
- Incluyen un margen de error

Central tendency measures:

- Expectation: 

- Mean: sum(x)/len(x)
- Normal: Simetrical distribution with a maximum in the average and symetrical 
- Distribution: How often a value occurs in a data set (frequency)
- Outliers: Data que se separa demasiado del rato, distorsionan la media

- Median: Valor que queda en el centro de los valores ordenados
	- Quartile: Divide the sample on 4, like the median divides in 2
- Mode: Valor que aparece mas en el data set
	- Bi/Multimodal: en la distribución de frecuencias hay mas de un pico
	- Funciona con valores no numéricos

Media y median son la misma son identicas dicen que la distribucion es simetrica
Skew: en uno de los lados hay valores extremos


Spread measures:

How much data diverges from the central tendency

- Range: distance between the extreme values
- Interquartile Range (IQR): Distance between extremes of the middle 50% of your data
	Divide in quartiles (4 parts) and take the two middle ones
- Variance 
- Deviation: separation of a data from the mean
- Squared deviation
- Standard deviation: square root of the Variance (en unidades del dominio, no el cuadrado)

## Data visualization

Quantitive data: 
- Consisten spacing

Categorical data:

Frequency table: How many data fits the category
Relative frequency: How many data fits the category over the total (percent)

Bar chart: Proportional bar height to the frequencies


Pictograms: objects number or size proportional to the data

Ojo con los radios, las superficies y lo ancho

Binning: agrupar datos quantitativos en intervalos (bins/compartimentos) que seran las categorias
Los compartimentos pueden no ser equidistantes
Aunque ello puede estar justificado (juntar la gente mayor de 70 años, o que compra mas de 4l de aceite a la semana), tambien se puede usar para enmascarar datos.

Histogram: Representacion en barras de un intervalo continuo haciendo binning

- Steam and leaf plot: separar los digitos 

- Box plot or  Box and wisker plot:
	- A splitted box shows the mean and the main quartiles.
	- The wisker
	- Outliers may be displayed as x outside the wisker

- Cumulative frequency graph
	- La integral de la frequencia
	- Es mejor para representar pregutnas de menos que...

## Data distribution

El infinitesimal de un histograma cuando los bins se hacen pequeños

Normal distribution:
- Mean media and mode are the same  -> simetrical
- Defined by the mean and the stddev

Uniform distribution:
- Every possible value has the same probability


## Correlations

Looking for relationships between two variables.

Bivariate data: relationship between two variables

Scatter plot: Visualizating two variables for each case as plots

Allows to see clusters, tendencies...


Regression line: is the line that minimizes the distance of the averall points

Regression coefficient: Y = mX + b


Correlatiation: The points relates
- Positive the increment of one variable

Correlation may often is due by causality,
but VERY IMPORTANT, correlation may be due to:

- A couses B
- B causes A
- third cause causes A and B
- No causal relation, just random

Squared correlation (r^2): How much of the variance of one variable can be explained by the other variable

## Controlled experiments

- Simulation:
	- 
- Experiment
	- Taking cases from the real world and using 
- Randomize block design: 


- Selection Bias: Distortion of the results because how the sample is selected
	- Sampling bias: The sampled population cannot be generalized to the rest of the population
		- ie: Calls to random land phones tends to select mature people homesa
		- ie: Asking for polling at the exit of the train station
	- Interval bias: 
	- Volunteer bias: Because the sample is volunteers this 
- Allocation Bias: Distortion of the results because how the control and experimental groups are selected
	- Allocation concealment or blinding:  

Still the groups could be uneven -> Replication

Placebo: Just the action of taking a pill could make the person feel better

- Single blind study: Researchers knows the control groups, but the patients don't to avoid placebo
- Double blind study: Prevents the researchers unconciously affect the subjects differently

- Twins experiments: Twins represent the same genetic background (not non-genetic)
- Repeated measures design: Different treatments With the same subject one after another


## Surveys

Non experimental way of getting statistical information

Leading questions: 
Biased questions:
Non-response bias: People who are not responding 
Voluntary response bias: People who response tend to be very positive or very negative

Cooking: 

Cluster sampling: Select a random cluster of population, not individually (classrooms, medical centers...)

Snowball sampling: The subjects are used to find more people of interest they might know
	Useful to locate small target groups.

Census: A survey of the entire population. Minimizes sampling error, and used as a benchmarch for later surveys.

- Biased polls
- Badly worded polls
- Fake pools

## Science Journalism

When the study headline is catchy few journalism asks for the quality of the study.

- _Beer/Chocolate/... is good for your health_

- _Significant_ does not mean important in statistics, but noticeable

Cuando leas science journalism

- Who wrote the article
- Who published the article
- Who made the study
- Who funded the study

Foundations are funded.

Journalist are under presure to catch your attention

Non representative results:

- Reports on mice extrapolated to humans
- Petry dish studies: substances cannot be applied as directly to inner cells by ingestion or similar, and it could be dangerous

Journals mentioning "Scientists have found...", "A new study says...", go to the source

## Ethicals of data collection

Nuremberg Code:

- Informed consent:
	- Provide information in a comprehensive level to the target
	- Not coerced in any way
- Good for the society
- Basado en trabajo previo en laboratorio, con animales
- Diseñado para evitar daños físicos y psicologicos innecesarios
- Que no se pueda pensar a priori que conducira a la muerte o a daños permanentes (excepto si el sujeto es el propio experimentador!??)
- El riesgo no puede exceder del beneficio humanitario que se extraiga (como lo comparas?)
- Infrastructura establecida para minimizar los posibles daños
- Personal cualificado cientificamente y en cuidados
- Libertad de salirse del experimento en cualquier momento (limitado a que su estado mental o fisico haya empeorado?)
- Researchers should end the experiments if at any moment they foresee it will end in injury death or disability

Se redactó a raiz de los juicios de Nuremberg a los nazis.


New digital contexts not that regulated.


## Probability

Empirical probability: Occurrence in actual data

Theoretical probability: Hidden true we cannot directly see

Empirical probability is a good estimation of 

Exclusive events: P(a & b) = 0
Addition rule: When events are exclusive P(a | b) = P(a) + P(b)
When not exclusive P(a or b) = P(a) + P(b) - P(a and b)
we dicount the overlaping area of the wen diagram.

Independent Events: Their occurence of one event is not affected by the occurence of the other

Multiplication rule: For independent events P(a and b) = P(a) P(b)

When they are not independents, means that conditional probability is different than the regular probability

Conditional probability P(a|b): The probability of a given that b is happens

P(a and b) = P(b) P(a|b) -> P(a|b) = P(a and b) / P(b)

They are not reciprocal.

P(b|a) = P(a and b) / P(a)

P(b|a) P(a) = P(a|b) P(b) Theorem of Bayes

Base Rate: Probability in the population
Sensitivity: True positives
Specificity: True negatives

## Binomial statistics

Binomial distribution:
Given n repeated independent experiments
chance to get k occurences of an event of probability p.

Probability of a given combination (ie: FTTFF)

P(a*k of N) = P(a)^k P(not a)^(n-k)

Binomial coefficent:
how many ordering combinations of k occurences out of N cases

nCk = n! /( (n-k)! k!) = (

binomial(n,k) = nCk P(a*k of N)


Bernoulli distribution (binomial para n = 1 y k in (0,1))




## Geometric distributions

Geometric distribution: La probabilitat que el primer caso se dé en el experimento k

geom(k;p) = p (1-p)^k


Cumulative geometric distributions: Useful to tell how much we should wait to get a result

acumgeom(k;p) sum(geom(i;p) for i in range(k))

Cumulative results may have anti-intuitive results:

- Shared birthday paradox: almost assured with 30 persons
- Lottery tickets: 15M tickets on average


# Randomness

Expected value of a sample the mean

First Moment / Mean

Multiply each value by its frequency in the sample

integral ( f(x)*x )

Second Moment / Variance:
the expectation of the difference to the first moment
E(x-Mean)

Third Moment / Skewness:
How data frequency is more extreme on higher (positive) or lower values (negative)
E (x-Mean)^3

Fourth Moment / Kurtosis
How thick the tails are 
E (x-Mean)^4

# Z-score

El z-score es una canonicalización de una función normal
para que puedan ser comparada con valores de otra distribución normal.
Se le resta la media y se divide por la desviacion standard.
La media queda en 0 y la desviación estandard en +1 y -1.

Percentile: what percent of the population is lower value than a given value of a distribution.

Percentile tables of z-distributions
(Accumulated z-score)

zscore | percentile|
--:|--:|
-3ð | 0.13%
-2ð | 2.27%
-1ð | 15.9%
 0ð | 50.0%
+1ð | 84.1&
+2ð | 97.7%
+3ð | 99.87%


## Normal distributions

Same value mean, mode and median
Skewness 0

Given a population with a variable following a distribution with a finite variance,
the distribution of the means of random samples of the population
tends to be a normal distribution, whatever the original population ditribution,
on increasing sample size.

Central Limit Theorem:
The distribution of sample means for an independent random variable
will get closer and closer to a normal distribution as the size of the sample
gets bigger and bigger, even if the original population distribution isn't normal itself.

The mean of the sample distribution is also getting closer to the population mean
as we increase the sample.


Standard Error (of the mean): 
The standard deviation on 

For larger samples, the standard error will be smaller

Margin of error (2ð): have 99% of the means, so it is quite secure to state that the population mean will be within that margin.



The central limit can be used on regressions...

Estimation of the standard error:

## Interval of confidence

Confidence interval: An estimated range of values that seems reasonable for the population mean based on what we observed.
Such an interval has the center on the sample mean and covers some room for uncertainty









