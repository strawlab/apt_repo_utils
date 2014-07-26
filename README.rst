==============================================================================
apt repo utils - Utilities for dealing with debian and ubuntu apt repositories
==============================================================================

.. contents::

check-shadow.py - check if packages are shadowed by newer versions elsewhere
----------------------------------------------------------------------------

Suppose you have a custom repository like debs.strawlab.org (i.e. `deb
http://debs.strawlab.org/ precise/` is in your `/etc/apt/sources.list`
file). After running `apt-get update` to ensure your local cache is
current, you can check if any of the packages at debs.strawlab.org are
shadowed by newer versions elsewhere::

    python check-shadow.py debs.strawlab.org

This will print a JSON-encoded dictionary like
`{pkg_name:{version1:site_a, version2:site_b}}` where multiple
versions are available of `pkg_name`, including at least one version
at the site specified on the command line which is shadowed by a newer
version at another site.
