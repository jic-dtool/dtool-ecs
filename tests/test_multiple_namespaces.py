import os
from . import TEST_SAMPLE_DATA

from . import tmp_uuid_and_uri  # NOQA
from . import tmp_uuid_and_uri_from_second_namespace  # NOQA

def test_basic_workflow_on_first_namespace(tmp_uuid_and_uri):  # NOQA

    uuid, dest_uri = tmp_uuid_and_uri

    from dtoolcore import ProtoDataSet, generate_admin_metadata
    from dtoolcore import DataSet
    from dtoolcore.utils import generate_identifier

    name = "my_dataset"
    admin_metadata = generate_admin_metadata(name)
    admin_metadata["uuid"] = uuid

    sample_data_path = os.path.join(TEST_SAMPLE_DATA)
    local_file_path = os.path.join(sample_data_path, 'tiny.png')

    # Create a minimal dataset
    proto_dataset = ProtoDataSet(
        uri=dest_uri,
        admin_metadata=admin_metadata,
        config_path=None)
    proto_dataset.create()
    proto_dataset.put_item(local_file_path, 'tiny.png')
    proto_dataset.freeze()

    # Read in a dataset
    dataset = DataSet.from_uri(dest_uri)

    expected_identifier = generate_identifier('tiny.png')

    assert expected_identifier in dataset.identifiers
    assert len(dataset.identifiers) == 1


def test_basic_workflow_on_second_namespace(tmp_uuid_and_uri_from_second_namespace):  # NOQA

    uuid, dest_uri = tmp_uuid_and_uri_from_second_namespace

    from dtoolcore import ProtoDataSet, generate_admin_metadata
    from dtoolcore import DataSet
    from dtoolcore.utils import generate_identifier

    name = "my_dataset"
    admin_metadata = generate_admin_metadata(name)
    admin_metadata["uuid"] = uuid

    sample_data_path = os.path.join(TEST_SAMPLE_DATA)
    local_file_path = os.path.join(sample_data_path, 'tiny.png')

    # Create a minimal dataset
    proto_dataset = ProtoDataSet(
        uri=dest_uri,
        admin_metadata=admin_metadata,
        config_path=None)
    proto_dataset.create()
    proto_dataset.put_item(local_file_path, 'tiny.png')
    proto_dataset.freeze()

    # Read in a dataset
    dataset = DataSet.from_uri(dest_uri)

    expected_identifier = generate_identifier('tiny.png')

    assert expected_identifier in dataset.identifiers
    assert len(dataset.identifiers) == 1
