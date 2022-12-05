#!/usr/bin/env python

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import itertools

def emulateMeasurement(size=40, low=0, high=5, slope=1, intercept=0, stddev=0):
    """
    Emulates a given number of measures of a linear relation with some
    independent normal noise.
    """
    X = np.random.uniform(size=size,low=low,high=high)
    Y = intercept + slope*X + np.random.normal(size=len(X))*stddev
    return X, Y

def linearRegression():
    X,Y = emulateMeasurement(stddev=1)
    xrange = np.linspace(
        (5*min(X)-max(X))/4,
        (5*max(X)-min(X))/4,
        num=100
    )
    interpolations = [
        np.polyfit(X,Y,deg=degree)
        for degree in range(1,3)
    ]

    np.polyfit(X,Y,deg=2)
    colors=['red', 'green', 'purple', 'orange']

    fig, ax = plt.subplots()
    ax.scatter(X,Y)
    for interpolation, color in zip(interpolations, itertools.cycle(colors)):
        print(" ".join([f'{val:.3}' for val in interpolation]))
        ax.plot(xrange, np.polyval(interpolation, xrange), color)
    fig.show()

def regressionWithNN():
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=[1]),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(1, name='output_layer'),
    ], name='Interpolator')

    model.compile(
        loss=tf.keras.losses.mae, # Mean Absolute Error
        #optimizer=tf.keras.optimizers.SGD(), # Stochastic Gradient Descent
        optimizer=tf.keras.optimizers.Adam(learning_rate=.0001), # Stochastic Gradient Descent
        metrics=['mae'],
    )

    for a in range(1):
        X,Y = emulateMeasurement(low=-2, stddev=1, slope=10, size=100)
        X = tf.constant(X,dtype=tf.float16)[:,tf.newaxis]
        Y = tf.constant(Y,dtype=tf.float16)
        model.fit(X, Y, epochs=1000, verbose=False)

    fig = plt.figure(figsize=(18,8))
    fig.scatter(X,Y, label='training data')
    xrange = np.linspace(
            #(5*min(X)-max(X))/4,
        -5,
        (5*max(X)-min(X))/4,
        num=500
    )
    fig.plot(xrange, model.predict(xrange), 'red', label="Predicted")

    print(model.predict((4,)))
    print(model.layers[0].weights[0].numpy())
    print(model.evaluate(*emulateMeasurement(low=-2, stddev=1, slope=10, size=100)))

    return model


def medicaldata():
    import pandas as pd
    insurance = pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
    #insurance = pd.get_dummies(insurance) # Turns categorical fields into one hot encoding
    insurance = insurance.sample(frac=1, random_state=1).reset_index()

    #insurance = insurance[insurance['smoker']=='yes']

    # Create X & y values
    X = insurance.drop(['index', "charges"], axis=1)
    Y = insurance["charges"]

    from sklearn.compose import make_column_transformer
    from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42, # set random state for reproducible splits
    )
 
    column_transformer = make_column_transformer(
        (MinMaxScaler(), ['age', 'bmi', 'children']),
        (OneHotEncoder(handle_unknown='ignore'), ["region"]),
        (OrdinalEncoder(handle_unknown='error'), ["sex", "smoker"]),
    )

    # Important: You fit the transformer on the training set
    column_transformer.fit(X_train)
    print(column_transformer.get_feature_names_out())

    # And then apply to both the training and test
    X_train = column_transformer.transform(X_train)
    X_test = column_transformer.transform(X_test)

    return X_train, X_test, y_train, y_test, column_transformer

def multivariateRegression_leastSquares():
    X_train, X_test, y_train, y_test, transformer = medicaldata()

    from sklearn.linear_model import LinearRegression

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    color_column = 1
    print("color:", transformer.get_feature_names_out()[color_column])
    plt.scatter(y_test,predictions,c=X_test[:,color_column])
    plt.xlabel('Y Test')
    plt.ylabel('Predicted Y')
    plt.ylabel('Predicted Y')
    print("Root mean squared error:", np.sqrt(np.square(y_test-predictions).mean()))


