from robocorp import workitems
from robocorp.tasks import task

from workflow.process import Process


@task
def run():
    for data in workitems.Inputs():
        print(data.payload)
        process = Process(
            data.payload["payload"]["product"],
            data.payload["payload"]["email"],
            data.payload["payload"]["pass"],
            data.payload["payload"]["send_to"],
            data.payload["payload"]["title"],
            data.payload["payload"]["body"],
            data.payload["payload"]["file"],
        )
        process.start()
