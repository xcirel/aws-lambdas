from chalice.test import Client
from app import app


def test_s3_handler():
    with Client(app) as client:
        event = client.events.generate_s3_event(
            bucket='aws-lambdas-chalice', key='sheet.xls')
        client.lambda_.invoke('s3_handler', event)
