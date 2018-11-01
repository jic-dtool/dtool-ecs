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
       "DTOOL_ECS_ENDPOINT": "http://blueberry.famous.uni.ac.uk",
       "DTOOL_ECS_ACCESS_KEY_ID": "olssont",
       "DTOOL_ECS_SECRET_ACCESS_KEY": "some-secret-token"
    }
