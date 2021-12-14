echo "Cloning Repo...."
git clone https://github.com/Judson-web/ID-Bot /ID-Bot
cd /ID-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 motech.py
