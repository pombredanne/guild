# Create MNIST package

Guild packages are created using the `package` command. This command
is commonly run within a directory containing a `PACKAGE` file, but it
can also be run using the `-C` option.

For our tests we'll just run the command in the `mnist` package
directory:

    >>> cd("guild-index/mnist")
    >>> run("guild package", ignore=['Normalizing', 'normalized_version,'])
    running bdist_wheel
    ...
    creating '.../guild-index/mnist/dist/gpkg.mnist-...-py2.py3-none-any.whl'
    ...
    adding 'gpkg/mnist/MODELS'
    adding 'gpkg/mnist/README.md'
    adding 'gpkg/mnist/__init__.py'
    adding 'gpkg/mnist/cnn.py'
    adding 'gpkg/mnist/softmax.py'
    ...
    <exit 0>