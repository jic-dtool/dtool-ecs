"""ECSStorageBroker"""

import copy

try:
    from urlparse import urlunparse
except ImportError:
    from urllib.parse import urlunparse

from boto3.session import Session

from dtool_s3.storagebroker import S3StorageBroker, _STRUCTURE_PARAMETERS

from dtoolcore.utils import (
    get_config_value,
    generous_parse_uri,
    DEFAULT_CACHE_PATH,
)

from dtool_ecs import __version__

_ECS_STRUCTURE_PARAMETERS = copy.deepcopy(_STRUCTURE_PARAMETERS)
_ECS_STRUCTURE_PARAMETERS["storage_broker_version"] = __version__


class ECSStorageBroker(S3StorageBroker):

    key = "ecs"

    def __init__(self, uri, config_path=None):

        parse_result = generous_parse_uri(uri)

        self.bucket = parse_result.netloc
        uuid = parse_result.path[1:]

        self.uuid = uuid

        ecs_endpoint = get_config_value("DTOOL_ECS_ENDPOINT")
        ecs_access_key_id = get_config_value("DTOOL_ECS_ACCESS_KEY_ID")
        ecs_secret_access_key = get_config_value("DTOOL_ECS_SECRET_ACCESS_KEY")

        session = Session(
            aws_access_key_id=ecs_access_key_id,
            aws_secret_access_key=ecs_secret_access_key
        )

        self.s3resource = session.resource('s3', endpoint_url=ecs_endpoint)
        self.s3client = session.client('s3', endpoint_url=ecs_endpoint)

        self._structure_parameters = _ECS_STRUCTURE_PARAMETERS
        self.dataset_registration_key = 'dtool-{}'.format(self.uuid)
        self._structure_parameters["dataset_registration_key"] = self.dataset_registration_key  # NOQA

        self.data_key_prefix = self._generate_key_prefix("data_key_infix")
        self.fragments_key_prefix = self._generate_key_prefix(
            "fragment_key_infix"
        )
        self.overlays_key_prefix = self._generate_key_prefix(
            "overlays_key_infix"
        )

        self.http_manifest_key = self._generate_key("http_manifest_key")

        self._s3_cache_abspath = get_config_value(
            "DTOOL_CACHE_DIRECTORY",
            config_path=config_path,
            default=DEFAULT_CACHE_PATH
        )

    @classmethod
    def list_dataset_uris(cls, base_uri, config_path):
        """Return list containing URIs with base URI."""
        uri_list = []

        ecs_endpoint = get_config_value("DTOOL_ECS_ENDPOINT")
        ecs_access_key_id = get_config_value("DTOOL_ECS_ACCESS_KEY_ID")
        ecs_secret_access_key = get_config_value("DTOOL_ECS_SECRET_ACCESS_KEY")

        session = Session(
            aws_access_key_id=ecs_access_key_id,
            aws_secret_access_key=ecs_secret_access_key
        )

        resource = session.resource('s3', endpoint_url=ecs_endpoint)

        parse_result = generous_parse_uri(base_uri)
        bucket_name = parse_result.netloc

        bucket = resource.Bucket(bucket_name)

        for obj in bucket.objects.filter(Prefix='dtool').all():
            uuid = obj.key.split('-', 1)[1]
            uri = cls.generate_uri(None, uuid, base_uri)

            storage_broker = cls(uri, config_path)
            if storage_broker.has_admin_metadata():
                uri_list.append(uri)

        return uri_list

    @classmethod
    def generate_uri(cls, name, uuid, base_uri):

        scheme, netloc, path, _, _, _ = generous_parse_uri(base_uri)
        assert scheme == 'ecs'

        # Force path (third component of tuple) to be the dataset UUID
        uri = urlunparse((scheme, netloc, uuid, _, _, _))

        return uri

    def http_enable(self):
        raise(AttributeError())

    def _list_historical_readme_keys(self):
        # This method is used to test the
        # BaseStorageBroker.readme_update method.
        prefix = self.get_readme_key() + "-"
        historical_readme_keys = []

        bucket = self.s3resource.Bucket(self.bucket)
        for obj in bucket.objects.filter(Prefix=prefix).all():
            historical_readme_keys.append(obj.key)

        return historical_readme_keys
