# Alternate run directory

By default Guild manages runs in a location under its home
directory. In some cases a user may want to generate a run in an
alternative directory. A common case for this is during development
when models are changed frequently and it's important to either not
clutter the list of runs with errors or it's simply more convenient to
develop with a single run directory.

Let's run a `hello` operation using a specific run directory.

    >>> run("guild run hello:default --run-dir hello-default -y")
    Run directory is 'hello-default' (results will not be visible to Guild)
    Hello Guild!
    <exit 0>

And the generated files:

    >>> run("find hello-default | sort")
    hello-default
    hello-default/.guild
    hello-default/.guild/attrs
    hello-default/.guild/attrs/cmd
    hello-default/.guild/attrs/env
    hello-default/.guild/attrs/exit_status
    hello-default/.guild/attrs/flags
    hello-default/.guild/attrs/opref
    hello-default/.guild/attrs/started
    hello-default/.guild/attrs/stopped
    hello-default/.guild/logs
    hello-default/output
    <exit 0>
