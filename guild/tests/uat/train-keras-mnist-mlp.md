# Train Keras `mnist-mlp`

For this example, we'll use the full spelling of "train", which is to
run the `train` operation on the model.

    >>> run("guild run -y keras.mnist/mnist-mlp:train epochs=1")
    Resolving 'script' resource
    ...
    Resolving 'mnist-npz' resource
    ...
    Using TensorFlow backend.
    ...
    Test loss: ...
    Test accuracy: ...
    <exit 0>
