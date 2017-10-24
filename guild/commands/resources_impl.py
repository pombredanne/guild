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

from guild import cli
from guild import resource
from guild import cmd_impl_support

def main(args):
    cmd_impl_support.init_resource_path(args.all, "--all")
    formatted = [_format_resource(r) for r in resource.iter_resources()]
    cli.table(
        sorted(formatted, key=lambda r: r["name"]),
        cols=["name", "description"],
        detail=(["sources"] if args.verbose else [])
    )

def _format_resource(res):
    resdef = res.resourcedef
    return {
        "name": resdef.name,
        "description": resdef.description or "",
        "sources": "\n".join([
            "  %s\n" % source
            for source in resdef.sources
        ])
    }