from loguru import logger

from argo.workflows.client import WorkflowServiceApi, V1alpha1WorkflowCreateRequest
from argo.workflows.client.rest import ApiException

from workflows import PythonWorkflow

wf = PythonWorkflow()

logger.info(f"Submiting workflow '{wf.name}' ...")
api_instance = WorkflowServiceApi()
namespace = 'argo'
body = V1alpha1WorkflowCreateRequest(
    namespace=namespace,
    workflow=wf
)

try:
    api_response = api_instance.create_workflow(namespace, body)
    logger.info(f"'{wf.name}' workflow submitted!")
except ApiException as e:
    logger.error(e)
