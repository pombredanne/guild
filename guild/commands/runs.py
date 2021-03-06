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

from guild import cli
from guild import click_util

from . import runs_support

from .runs_delete import delete_runs
from .runs_info import run_info
from .runs_list import list_runs
from .runs_purge import purge_runs
from .runs_restore import restore_runs

@click.group(invoke_without_command=True, cls=click_util.Group)
@runs_support.runs_list_options

@click.pass_context

def runs(ctx, **kw):
    """Show or manage runs.

    If COMMAND is omitted, lists run. Refer to 'guild runs list
    --help' for more information on the list command.
    """
    if not ctx.invoked_subcommand:
        ctx.invoke(list_runs, **kw)
    else:
        if _params_specified(kw):
            # TODO: It'd be nice to move kw over to the subcommand.
            cli.error(
                "options cannot be listed before command ('%s')"
                % ctx.invoked_subcommand)

def _params_specified(kw):
    return any((kw[key] for key in kw))

runs.add_command(delete_runs)
runs.add_command(run_info)
runs.add_command(list_runs)
runs.add_command(purge_runs)
runs.add_command(restore_runs)
