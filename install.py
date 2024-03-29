#! /usr/bin/env python3

import os
import site

NO_SUDO = int(os.getenv("NO_SUDO") or 0)
sudo = "" if bool(NO_SUDO) else "sudo"

BIN_PATH = f"/usr/local/bin/yacli"
LIB_PATH = f"/usr/local/lib/yacli"
ETC_PATH = f"/usr/local/etc/yacli"
PY_LIB_PATH = f"{site.USER_SITE}/yacli"

if __name__ == "__main__":
  print(f"Installing yacli...")

  if os.path.isdir(BIN_PATH):
    os.system(f"{sudo} rm -rf {BIN_PATH}")
  os.system(f"{sudo} cp ./bin/yacli {BIN_PATH}")

  if os.path.isdir(LIB_PATH):
    os.system(f"{sudo} rm -rf {LIB_PATH}")
  os.system(f"{sudo} cp -r ./src {LIB_PATH}")

  if os.path.isdir(ETC_PATH):
    os.system(f"{sudo} rm -rf {ETC_PATH}")
  os.system(f"{sudo} cp -r ./etc {ETC_PATH}")

  if os.path.isdir(PY_LIB_PATH):
    os.system(f"rm -rf {PY_LIB_PATH}")
  os.system(f"mkdir -p {PY_LIB_PATH}/core")
  os.system(f"cp -r ./src/core {PY_LIB_PATH}")
  os.system(f"cp ./src/__init__.py {PY_LIB_PATH}")

  print("Installed successfully!")
