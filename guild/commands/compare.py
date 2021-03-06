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

import click

from guild import click_util

from . import runs_support

@click.command()
@click.argument("runs", metavar="[RUN...]", nargs=-1)
@runs_support.run_scope_options
@runs_support.runs_list_options
@click.option(
    "--csv", "format", flag_value="csv",
    help="Generate comparison data as a CSV file.",
    is_flag=True)

@click_util.use_args

def compare(args):
    """Compare run results.
    """
    from . import compare_impl
    compare_impl.main(args)
