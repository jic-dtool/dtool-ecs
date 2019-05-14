CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^


[0.3.0] - 2019-05-14
--------------------

Added
^^^^^

- Support for multiple namespaces


Changed
^^^^^^^

Environment variables used to configure access to the ECS storage to allow use
of multiple namespaces.

- ``DTOOL_ECS_ENDPOINT`` has changed to ``DTOOL_ECS_ENDPOINT_<BUCKET NAME>``
- ``DTOOL_ECS_ACCESS_KEY`` has changed to ``DTOOL_ECS_ACCESS_KEY_<BUCKET NAME>``
- ``DTOOL_ECS_SECRET_ACCESS_KEY`` has changed to ``DTOOL_ECS_SECRET_ACCESS_KEY_<BUCKET NAME>``


[0.2.0] - 2019-04-25
--------------------

Changed
^^^^^^^

- Cache environment variable changed from DTOOL_ECS_CACHE_DIRECTORY to DTOOL_CACHE_DIRECTORY
- Default cache directory changed from ``~/.cache/dtool/ecs`` to ``~/.cache/dtool``


[0.1.0] - 2018-08-13
--------------------

Initial release.
