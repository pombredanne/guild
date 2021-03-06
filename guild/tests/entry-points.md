# Entry points

Various Guild "objects" (internal code resources) are discoverable
using `pkg_resources`. For details on this module, see [Package
Discovery and Resource Access using
pkg_resources](http://setuptools.readthedocs.io/en/latest/pkg_resources.html).

    >>> import pkg_resources

For the tests below we're only interested in resources provided by
Guild itself and not other packages that may be installed on the
system.

Here's a function that returns a sorted list of Guild entry points.

    >>> def guild_entry_points(group, name=None):
    ...   return sorted(
    ...     [ep for ep in pkg_resources.iter_entry_points(group, name)
    ...      if ep.dist.project_name == "guildai"],
    ...     key=lambda ep: ep.name)

Guild uses entry points to discover various resources including
plugins, namespaces, and models. Guid defines its built-in resources
in `PKG_INFO/entry_points.txt` where `PKG_INFO` is the location of the
`guild` package. Other packages can advertise Guild entry points in
their own distributions in the same way.

    >>> pprint(guild_entry_points("guild.plugins"))
    [EntryPoint.parse('cloudml = guild.plugins.cloudml:CloudMLPlugin'),
     EntryPoint.parse('cpu = guild.plugins.cpu:CPUPlugin'),
     EntryPoint.parse('disk = guild.plugins.disk:DiskPlugin'),
     EntryPoint.parse('gpu = guild.plugins.gpu:GPUPlugin'),
     EntryPoint.parse('keras = guild.plugins.keras:KerasPlugin'),
     EntryPoint.parse('memory = guild.plugins.memory:MemoryPlugin')]
