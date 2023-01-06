class Command:
  def __init__(self, command: str, description: str, args_len: int = 0):
    self.__command = command
    self.__description = description
    self.__args_len = args_len

  def get_command(self) -> str:
    return self.__command

  def get_description(self) -> str:
    return self.__description

  def validate_args_len(self, args: list[str]) -> None:
    if len(args) < self.__args_len:
      raise Exception("Invalid args length")

  def handle(self, args: list[str]) -> None:
    raise NotImplemented()


class HelpCommand(Command):
  def __init__(self, cli_name: str):
    super().__init__("help", "Show commands descriptions")
    self.__cli_name = cli_name
    self.__commands = []

  def attach_commands(self, commands: list[Command]) -> None:
    self.__commands = commands

  def handle(self, _) -> None:
    print(self.__cli_name)
    for command in self.__commands:
      print(f"\t{command.get_command()}: {command.get_description()}")
