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

from guild import entry_point_util
from guild.model import ModelfileDistribution

_resources = entry_point_util.EntryPointResources("guild.resources", "resource")

class Resource(object):

    def __init__(self, ep):
        self.name = ep.name
        self.dist = ep.dist
        self.resourcedef = _resourcedef_for_dist(ep.name, ep.dist)

def _resourcedef_for_dist(name, dist):
    if isinstance(dist, ModelfileDistribution):
        for model in dist.modelfile:
            for res_name in model.resources:
                if res_name == name:
                    return model.resources[res_name]
        raise ValueError(
            "cannot find resource '%s' in modefile %s"
            % name, dist.modelfile.src)
    else:
        raise ValueError("unsupported resource distribution: %s" % dist)

def set_path(path):
    _resources.set_path(path)

def add_model_path(model_path):
    path = _resources.path()
    try:
        path.remove(model_path)
    except ValueError:
        pass
    path.insert(0, model_path)
    _resources.set_path(path)

def iter_resources():
    for _name, resource in _resources:
        yield resource