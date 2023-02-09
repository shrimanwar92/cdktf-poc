from cdktf import TerraformHclModule
from constructs import Construct

from cdktf_cdktf_provider_aws import s3_bucket as s3
from constructs import Construct


class CXVpc():
    def __init__(self, provider, **opts):
        self.provider = provider
        self.opts = opts

    def create(self, stack: Construct):
        return TerraformHclModule(stack, "vpc",
                                  source="terraform-aws-modules/vpc/aws",
                                  variables={
                                      "name": self.opts['name'],
                                      "cidr": "10.0.0.0/16",
                                      "azs": ["us-west-2a", "us-west-2b", "us-west-2c"],
                                      "private_subnets": ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
                                      "public_subnets": ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],
                                      "enable_nat_gateway": True,
                                  },
                                  providers=[self.provider]
                                  )
