import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pyfiglet import figlet_format
def get_my_ip():
    ip_addr = requests.get("https://api.ipify.org").text
    respo = requests.get(f"http://ip-api.com/json/{ip_addr}?lang=r").json()
    return respo

ipinfo = get_my_ip()
print(figlet_format("IP INFO"))

print(f'IP: {ipinfo['query']}\nStatus: {ipinfo['status']}\nCity: {ipinfo['city']}\nRegion name: {ipinfo['regionName']}\nCountry: {ipinfo['country']}\nTimezone: {ipinfo['timezone']}')  