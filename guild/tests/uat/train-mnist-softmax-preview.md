# Train `mnist-softmax` preview

By default Guild operations show the user a preview, allowing her to
review the setting before continuing.

Because the prompt waits for user input, we need to terminate the
process using a timeout:

    >>> run("guild train mnist-softmax", timeout=1)
    You are about to run mnist/mnist-softmax:train with the following flags:
      batch-size: 100
      epochs: 10
    Continue? (Y/n)
    <exit -9>
