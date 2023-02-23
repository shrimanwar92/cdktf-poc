#import pytest
#from cdktf import Testing
import pytest
import tftest
from pathlib import PurePath

@pytest.fixture
def plan():
    #file_path = Path(__file__).resolve()
    file_path = PurePath('./examples/cdktf.out/stacks/cdktf-project')
    #base_dir = file_path.parent.parent.parent.absolute()
    #tf = tftest.TerraformTest(tfdir=file_path)
    #return tf.setup()
    #return tf.plan(output=True)

def test_outputs(plan):
    """Simple test of the output vars after a terraform plan cmd
    """
    assert plan == 567
    #assert plan.outputs['cloud_run_api_image_name'] == f"{plan.variables['prefix']}-cloudrun-api"