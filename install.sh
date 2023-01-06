#! /usr/bin/env bash

echo "Installing yacli..."

sudo cp ./bin/yacli /usr/local/bin/yacli

sudo rm -rf /usr/local/lib/yacli
sudo cp -r ./src /usr/local/lib/yacli

echo "Installed successfully!"