def multivariateRegression_NN():
    # Set random seed
    tf.random.set_seed(42)

    X_train, X_test, y_train, y_test, transformer = medicaldata()

    # Create a new model (same as model_2)
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=[X_train.shape[-1]]),
        tf.keras.layers.Dense(500, activation='relu'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(50, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, name='output')
    ])

    # Compile the model
    model.compile(
        loss=tf.keras.losses.mae,
        optimizer=tf.keras.optimizers.Adam(), # Stochastic Gradient Descent
        #optimizer=tf.keras.optimizers.SGD(),
        metrics=['mae'],
    )
    # Fit the model
    history = model.fit(X_train, y_train, epochs=1000, verbose=False)

    #pd.DataFrame(history.history).plot()

    fig = plt.figure(figsize=(18,8))
    plt.plot(history.history['mae'], label='mae')
    plt.legend()
    plt.show()

    # Check the results of the insurance model
    print(model.evaluate(X_test, y_test))

    predictions=tf.squeeze(model.predict(X_test))
    print(predictions.shape, y_test.shape)

    for color_column, color_name in enumerate(transformer.get_feature_names_out()):
        print("color:", color_name)
        fig = plt.figure(figsize=(18,8))
        fig.suptitle(color_name)
        plt.scatter(y_test,predictions,c=X_test[:,color_column])
        plt.xlabel('Y Test')
        plt.ylabel('Predicted Y')
        plt.ylabel('Predicted Y')
        print("Root mean squared error:", np.sqrt(np.square(y_test-predictions).mean()))
    return model


def boundaryScatterPlot(model, X, y, title=None):
    # Define the axis boundaries of the plot and create a meshgrid
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 100),
        np.linspace(y_min, y_max, 100),
    )

    x_in = np.c_[xx.ravel(), yy.ravel()]
    y_pred = model.predict(x_in).reshape(xx.shape)
    if model.output_shape[-1] > 1:
        # Multiclass
        y_pred = np.argmax(y_pred)
    else:
        # Binary classification
        y_pred = np.round(y_pred)
    figure = plt.figure()
    if title:
        figure.suptitle(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    contourplot = plt.contourf(xx, yy, y_pred, vmin=-1, vmax=1, cmap=plt.cm.RdYlBu, alpha=0.7)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu)
    plt.colorbar(contourplot)
    figure.show()


def plotConfusionMatrix(y_test, y_preds, classes=None):
    # Note: The following confusion matrix code is a remix of Scikit-Learn's
    # plot_confusion_matrix function - https://scikit-learn.org/stable/modules/generated/sklearn.metrics.plot_confusion_matrix.html
    # and Made with ML's introductory notebook - https://github.com/GokuMohandas/MadeWithML/blob/main/notebooks/08_Neural_Networks.ipynb
    from sklearn.metrics import confusion_matrix
    import itertools

    figsize = (15, 15)

    # Create the confusion matrix
    cm = confusion_matrix(y_test, tf.round(y_preds))
    cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis] # normalize it
    n_classes = cm.shape[0]

    # Let's prettify it
    fig, ax = plt.subplots(figsize=figsize)
    # Create a matrix plot
    cax = ax.matshow(cm, cmap=plt.cm.Blues) # https://matplotlib.org/3.2.0/api/_as_gen/matplotlib.axes.Axes.matshow.html
    fig.colorbar(cax)

    if classes:
        labels = classes
    else:
        labels = np.arange(cm.shape[0])

    # Label the axes
    ax.set(
        title="Confusion Matrix",
        xlabel="Predicted label",
        ylabel="True label",
        xticks=np.arange(n_classes),
        yticks=np.arange(n_classes),
        xticklabels=labels,
        yticklabels=labels,
    )

    # Set x-axis labels to bottom
    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()

    # Adjust label size
    ax.xaxis.label.set_size(20)
    ax.yaxis.label.set_size(20)
    ax.title.set_size(20)

    # Set threshold for different colors
    threshold = (cm.max() + cm.min()) / 2.

    # Plot the text on each cell
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(
            j, i, f"{cm[i, j]} ({cm_norm[i, j]*100:.1f}%)",
            horizontalalignment="center",
            color="white" if cm[i, j] > threshold else "black",
            size=15,
        )

