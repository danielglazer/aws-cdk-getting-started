import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_getting_started.cdk_getting_started_stack import CdkGettingStartedStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_getting_started/cdk_getting_started_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkGettingStartedStack(app, "cdk-getting-started")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
