from cdktf_cdktf_provider_aws import s3_bucket as s3
from constructs import Construct


class CXS3Bucket():
    def __init__(self, **opts):
        self.opts = opts

    def create(self, stack: Construct) -> s3.S3Bucket:
        return s3.S3Bucket(stack, f"s3-{self.opts['name']}",
                           bucket=self.opts['name'],
                           tags=self.opts['tags'],
                           policy=str(self.opts['policy'])
                           )
