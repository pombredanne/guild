# Check without TensorFlow

The check command will work when TensorFlow is not installed. However
it will note the problem and exit with an error.

    >>> run("guild check")
    guild_version:             ...
    guild_home:                ...
    guild_install_location:    ...
    installed_plugins:         cloudml, cpu, disk, gpu, keras, memory
    python_version:            ...
    tensorflow_version:        NOT INSTALLED (No module named 'tensorflow')
    nvidia_smi_available:      ...
    guild: there are problems with your Guild setup
    Refer to the issues above for more information or rerun check with the --verbose option.
    <exit 1>
