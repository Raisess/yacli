# Yet Another CLI

Just another CLI library.

### Setup

```shell
$ ./install.sh
```

### How to use?

#### Creating a new CLI:

```shell
$ yacli create my-cli
$ cd my-cli
```

All required files will be created by `yacli`, just start editing `my-cli/src/main.py`:

```py
#! /usr/bin/env python3

from yacli import CLI, Command

class TestCommand(Command):
  def __init__(self):
    super().__init__("my-command", "description", args_len=0)

  def handle(self, args: list[str]) -> None:
    print("Hello, world!")


if __name__ == "__main__":
  cli = CLI("my-cli", [TestCommand()])
  cli.handle()
```

and run `my-cli/install.sh`.

That's all!
