#!/usr/bin/env python
from constructs import Construct
from cdktf import TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        self.provider = AwsProvider(self, "AWS", region="us-west-1")
