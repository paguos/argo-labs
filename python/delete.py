from loguru import logger

from argo.workflows.client import WorkflowServiceApi
from argo.workflows.client.rest import ApiException

namespace = "argo"
worklow_name = "python-workflow"
api_instance = WorkflowServiceApi()

logger.info(f"Deleting workflow '{worklow_name}' ...")

try:
    api_response = api_instance.delete_workflow(namespace, worklow_name)
    logger.info(f"'{worklow_name}' workflow deleted!'")
except ApiException as e:
    print("Exception when calling WorkflowServiceApi->delete_workflow: %s\n" % e)
