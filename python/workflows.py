from argo.workflows.dsl.templates import V1Container
from argo.workflows.dsl import Workflow
from argo.workflows.dsl import template


class PythonWorkflow(Workflow):

    entrypoint = "whalesay"
    service_account_name = "argo"

    @template
    def whalesay(self) -> V1Container:
        container = V1Container(
            image="docker/whalesay:latest",
            name="whalesay",
            command=["cowsay"],
            args=["hello world"]
        )

        return container
