Add ECS S3 support to dtool
===========================

.. image:: https://badge.fury.io/py/dtool-ecs.svg
   :target: http://badge.fury.io/py/dtool-ecs
   :alt: PyPi package

- GitHub: https://github.com/jic-dtool/dtool-ecs
- PyPI: https://pypi.python.org/pypi/dtool-ecs
- Free software: MIT License

Features
--------

- Copy datasets to and from ECS S3 object storage
- List all the datasets in a ECS S3 bucket
- Create datasets directly in ECS S3

Installation
------------

To install the dtool-ecs package::

    pip install dtool-ecs

Configuration
-------------

Create the file ``.config/dtool/dtool.json`` and add the ECS account details
using the format below::

    {
       "DTOOL_ECS_ENDPOINT_<BUCKET NAME>": "<ENDPOINT URL HERE>",
       "DTOOL_ECS_ACCESS_KEY_<BUCKET NAME>": "<USER NAME HERE>",
       "DTOOL_ECS_SECRET_ACCESS_KEY_<BUCKET NAME>": "<KEY HERE>"
    }

For example::

    {
       "DTOOL_ECS_ENDPOINT_my-bucket": "http://blueberry.famous.uni.ac.uk",
       "DTOOL_ECS_ACCESS_KEY_ID_my-bucket": "olssont",
       "DTOOL_ECS_SECRET_ACCESS_KEY_my-bucket": "some-secret-token"
    }

See the `dtool documentation <http://dtool.readthedocs.io>`_ for more detail.

Related packages
----------------

- `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_
- `dtool-http <https://github.com/jic-dtool/dtool-http>`_
- `dtool-s3 <https://github.com/jic-dtool/dtool-s3>`_
- `dtool-azure <https://github.com/jic-dtool/dtool-azure>`_
- `dtool-irods <https://github.com/jic-dtool/dtool-irods>`_
