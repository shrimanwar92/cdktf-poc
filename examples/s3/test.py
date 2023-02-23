#!/usr/bin/env python
import sys

sys.path.append("../..")
from cdktf import App, TerraformOutput
from constructs import Construct
from lib.s3 import CXS3Bucket
#from lib.vpc import CXvpc
from main import MyStack
#from operator import itemgetter


class TestS3Lib(MyStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        s3_tags = {
            "Team": "Devops",
            "Company": "Tavisca"
        }

        my_bucket = CXS3Bucket(self,
                               name="my-test-bucket-nilays-1235432",
                               tags=s3_tags
                               ).create()

        # vpc = CXvpc(self,
        #             name="my-vpc",
        #             cidr="10.0.0.0/16",
        #             azs=['us-west-2a', 'us-west-2b', 'us-west-2c'],
        #             private_subnets=['10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24'],
        #             public_subnets=['10.0.101.0/24', '10.0.102.0/24', '10.0.103.0/24'],
        #             enable_nat_gateway=True
        #             ).create()

        # TerraformOutput(
        #     self,
        #     "vpc_id",
        #     value=vpc.vpc_id_output,
        # )

        TerraformOutput(
            self,
            "bucket_name",
            value=my_bucket.bucket,
        )


app = App()
TestS3Lib(app, "cdktf-project")
app.synth()
