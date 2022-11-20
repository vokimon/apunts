# Deep learning

Notes taken from https://www.youtube.com/watch?v=tpCFfeUEGs8

Background:

- [Lecture 1: A Brief History of Geometric Deep Learning - Michael Bronstein](https://www.youtube.com/watch?v=yuw_LwqHsgM)
- [Full course for Begginners: How Deep Neural Networks Work](https://www.youtube.com/watch?v=dPWYUELwIdM)


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

Example: Price of a house depending on the number of rooms, bathrooms and garage space (how many cars).

Features, shape 3:

- Number of rooms
- Number of bathrooms
- Number of cars in garage

Outcome, shape 1:

- House price

Other parameters:

- Hidden activation: ReLU (Rectified Linear Unit)
- Option activation:
- Loss function: Computes the error on the output
  - (MSE) Mean Square Error
  - (MAE) Mean Absolute error
  - Huber (combination of MSE and MAE)
- Optimizer: How to compute the next weights given the error
  - SGD Stochastic Gradient Descent
  - Adam Adaptative Moment Estimation
- Evaluation metrics: Human indicator on how well works



```
# Set random seed

tf.random.set_seed(42)

# Create a model using the Sequential API
model = tf.keras.Sequential([
  tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(
	loss=tf.keras.losses.mae, # mae is short for mean absolute error
	optimizer=tf.keras.optimizers.SGD(), # SGD is short for stochastic gradient descent
	metrics=["mae"]
)

# Fit the model
# model.fit(X, y, epochs=5) # this will break with TensorFlow 2.7.0+
model.fit(tf.expand_dims(X, axis=-1), y, epochs=5)

model 
```

## Improving the model

- Model definition:
	- Number of layers
	- Number of neurons per layer
	- Activation function
- Compilation:
	- Optimization function
	- Optimization rate
- Fitting:
	- Number of epochs
	- More data


## Evaluating

Divide the data into 3 sets:

- Training set: The model learns from this data (70-80%)
- Validation set: To tune the parameters of the model (10-15%)
- Test set: To know the final performance achieved (10-15%)

Goal: Generalization: Perform well on data you haven't seen before.

Layer `Dense` means that the layer connects to all the neurons of the previous level.

Trainable parameters are one for input or output connection.

A dense layer `i` with `n_i` nodes will have $$ n_{i-1}*n_i + n* n_{i+1} $$ learnable parameters

A network may have non-trainable parameters if we freeze them.
You want to do this if you are reusing an already learnt model
within a bigger one.

Metrics:

- Mean absolute error MAE: Reduces the importance of outliers
- Mean squared error MSE: Larger error are more significant than smaller errors
- Huber: Inside ð, use the square, outside use a linear proportion adjusted to be continuous in ð

Visualize:

- Learning data
- Model
- Training
- Predictions

Twiking: Change one parameter at a time and evaluate using the metrics.

Tip: Start small so that we can repeat experiments before they last so long.

Evaluation Libraries

- TensorBoard, web app to track experimentation with several models

## Exporting and importing models


`model.save('mymodel')`

Saves

- Model structure
- Weights to predict
- Optimizer status to resume fitting

`tf.keras.models.load_model('mymodel')`

Its a folder with structure. Some files are protobuffer format (`.pb`)

If you use the '.h5' extension it will be saved in a single file using the HDF5 format.
This format is uses to exchange data with other frameworks.

How to visualize the training:

```python
history = model.fit(X_train, y_train, epochs=100)

print(history.history)
pd.DataFrame(history.history).plot()
```

## Normalize or standardize input data

Convert the input data so that all features have the same scale.
ML algorithms perform better if input is normalized.
Ie errors add more if the feature has large numbers.

Strategies:

- MinMaxScaler: Scale linearly mapping min and max to 0 and 1
- Standardizer: Remove the mean divide by the stddev

You fit the column transformer to the training set,
and then apply to both the training and the test set.



## Classification with NN

Binary classification: Two exclusive categories (Is it spam? yes or no)

Multiclass classification: For each sample choose one of the categories

Multilabel classification: When several labels can apply to a sample

What is different?

- Input Layer may hav structure
- Output Layer, one by category (in binary just one)
- Output Activation: Softmax (or Sigmoid for binary)
- Loss Function: `tf.keras.losses.CategoricalCrossentropy` (or `BinaryCrossentropy` for binary)
- Avaluation: accuracy

### Inputs and outputs

The outputs should have an output value for each category/label
with a value from 0 to 1, ideally one-hot-encoding.

### Activation

Default is linear, good for the output but hard for non-linear problems like this one.


http://playground.tensorflow.org


- Linear: passthru f(x) = x
- ReLU: linear but zero for negative f(x) = max(0,x)
- Sigmoid: curved on onf f(x) = 1 / (1+exp(x))


### Evaluation


Cases:

- True positive: predicted positive, and it was
- True negative: predicted negative, and it was
- False positive: predicted positive, but was negative
- False negative: predicted negative, but was positive

Metrics:

- Accuracy:
	- (tp + tn) / (total)
	- `tf.keras.metrics.Accuracy`
	- General purpose. Not best for imbalanced classes
- Precission:
	- tp / (tp + tn)
	- `tf.keras.metrics.Precission`
	- Leads to less false positives
	- You want to confirm that you detect it is right
	- You want apply experimental treatments just the ones that has Covid
- Recall
	- tp / (tp + fn)
	- `tf.keras.metrics.Recall`
	- Leads to less false negatives
	- You want to catch any suspect
	- You want to screen any Covid supect
- F1-score:
	- 2*(precission*recall)/(precission+recall) = tp / (tp + 1/2(fp+fn))
	- `sklearn.metrics.f1_score` # not in tensorflow
- Confusion matrix:
	- Not a metric
	- `sklearn.confusion_matrix()`
	- Good with many classes.


```python
sklearn.metrics.confusion_matrix(truth, prediction)
```

# Multi-class classification



## Process input data

- Turn all your data into numbers
- Make them have the proper shape
- Normalize them


# Internal representation

Each layer has  NxM weights. N outer layer nodes, M number of nodes

Every neuron has a bias parameter.
Iniciatialized zero as default.
The bias is applied (multiplied) to the output to all the neurons of the next layer.



Weights are randomly initialized at the beginning.
(`kernel_initizalizer` parameter, by default `glorot uniform`)

Generates the outputs of the trained data

If fails, the error is propagated back. How?

```python

```

## Convolutional Neural Nets (ConvNets)

The first layer are convolution kernels on a local region of the input.

Have sense on data that has local connection: images (w,h), sound (f,t), text (t)

Rule of thumb: Given a matrix of input data, if swapping rows or columns is meaningless, there is no point of using ConvNets.

- Ex: a table of clients with columns (the order of clients is meaningless, the orded of columns as well)
- Ex: Text with a matrix of time x words, words in a dictionary has no meaningful order, but still time dimension could be useful 


## Recurrent Neural Nets

If the previous result, has impact on the next.

To expand memory beyond the last result, we need memory

- Ignore network: decides what passes to the memory pipeline
- Forget network: decides what is ignored for the next input
- Selection network: decides what of the memory goes outside as output

Applications: sequence based

- text
- speech
- audio
- video
- robotics
- physical process





- Selection: 















