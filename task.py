import os

from workflow.process import Process


def run():
    process = Process(
        "notebook-gamer",
        "automationdeveloper94@gmail.com",
        "opqv ezjq kywq vwax",
        "gabriel_almeida50@yahoo.com.br",
        "Arquivo de validacoes",
        "Segue em anexo arquivo de validações",
        f"{os.getcwd()}/{'notebook-gamer.xlsx'}",
    )
    process.start()


run()
