from robocorp import workitems
from robocorp.tasks import task

from workflow.process import Process


@task
def run():
    for data in workitems.Inputs():
        process = Process(
            data.payload[0]["product"],
            data.payload[0]["email"],
            data.payload[0]["pass"],
            data.payload[0]["send_to"],
            data.payload[0]["title"],
            data.payload[0]["body"],
            data.payload[0]["file"],
        )
        process.start()
