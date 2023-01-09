#! /usr/bin/env bash

echo "Installing yacli..."

BIN_PATH=/usr/local/bin/yacli
LIB_PATH=/usr/local/lib/yacli
PY_USER_SITE=$(python3 -m site --user-site)
PY_LIB_PATH=$PY_USER_SITE/yacli

sudo cp ./bin/yacli $BIN_PATH

sudo rm -rf $LIB_PATH
sudo cp -r ./src $LIB_PATH
sudo rm -rf $PY_LIB_PATH
sudo mkdir -p $PY_LIB_PATH/core
sudo cp -r ./src/core/*.py $PY_LIB_PATH/core
sudo cp -r ./src/__init__.py $PY_LIB_PATH

echo "Installed successfully!"
