#!/usr/bin/env python
import sys

sys.path.append("..")
from cdktf import App, TerraformOutput
from constructs import Construct
from lib.s3 import CXS3Bucket
from lib.vpc import CXVpc
from main import MyStack


class TestS3Lib(MyStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        s3_tags = {
            "Team": "Devops",
            "Company": "Tavisca"
        }
        s3_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": [
                        "s3:GetObject"
                    ],
                    "Resource": "*"
                }
            ]
        }

        my_bucket = CXS3Bucket(
            name="my-test-bucket",
            policy=s3_policy,
            tags=s3_tags
        ).create(self)

        vpc = CXVpc(
            self.provider,
            name="my-vpc"
        ).create(self)

        TerraformOutput(
            self,
            "bucket_name",
            value=my_bucket.bucket,
        )

        TerraformOutput(
            self,
            "bucket_arn",
            value=my_bucket.arn,
        )

        # TerraformOutput(
        #     self,
        #     "vpc_id",
        #     value=vpc.vpc_id,
        # )


app = App()
TestS3Lib(app, "cdktf-project")
app.synth()
