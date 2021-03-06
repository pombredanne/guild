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

import errno
import os
import logging
import sys
import time
import threading

OS_ENVIRON_BLACKLIST = [
    "PYTHONPATH", # unsafe - must be set explicitly
]

class Stop(Exception):
    """Raise to stop loops started with `loop`."""

def find_apply(funs, *args, **kw):
    for f in funs:
        result = f(*args)
        if result is not None:
            return result
    return kw.get("default")

def ensure_dir(d):
    try:
        os.makedirs(d)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def pid_exists(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def free_port():
    import random
    import socket
    min_port = 49152
    max_port = 65535
    max_attempts = 100
    attempts = 0

    while True:
        if attempts > max_attempts:
            raise RuntimeError("too many free port attempts")
        port = random.randint(min_port, max_port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        try:
            sock.connect(('localhost', port))
        except socket.timeout:
            return port
        except socket.error as e:
            if e.errno == errno.ECONNREFUSED:
                return port
        else:
            sock.close()
        attempts += 1

def open_url(url):
    try:
        _open_url_with_cmd(url)
    except OSError:
        _open_url_with_webbrowser(url)

def _open_url_with_cmd(url):
    import subprocess
    if sys.platform == "darwin":
        args = ["open", url]
    else:
        args = ["xdg-open", url]
    with open(os.devnull, "w") as null:
        subprocess.check_call(args, stderr=null, stdout=null)

def _open_url_with_webbrowser(url):
    import webbrowser
    webbrowser.open(url)

def loop(cb, wait, interval, first_interval=None):
    try:
        _loop(cb, wait, interval, first_interval)
    except Stop:
        pass
    except KeyboardInterrupt:
        pass

def _loop(cb, wait, interval, first_interval):
    loop_interval = first_interval if first_interval is not None else interval
    start = time.time()
    while True:
        sleep = _sleep_interval(loop_interval, start)
        loop_interval = interval
        should_stop = wait(sleep)
        if should_stop:
            break
        cb()

def _sleep_interval(interval, start):
    if interval <= 0:
        return 0
    now_ms = int(time.time() * 1000)
    interval_ms = int(interval * 1000)
    start_ms = int(start * 1000)
    sleep_ms = (
        ((now_ms - start_ms) // interval_ms + 1)
        * interval_ms + start_ms - now_ms)
    return sleep_ms / 1000

class LoopingThread(threading.Thread):

    def __init__(self, cb, interval, first_interval=None, stop_timeout=0):
        super(LoopingThread, self).__init__()
        self._cb = cb
        self._interval = interval
        self._first_interval = first_interval
        self._stop_timeout = stop_timeout
        self._stop = threading.Event()
        self._stopped = threading.Event()

    def run(self):
        loop(
            cb=self._cb,
            wait=self._stop.wait,
            interval=self._interval,
            first_interval=self._first_interval)
        self._stopped.set()

    def stop(self):
        self._stop.set()
        self._stopped.wait(self._stop_timeout)

def safe_osenv():
    return {
        name: val
        for name, val in os.environ.items()
        if name not in OS_ENVIRON_BLACKLIST
    }

def match_filters(filters, vals, match_any=False):
    test_fun = any if match_any else all
    vals_lower = [val.lower() for val in vals]
    filters_lower = [f.lower() for f in filters]
    return test_fun(
        (any((f in val for val in vals_lower))
         for f in filters_lower)
    )

def split_description(s):
    lines = s.split("\n")
    return lines[0], _format_details(lines[1:])

def _format_details(details):
    lines = []
    for i, line in enumerate(details):
        if i > 0:
            lines.append("")
        lines.append(line)
    return lines

def file_sha256(path):
    import hashlib
    hash = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            hash.update(data)
    return hash.hexdigest()

def parse_url(url):
    try:
        from urlparse import urlparse
    except ImportError:
        # pylint: disable=import-error,no-name-in-module
        from urllib.parse import urlparse
    return urlparse(url)

class TempDir(object):

    def __init__(self, prefix=None):
        self._prefix = prefix
        self.path = None

    def __enter__(self):
        import tempfile
        self.path = tempfile.mkdtemp(prefix=self._prefix)
        return self.path

    def __exit__(self, *_exc):
        import shutil
        import tempfile
        assert os.path.dirname(self.path) == tempfile.gettempdir(), self.path
        shutil.rmtree(self.path)

def mktempdir(prefix=None):
    import tempfile
    return tempfile.mkdtemp(prefix=prefix)

class LogCapture(object):

    def __init__(self):
        self._records = []

    def __enter__(self):
        for logger in self._iter_loggers():
            logger.addFilter(self)
        self._records = []
        return self

    def __exit__(self, *exc):
        for logger in self._iter_loggers():
            logger.removeFilter(self)

    @staticmethod
    def _iter_loggers():
        yield logging.root
        for logger in logging.Logger.manager.loggerDict.values():
            if isinstance(logger, logging.Logger):
                yield logger

    def filter(self, record):
        self._records.append(record)

    def print_all(self):
        format = logging.root.handlers[0].format
        for r in self._records:
            print(format(r))

    def get_all(self):
        return self._records
