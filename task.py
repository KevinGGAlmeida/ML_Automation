from robocorp import workitems
from robocorp.tasks import task

from workflow.process import Process


@task
def run():
    for data in workitems.Inputs():
        process = Process(
            data.payload["product"],
            data.payload["email"],
            data.payload["pass"],
            data.payload["send_to"],
            data.payload["title"],
            data.payload["body"],
            data.payload["file"],
        )
        process.start()
