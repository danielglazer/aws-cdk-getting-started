from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    RemovalPolicy,
    aws_s3 as s3
)
from constructs import Construct

class CdkGettingStartedStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "MyFirstBucket",
          versioned=True,
          removal_policy=RemovalPolicy.DESTROY,
          auto_delete_objects=True)
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkGettingStartedQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
