# `mnist` package info

Use `guild packages info PKG` to show information about a package:

    >>> run("guild packages info mnist")
    name: mnist
    version: 0.1.0.post10
    summary: CNN and softmax regression classifiers for MNIST digits
    home-page: https://github.com/guildai/index/tree/master/mnist
    author: Guild AI
    author-email: packages@guild.ai
    license: Apache 2.0
    location: /tmp/guild-uat/lib/python3.5/site-packages
    requires: []
    <exit 0>

We can use the `--verbose` and `--files` flags to get more
information.

    >>> run("guild packages info mnist --verbose --files")
    name: mnist
    version: 0.1.0.post10
    summary: CNN and softmax regression classifiers for MNIST digits
    home-page: https://github.com/guildai/index/tree/master/mnist
    author: Guild AI
    author-email: packages@guild.ai
    license: Apache 2.0
    location: /tmp/guild-uat/lib/python3.5/site-packages
    requires: []
    metadata-version: 2.0
    installer: pip
    classifiers:
    entry-points:
      [guild.models]
      mnist-cnn = guild.model:PackageModel
      mnist-softmax = guild.model:PackageModel
    files:
      ...
      gpkg/mnist/cnn.py
      gpkg/mnist/softmax.py
    <exit 0>