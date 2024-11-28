import sys

sys.path.insert(0, "..")
from libraries.request import Request
from libraries.stmp import Gmail


class Process:
    def __init__(
        self,
        product_name,
        whoami,
        app_pass,
        send_to,
        title,
        body_msg,
        file_path,
    ):
        self.request = Request(product_name)
        self.email = Gmail(
            whoami, app_pass, send_to, title, body_msg, file_path
        )

    def start(self):
        self.request.get_list_of_products()
        self.request.filtering_data()
        self.request.creating_df()
        self.email.login()
        self.email.config_message()
        self.email.attach_file()
        self.email.send_email()
