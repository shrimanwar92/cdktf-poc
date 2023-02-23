from imports.aws.s3_bucket import S3Bucket
from constructs import Construct
from cdktf import TerraformOutput


class CXS3Bucket():
    def __init__(self, stack: Construct, **opts):
        self.stack = stack
        self.opts = opts

    def create(self) -> S3Bucket:
        bucket = S3Bucket(self.stack, f"s3-{self.opts['name']}",
                        bucket=self.opts['name'],
                        tags=self.opts['tags']
                        )
    
        TerraformOutput(
            self.stack,
            "bucket_arn",
            value=bucket.arn,
        )

        return bucket