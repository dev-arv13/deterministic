from cloud import make_s3_client

def test_client_exists():
    assert make_s3_client is not None
