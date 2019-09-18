"""
Put the version to the __version__ variable.

Realized with the versioneer.
"""


__all__ = ("VERSION", "Client", "get_version")  # noqa


# Declare child imports last to prevent recursion
from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
