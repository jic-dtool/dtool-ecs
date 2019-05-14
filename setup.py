from setuptools import setup

url = "https://github.com/jic-dtool/dtool-ecs"
version = "0.3.0"
readme = open('README.rst').read()

setup(
    name="dtool-ecs",
    packages=["dtool_ecs"],
    version=version,
    description="Add ECS S3 support to dtool",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    download_url="{}/tarball/{}".format(url, version),
    install_requires=[
        "click",
        "dtoolcore>=3.10",
        "dtool_cli",
        "boto3",
        "dtool-s3",
    ],
    entry_points={
        "dtool.storage_brokers": [
            "ECSStorageBroker=dtool_ecs.storagebroker:ECSStorageBroker",
        ],
    },
    license="MIT"
)
