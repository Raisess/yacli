import os

from core.command import Command
from util.boilerplate_loader import BoilerplateLoader

class CreateCLICommand(Command):
  def __init__(self):
    super().__init__("create", "Create a new CLI application.", 1)

  def handle(self, args: list[str]) -> None:
    cli_name = args[0]

    print(f"Creating new {cli_name} cli...")

    if not os.path.isdir(cli_name):
      os.mkdir(cli_name)

    required_folders = ["bin", "src"]
    for folder in required_folders:
      path = f"{cli_name}/{folder}"
      if not os.path.isdir(path):
        os.mkdir(path)

    required_files = [
      ("install.sh", BoilerplateLoader.Load("install.sh", { "cli_name": cli_name }), "chmod +x"),
      (f"bin/{cli_name}", BoilerplateLoader.Load("bin", { "cli_name": cli_name }), "chmod +x"),
      (f"src/main.py", BoilerplateLoader.Load("main.py", { "cli_name": cli_name }), "chmod +x")
    ]
    for file in required_files:
      path = f"{cli_name}/{file[0]}"
      if not os.path.isfile(path):
        with open(path, "w") as opened_file:
          opened_file.write(file[1].strip())
        if len(file) == 3:
          os.system(f"{file[2]} {path}")

    print("Created!")
