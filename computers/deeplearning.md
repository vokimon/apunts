# Deep learning

Notes taken from https://www.youtube.com/watch?v=tpCFfeUEGs8

## Applicability

	_If you can build a rule based system that does the same, do that_

So:

- When you cannot figure out all the rules
- When the rules changes all the time
- Getting insigths on large sets of data

But (mostly) not when:

- Requiring explainability
- Traditional approach is a better option
- When errors unacceptable
- Not large amounts of data

Mostly because it can be circunvented

Machine learning: Turning data into numbers and finding patterns in those numbers

While traditional Machine Learning works better with structured (tabular) data,
deep learning works better on unstructured data.

Old ML (shallow) algoriths:
- Random forest
- Naive bayes
- Nearest Neighbour
- Support vector machines


## Neural networks

Input Data -> Numerical Input -> Neural Network -> Numerical Output -> Interpreted Output

Input data: Images, text, audio...
Numerical Input: Processed numerical features as vectors of numbers
Numerical Output: Learned output, also vectors/tensors of numbers
Interpreted output: We know how to interprete output depending on the learning references

Anatomy:

- Neuron: processing depending on some inputs to generate a single output
- Input layers: Neurons that receives directly the numerical input
- Output layers: Neurons that generates the numerical output
- Hidden layers: Neurons not  involved with neither input or output

Types of learning:

- Supervised: Learning on labeled information
- Semisupervised: labels just for some inputs
- Unsupervised learning: Find patterns with no  
- Transfer learning: TODO: Not understood

Real used:

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
- Dimension: Number of numbers for each component

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
c3 = tf.constant([[[1,2],[3,4],[5,6]],[[1,2],[3,4],[5,6]]]) # tensor rank 2 (matrix)
c3.shape # (2,3,2)
c2.ndim # 3

v = tf.Variable([3,4]) 
v[0] = 5 # fails
v[0].assign(5) # works

```



