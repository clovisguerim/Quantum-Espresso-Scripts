#! \bin\python
'''
This script sends a post to telegram API
'''
import sys
import requests

msg = str(sys.argv[1])
base_url = "https://api.telegram.org/bot1813408039:AAHC_J4IO0iXkm8oJfQJ9Rg9o-Xe7sQpwB0/sendMessage?chat_id=-466952466&text={}".format(msg)
requests.get(base_url)
