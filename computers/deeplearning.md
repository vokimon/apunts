# Deep learning

Notes taken from https://www.youtube.com/watch?v=tpCFfeUEGs8

## Definition of the field

**Artificial Intelligence:**
Mimicking the intelligence or behavioural patterns of humans
(or other living beings)

**Machine Learning:**
Machine learning algorithms build a model based on sample data,
known as training data, in order to make predictions or decisions
without being explicitly programmed to do so.

Instead of telling the computer how to cook a recipe,
you show it the input and the output and it figures out
how to cook it.
In order to do that you show it many recipes in order for it to learn.

**Machine learning:** Turning data into numbers and finding patterns in those numbers

While traditional Machine Learning works better with structured (tabular) data,
deep learning works better on unstructured data.

However a given problem could be represented as either structured or unstructured.

**Deep Learning:** A type of Machine Learning,
based on neural networks in which multiple layers of processing
each extracting progressively higher level features from data.

Old ML (shallow) algoriths:
- Random forest
- Naive bayes
- Nearest Neighbour
- Support vector machines
- Gradient boosted trees

Deep learning algorithms:

- Neural Networks
- Fully connected NN
- Convolutional NN
- Recurrent NN
- Transformers
- ...

## Applicability

	_If you can build a rule based system that does the same, do that_

So:

- When you cannot figure out all the rules
- When the rules changes all the time
- Getting insigths on large sets of data

But (mostly) not when:

- Traditional approach is a better option: well not mess with us
- Requiring explainability: deep learning results are often non interpretable
- When errors unacceptable: deep learning is not expectable
- Not large amounts of data: such amounts are required

Mostly because it can be circunvented


## Neural networks

Neural Networks: Set or interconnected nodes (neurons)
each one processing as inputs the outputs of the other nodes.

Input Data -> Numerical Input -> Neural Network -> Numerical Output -> Interpreted Output

Input data: Images, text, audio...
Numerical Input: Processed numerical features as vectors of numbers
Numerical Output: Learned output, also vectors/tensors of numbers
Interpreted output: We know how to interprete output depending on the learning references

Anatomy:

- Neuron: processing depending on some inputs to generate a single output
- Input layer: Neurons that receives directly the numerical input
- Output layer: Neurons that generates the numerical output
- Hidden layers: Neurons not  involved with neither input or output

The learning of patterns is don in the hidden layers.
This learning of patterns is also called
_embedding_, _weights_, _feature vectors_, _feature representation_...

Types of learning:

- Supervised: Learning on labeled information
- Semisupervised: labels just for some inputs
- Unsupervised learning: Find patterns with no  
- Transfer learning: TODO: Not understood

Real uses:

- Recommendation
- Sequence to sequence seq2seq
	- Translation
	- Speech recognition
- Classification/regression
	- Computer vision
	- Natural language processing

## Tensorflow

End-to-end platform:

- Preprocessing data
- Define neural models (neural arquitecture)
- Train in GPU/TPU (tensor processing unit)
- You can migrate the trained model to the application and use them

Tensor: Representacion númerica multidimensional

- Rank: Number of indexes to access a component
- Dimension(s): Number of numbers for each component

Rank 0: Scalar
Rank 1: Vector
Rank 2: Matrix
Rank 3: Booom
Rank 4 and beyond: Crackaboom

