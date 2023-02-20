#! /usr/bin/env python3

import os
import site

NOT_USE_SUDO = bool(os.getenv("NOT_USE_SUDO")) or False
sudo = "" if NOT_USE_SUDO else "sudo"

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
    os.system(f"{sudo} rm -rf {PY_LIB_PATH}")
  os.system(f"{sudo} mkdir -p {PY_LIB_PATH}/core")
  os.system(f"{sudo} cp -r ./src/core {PY_LIB_PATH}/core")
  os.system(f"{sudo} cp ./src/__init__.py {PY_LIB_PATH}")

  print("Installed successfully!")
