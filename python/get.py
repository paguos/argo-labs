from loguru import logger

from argo.workflows.client import WorkflowServiceApi
from argo.workflows.client.rest import ApiException


def get_workflow(namespace, name):
    logger.debug(f"Getting workflow '{worklow_name}' ...")
    try:
        api_response = api_instance.get_workflow(namespace, worklow_name)
        logger.debug(f"'{worklow_name}' workflow retrived!'")
        return api_response
    except ApiException as e:
        print("Exception when calling WorkflowServiceApi->delete_workflow: %s\n" % e)


namespace = "argo"
worklow_name = "python-workflow"
api_instance = WorkflowServiceApi()

wf = get_workflow(namespace, worklow_name)
while wf.status.phase != "Succeeded":
    wf = get_workflow(namespace, worklow_name)

logger.info(f"Worklow phase: {wf.status.phase}")
