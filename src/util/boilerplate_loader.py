class BoilerplateLoader:
  @staticmethod
  def Load(path: str, params: dict[str, str]) -> str:
    file = open(f"/usr/local/etc/yacli/boilerplates/{path}.bp", "r")
    content = file.read()
    file.close()

    for param in dict.items(params):
      content = content.replace("{" + param[0] + "}", param[1])

    return content.strip()
