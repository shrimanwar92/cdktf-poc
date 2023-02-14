from imports.vpc import Vpc
from constructs import Construct


class CXvpc():
    stack: Construct

    def __init__(self, stack: Construct, **opts):
        self.stack = stack
        self.opts = opts

    def create(self) -> Vpc:
        return Vpc(self.stack, "my-vpc",
                   name=self.opts['name'],
                   cidr=str(self.opts['cidr']),
                   azs=list(self.opts['azs']),
                   private_subnets=list(self.opts['private_subnets']),
                   public_subnets=list(self.opts['public_subnets']),
                   enable_nat_gateway=self.opts['enable_nat_gateway']
                   )
