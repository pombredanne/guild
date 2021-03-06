# Copyright 2017 TensorHub, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division

import functools
import logging
import os
import shutil

import guild.config
import guild.run
import guild.util

log = logging.getLogger("core")

def path(subpath):
    return os.path.join(_root(), subpath)

def _root():
    return guild.config.guild_home()

def runs_dir(deleted=False):
    if deleted:
        return trash_dir("runs")
    else:
        return path("runs")

def trash_dir(name=None):
    return os.path.join(path("trash"), name) if name else path("trash")

def cache_dir(name=None):
    return os.path.join(path("cache"), name) if name else path("cache")

def runs(root=None, sort=None, filter=None, run_init=None):
    root = root or runs_dir()
    filter = filter or (lambda _: True)
    runs = [run for run in _all_runs(root, run_init) if filter(run)]
    if sort:
        runs = sorted(runs, key=_run_sort_key(sort))
    return runs

def run_filter(name, *args):
    # Disabling undefined-variable check to work around
    # https://github.com/PyCQA/pylint/issues/760
    # pylint: disable=undefined-variable
    if name.startswith("!"):
        name = name[1:]
        maybe_negate = lambda f: lambda r: not f(r)
    else:
        maybe_negate = lambda f: lambda r: f(r)
    if name == "true":
        filter = lambda _: True
    elif name == "attr":
        name, expected = args
        filter = lambda r: _run_attr(r, name) == expected
    elif name == "all":
        filters, = args
        filter = lambda r: all((f(r) for f in filters))
    elif name == "any":
        filters, = args
        filter = lambda r: any((f(r) for f in filters))
    else:
        raise ValueError(name)
    return maybe_negate(filter)

def _all_runs(root, run_init):
    return [run for run in _all_init_runs(root, run_init) if run]

def _all_init_runs(root, run_init):
    run_init = run_init if run_init else lambda x: x
    return [
        run_init(guild.run.Run(name, path))
        for name, path in _iter_dirs(root)
    ]

def _iter_dirs(root):
    try:
        names = os.listdir(root)
    except OSError:
        names = []
    for name in names:
        path = os.path.join(root, name)
        if os.path.isdir(path):
            yield name, path

def _run_sort_key(sort):
    return functools.cmp_to_key(lambda x, y: _run_cmp(x, y, sort))

def _run_cmp(x, y, sort):
    for attr in sort:
        attr_cmp = _run_attr_cmp(x, y, attr)
        if attr_cmp != 0:
            return attr_cmp
    return 0

def _run_attr_cmp(x, y, attr):
    if attr.startswith("-"):
        attr = attr[1:]
        rev = -1
    else:
        rev = 1
    x_val = _run_attr(x, attr)
    y_val = _run_attr(y, attr)
    return rev * ((x_val > y_val) - (x_val < y_val))

def _run_attr(run, name):
    if name in guild.run.Run.__properties__:
        return getattr(run, name)
    else:
        return run.get(name)

def delete_runs(runs, permanent=False):
    for run in runs:
        src = os.path.join(runs_dir(), run.id)
        if permanent:
            _delete_run(src)
        else:
            dest = os.path.join(runs_dir(deleted=True), run.id)
            _move(src, dest)

def purge_runs(runs):
    for run in runs:
        src = os.path.join(runs_dir(deleted=True), run.id)
        _delete_run(src)

def _delete_run(src):
    assert src and src != os.path.sep, src
    assert (src.startswith(runs_dir()) or
            src.startswith(runs_dir(deleted=True))), src
    log.debug("deleting %s", src)
    shutil.rmtree(src)

def _move(src, dest):
    guild.util.ensure_dir(os.path.dirname(dest))
    log.debug("moving %s to %s", src, dest)
    shutil.move(src, dest)

def restore_runs(runs):
    for run in runs:
        src = os.path.join(runs_dir(deleted=True), run.id)
        dest = os.path.join(runs_dir(), run.id)
        _move(src, dest)

def find_runs(run_id_prefix, root=None):
    root = root or runs_dir()
    return (
        (name, path) for name, path in _iter_dirs(root)
        if name.startswith(run_id_prefix)
    )

def get_run(run_id, root=None):
    root = root or runs_dir()
    path = os.path.join(root, run_id)
    if os.path.exists(path):
        return guild.run.Run(run_id, path)
    raise LookupError(run_id)
