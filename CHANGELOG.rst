CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^

- User-specified prefix for object path, can be configured via
  DTOOL_ECS_DATASET_PREFIX_* in the dtool configuration file


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


[0.5.0] - 2021-01-19
--------------------

Added
^^^^^

- Added support for working with tags.
- Added verbose error reporting when endpoint information are missing.
  Thanks to `Lars Pastewka <https://github.com/pastewka>`_.


[0.4.0] - 2019-11-19
--------------------

Added
^^^^^

- Added support for dataset annotations


[0.3.1] - 2019-09-19
--------------------

Fixed
^^^^^

- Increased the number of connection retries to 20 from the default of 4
  to make it more robust


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
