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

from .packages_delete import delete_packages
from .packages_info import package_info
from .packages_list import list_packages

class PackagesGroup(click.Group):

    def get_command(self, ctx, cmd_name):
        if cmd_name in ["delete", "rm"]:
            cmd_name = "delete, rm"
        elif cmd_name in ["list", "ls"]:
            cmd_name = "list, ls"
        return super(PackagesGroup, self).get_command(ctx, cmd_name)

@click.group(invoke_without_command=True, cls=PackagesGroup)

@click.pass_context

def packages(ctx, **kw):
    """Show or manage packages.

    If COMMAND is not specified, lists packages.
    """
    if not ctx.invoked_subcommand:
        ctx.invoke(list_packages, **kw)

packages.add_command(delete_packages)
packages.add_command(list_packages)
packages.add_command(package_info)