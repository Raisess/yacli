#! /usr/bin/env python3

from core.cli import CLI
from commands.create_cli_command import CreateCLICommand

if __name__ == "__main__":
  cli = CLI("yacli", [CreateCLICommand()])
  cli.handle()
