# Asterisk-VtigerCRM-PBX-connector-

You need some Python packages, so run



sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
mkdir ~/asterisk-listener
cd ~/asterisk-listener
pip install pyst2 requests flask flask_cors
source venv/bin/activate

python3 ./log2crm.py
