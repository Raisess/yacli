import sys

from core.command import Command, HelpCommand

class CLI:
  def __init__(self, cli_name: str, commands: list[Command]):
    self.__cli_name = cli_name
    self.__commands = {}

    help_command = HelpCommand(cli_name)
    commands.append(help_command)
    help_command.attach_commands(commands)

    for command in commands:
      self.__commands[command.get_command()] = command

  def handle(self, args: list[str] = sys.argv[1:]) -> None:
    command_name = args[0]
    command: Command = self.__commands.get(command_name)
    if not command:
      raise Exception("Invalid command")

    command.validate_args_len(args[1:])
    command.handle(args[1:])