def circleClassification():

    from sklearn.model_selection import train_test_split
    from sklearn.datasets import make_circles

    # Make 1000 examples
    n_samples = 1000

    # Create circles
    X, y = make_circles(
        n_samples, 
        noise=0.03, 
        random_state=42,
    )

    plt.scatter(X[:,0], X[:,1], c=y)

    # Set random seed
    tf.random.set_seed(100)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42, # set random state for reproducible splits
    )

    # 1. Create the model using the Sequential API
    model = tf.keras.Sequential([
      tf.keras.layers.Dense(20, activation='relu'),
      tf.keras.layers.Dense(6, activation='relu'),
      tf.keras.layers.Dense(1, activation='sigmoid'),
    ])

    # 2. Compile the model
    model.compile(
        loss=tf.keras.losses.BinaryCrossentropy(), # binary since we are working with 2 clases (0 & 1)
        optimizer=tf.keras.optimizers.Adam(learning_rate=.001),
        metrics=['accuracy'],
    )

    random=tf.random.uniform(shape=(500,2), minval=-1)
    # 3. Fit the model
    accuracy_history = []
    step = 5
    for i in range(int(200/step)):
        history = model.fit(X_train, y_train, epochs=step, verbose=False)
        accuracy_history.extend(history.history['accuracy'])
        boundaryScatterPlot(model, X_test, y_test, title=f"Epoch {i*step}, accuracy {accuracy_history[-1]:.3f}")

    fig = plt.figure(figsize=(18,8))
    plt.plot(accuracy_history, label='accuracy')
    plt.legend()
    plt.show()

    model.evaluate(X_test, y_test)
    boundaryScatterPlot(model, X_test, y_test)

    y_pred = model.predict(X_test)
    plotConfusionMatrix(y_test, y_pred)




#linearRegression()
#model = regressionWithNN()
#multivariateRegression_leastSquares()
#model = multivariateRegression_NN() # 
#circleClassification()
#plotConfusionMatrix(
#    [x and 'abcd'.index(x) for x in 'abaaaabbbcccddaaadddaaaddaddaabbb'],
#    [x and 'abcd'.index(x) for x in 'abaaaabcbcccaaadddaaaddaddaabbbaa'],
#)

def multiclassClassification():
    from tensorflow.keras.datasets import fashion_mnist
    (
        (train_data, train_labels),
        (test_data, test_labels),
    ) = fashion_mnist.load_data()

    # data is a 28x28 grayscale image of a piece of 
    class_names = [
        'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot',
    ]

    def showFashion(data, label, index):
        plt.imshow(data[index], cmap=plt.cm.binary)
        plt.title(class_names[label[index]])

    showFashion(train_data, train_labels, 5)

    train_data = train_data / 255.
    test_data = test_data / 255.
    train_labels = tf.one_hot(train_labels, depth=len(class_names))
    test_labels = tf.one_hot(test_labels, depth=len(class_names))

    # 1. Create the model using the Sequential API
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=train_data.shape[1:]), # This is added
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(len(class_names), activation='softmax'), # This changes
    ])

    # 2. Compile the model
    model.compile(
        loss=tf.keras.losses.CategoricalCrossentropy(),
        optimizer=tf.keras.optimizers.Adam(learning_rate=.001),
        metrics=['accuracy'],
    )

    fullhistory={}
    accuracy_history=[]
    loss_history=[]
    nepochs = 5
    step = 1
    for i in range(int(nepochs/step)):
        history = model.fit(
            train_data, train_labels,
            validation_data=(test_data, test_labels),
            epochs=step,
            #verbose=False,
        )
        for metric, data in history.history.items():
            fullhistory.setdefault(metric, []).extend(data)

    fig = plt.figure(figsize=(18,8))
    for metric, data in fullhistory.items():
        plt.plot(data, label=metric)
    plt.legend()
    plt.show()

    predicted = model.predict(test_data)
    print(predicted)
    plotConfusionMatrix(tf.argmax(test_labels, axis=1), tf.argmax(predicted, axis=1), class_names)

multiclassClassification()


