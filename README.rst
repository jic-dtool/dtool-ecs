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

Path prefix and access control
------------------------------

The ECS plugin supports a configurable prefix to the path. This can be used for
access control to the dataset. For example, configure::

    {
       "DTOOL_ECS_DATASET_PREFIX_my-bucket": "u/olssont"
    }

and use the following S3 access to policy to that allows reading all data
in the bucket but only writing to the prefix `u/<username>` and `dtool-`::

    {
      "Statement": [
        {
          "Sid": "AllowReadonlyAccess",
          "Effect": "Allow",
          "Action": [
            "s3:ListBucket",
            "s3:ListBucketVersions",
            "s3:GetObject",
            "s3:GetObjectTagging",
            "s3:GetObjectVersion",
            "s3:GetObjectVersionTagging"
          ],
          "Resource": [
            "arn:aws:s3:::my-bucket",
            "arn:aws:s3:::my-bucket/*"
          ]
        },
        {
          "Sid": "AllowPartialWriteAccess",
          "Effect": "Allow",
          "Action": [
            "s3:DeleteObject",
            "s3:PutObject",
            "s3:PutObjectAcl"
          ],
          "Resource": [
            "arn:aws:s3:::my-bucket/dtool-*",
            "arn:aws:s3:::my-bucket/u/${aws:username}/*"
          ]
        },
        {
          "Sid": "AllowListAllBuckets",
          "Effect": "Allow",
          "Action": [
            "s3:ListAllMyBuckets",
            "s3:GetBucketLocation"
          ],
          "Resource": "arn:aws:s3:::*"
        }
      ]
    }

The user also needs write access to toplevel objects that start with `dtool-`.
Those are the registration keys that are not stored under the configured
prefix. The registration keys contain the prefix where the respective dataset
is found. They are empty if no prefix is configured.

Related packages
----------------

- `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_
- `dtool-http <https://github.com/jic-dtool/dtool-http>`_
- `dtool-s3 <https://github.com/jic-dtool/dtool-s3>`_
- `dtool-azure <https://github.com/jic-dtool/dtool-azure>`_
- `dtool-irods <https://github.com/jic-dtool/dtool-irods>`_
- `dtool-smb <https://github.com/IMTEK-Simulation/dtool-smb>`_