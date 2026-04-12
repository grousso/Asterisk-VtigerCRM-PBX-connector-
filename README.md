# Asterisk-VtigerCRM-PBX-connector-

1) At your CRM PBX configuration page 
fill Vtiger Asterisk App URL with http://pbx-domain:5000 and Outbound with Context	from-internal. Secret for now is useless.


2)You need some Python packages, so run

sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
mkdir ~/asterisk-listener
cd ~/asterisk-listener
pip install pyst2 requests flask flask_cors
python3 -m venv venv
source venv/bin/activate

python3 ./log2crm.py