```python
import TensorFlow as tf

c0 = tf.constant(4) # tensor rank 0 (scalar)
c1 = tf.constant([3,3]) # tensor rank 1 (vector)
c2 = tf.constant([[1,2],[3,4],[5,6]]) # tensor rank 2 (matrix)
c3 = tf.constant([[[1,2],[3,4],[5,6]],[[1,2],[3,4],[5,6]]]) # tensor rank 3 (tensor)

# What we have
c3.shape # (2,3,2) can be reshaped with the shape param
c3.ndim # 3, the rank
c3.dtype # tf.int64, can be changed providing dtype param
tf.size(c3) # 12, the number of elements, multiplicative 
c3[1] # slice the second element on the first dimension
c3[:,1] # slice the second element on the second dimension

v1 = tf.Variable([3,4]) 
v1[0] = 5 # fails
v1[0].assign(5) # works

v3 = tf.Variable([[[1,2],[3,4],[5,6]],[[10,20],[30,40],[50,60]]])
v3[0,0,0].assign(69)
v3[1,...,1].assign([666,666,666])

# We will use random tensor to initialize the weights.
tf.random.uniform(shape) # minval=0. to maxval=1., if dtype = int, maxval must ve especified
tf.random.normal(shape) # mean=0, stddev=1

tf.random.Generator.from_seed(69) # for reproducibility
# Also you can use operation level seed (seed=x parameter),
# but then they are combined and in order to have
# reproducible results you have to specify them both always

tf.shuffle(v3) # returns a tensor with the first dimension randomly exchanged
# We use shuffle to randomly set the order of the training inputs

# Often is useful to create zero and ones matrixes

tf.ones(shape)
tf.zeros(shape)
tf.arange(N)

import numpy as np
v = tf.constant(np.arrange(30), shape=(3,2,5)) # numpy -> tensorflow
n = v.numpy() # tensorflow -> numpy
```

# Indexing the tensors

```python
t[x,x,x]
```

each dimension can have a slice, comma separated:

- : full dimension (the default if not specified for inner dims)
- 2 the third item of the dimension (the dimension is removed)
- -1 the last element along the dimension
- :2 first two items
- :-3 the last 3 elements along the dimension
- 2:3 the third  element but keeps dimension
- 1::2 odd elements
- ::-1 elemens in inverted order
- tf.newaxis expand a 1 lenght dimension

In order to remove single dimensions (dimensions of size 1)

`tf.squeeze(t)`



# Operations

For element wise ops `+`, `*`...

Usually function is faster than operator:

- `tf.math.add` `+`
- `tf.math.multiply` `*`
- `tf.math.divide` `/`
- `tf.math.substract` `-`
- `tf.linalg.matmul` `@`

# Unary ops

- `tf.math.sqrt` Not for int
- `tf.math.log` Not for int
- `tf.math.squared`

All of them are aliased into `tf`, like `tf.add`

Matrix multiplication:

`tf.linalg.matmul` aliased as `tf.matmul`

```python
# Inner dimensions must match, 3 in the example
tf.matmul(tf.random.uniform((2,3)), tf.random.uniform((3,4))).shape
(2,4)
```

How to make it match?

tf.reshape(x, shape) # be careful!! it relocates elements do not flip elements
tf.transpose(x) # inverts the axis order

## Data types

By default, deduces the type from 

- float -> tf.float32
- int -> tf.int32

TPU's use `tf.float16` for speedup and space.

How to obtain different precissions?

```python
tf.cast(x, dtype)
```

Also in construction specify the dtype

Another common use is ops that do not work with ints


## Tensor Aggregation

Condensing values

- `tf.reduce_mean(x)`
- `tf.reduce_sum(x)`
- `tf.reduce_max(x)`
- `tf.reduce_min(x)`

By default reduces all axes, but you can specify the axis to reduce (integer or tuple)

- `tf.argmax(x)`, `tf.argmin(x)` returns the index wich has the position

## One-hot encoding

Way of encoding enumeration.

```python
tf.one_hot(tf.range(4), depth=4, on_value='yes', off_value='no')
```

## NN for regression

Regression problem: Predicting a number given a lot of parametrized examples.

- Independent variables: the ones used as reference (predictors, features, covariates)
- Dependent variables: the ones to be predicted (outcome variable)

A learning system could infer the relationship of the dependant variables respect the independant ones.

The commonly used is the linear regression that suposes a proportion or inverse proportion among variables.











