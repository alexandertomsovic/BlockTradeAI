# Crypto Price tracker by Alexander Tomsovic
# linktr.ee/alextomsovic
#
# Please note: 
# The crypto checker has BETA features that allow users to recieve SMS messages about price updates and changes. 
# To recieve these updates, I am making a FREE service that will be released by late 2022. In the meantime, 
# you can get your own (1) number, (2) account_sid, and (3) auth token at https://www.twilio.com/referral/CaqA6u
# Enter (2) and (3) into lines 28 and 29 of this file. Enter (1) into line 204! 
#
# If you do not wish to use SMS updates at this time and only want CLI updates:
# Comment out lines 28 - 31, 202 - 206, and 272 - 273
import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore
import sys
from twilio.rest import Client
from datetime import datetime

# Date for SMS messaging

current_day = datetime.now()
current_time = current_day.strftime("%H:%M:%S")
current_day_formatted = str(current_day.month) + "/" + str(current_day.day) + "/" + str(current_day.year) + " " + str(current_time) + " EST | "

# TWilio auth codes SMS messaging

account_sid = "twilio account_sid here"
auth_token  = "twilio auth token here"

client = Client(account_sid, auth_token)


# Clearpage Function

def clearpage():
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')

def clearnine():
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()
  clearpage()

# Webscraping function for Bitcoin
  
def btc_prices():
  btc_url='https://crypto.com/price/bitcoin' # URL we use
  btc_response = requests.get(btc_url)
  btc_soup = BeautifulSoup(btc_response.text, 'html.parser') # soup variable parses 
  btc_price = btc_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text 
  return btc_price

def btc_24h():
  btc_24h_url = 'https://www.binance.com/en/price/bitcoin'
  btc_24h_response = requests.get(btc_24h_url)
  btc_24h_soup = BeautifulSoup(btc_24h_response.text, 'html.parser')
  btc_24h_change = btc_24h_soup.find('div', {"class": "css-4j2do9"}).text
  return btc_24h_change
# Webscraping function for Ethereum
  
def eth_prices(): 
  eth_url = 'https://crypto.com/price/ethereum'
  eth_response = requests.get(eth_url)
  eth_soup = BeautifulSoup(eth_response.text, 'html.parser')
  eth_price = eth_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text 
  return eth_price

def eth_24h():
  eth_24h_url = 'https://coindesk.com/price/ethereum'
  eth_24h_response = requests.get(eth_24h_url)
  eth_24h_soup = BeautifulSoup(eth_24h_response.text, 'html.parser')
  eth_24h_change = eth_24h_soup.find('h6', {"class": "typography__StyledTypography-owin6q-0 hZxwDe"}).text
  return eth_24h_change
  
# Webscraping function for XRP
  
def xrp_prices():
  xrp_url = 'https://crypto.com/price/xrp'
  xrp_response = requests.get(xrp_url)
  xrp_soup = BeautifulSoup(xrp_response.text, 'html.parser')
  xrp_price = xrp_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text 
  return xrp_price

def xrp_24h():
  xrp_24h_url = 'https://www.coindesk.com/price/xrp/'
  xrp_24h_response = requests.get(xrp_24h_url)
  xrp_24h_soup = BeautifulSoup(xrp_24h_response.text, 'html.parser')
  xrp_24h_change = xrp_24h_soup.find('h6', {"class": "typography__StyledTypography-owin6q-0 hZxwDe"}).text
  return xrp_24h_change
  
# Webscraping function for Tether
  
def usdt_prices():
  usdt_url = 'https://crypto.com/price/tether'
  usdt_response = requests.get(usdt_url)
  usdt_soup = BeautifulSoup(usdt_response.text, 'html.parser')
  usdt_price = usdt_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text
  return usdt_price

def usdt_24h():
  usdt_24h_url = 'https://www.coindesk.com/price/tether/'
  usdt_24h_response = requests.get(usdt_24h_url)
  usdt_24h_soup = BeautifulSoup(usdt_24h_response.text, 'html.parser')
  usdt_24h_change = usdt_24h_soup.find('h6', {"class": "typography__StyledTypography-owin6q-0 hZxwDe"}).text
  return usdt_24h_change

# Webscraping function for Litecoin

def ltc_prices():
  ltc_url = 'https://crypto.com/price/litecoin'
  ltc_response = requests.get(ltc_url)
  ltc_soup = BeautifulSoup(ltc_response.text, 'html.parser')
  ltc_price = ltc_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text
  return ltc_price

def ltc_24h():
  ltc_24h_url = 'https://coindesk.com/price/litecoin'
  ltc_24h_response = requests.get(ltc_24h_url)
  ltc_24h_soup = BeautifulSoup(ltc_24h_response.text, 'html.parser')
  ltc_24h_change = ltc_24h_soup.find('h6', {"class": "typography__StyledTypography-owin6q-0 hZxwDe"}).text
  return ltc_24h_change
  
# Attributes function price to actual price
  
btc_price = btc_prices()
eth_price = eth_prices()
xrp_price = xrp_prices()
usdt_price = usdt_prices()
ltc_price = ltc_prices()

# 24 Hour price percentage changes

btc_24h_change = btc_24h()
eth_24h_change = eth_24h()
xrp_24h_change = xrp_24h()
usdt_24h_change = usdt_24h()
ltc_24h_change = ltc_24h()

# Prints prices in terminal

print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + str(btc_price) + " | 24H checking...")
print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + str(eth_price) + " | 24H checking...")
print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + str(xrp_price) + " | 24H checking...")
print(Fore.GREEN + "Tether " + Fore.WHITE + "is trading at " + str(usdt_price) + " | 24H checking...")
print(Fore.BLUE + "Litecoin " + Fore.WHITE + "is trading at " + str(ltc_price) + " | 24H checking...")

# price checker

checker = 1

while True:

  print("")
  print(Fore.MAGENTA + str(checker) + Fore.WHITE + " ticks since last price change")
  checker += 1
  sleep(0.001)
  clearpage()

  # Price currents 
  
  new_btc_prices = btc_prices()
  new_eth_prices = eth_prices()
  new_xrp_prices = xrp_prices()
  new_usdt_prices = usdt_prices()
  new_ltc_prices = ltc_prices()

  # 24 Hour currents

  new_btc_24h = btc_24h()
  new_eth_24h = eth_24h()
  new_xrp_24h = xrp_24h()
  new_usdt_24h = usdt_24h()
  new_ltc_24h = ltc_24h()

  if new_eth_prices != eth_prices or new_btc_prices != btc_prices():

    # Price Updates
    
    btc_price = btc_prices()
    eth_price = eth_prices()
    xrp_price = xrp_prices()
    usdt_price = usdt_prices()
    ltc_price = ltc_prices()

    # 24 Hour updates
    
    btc_24h_change = btc_24h()
    eth_24h_change = eth_24h()
    xrp_24h_change = xrp_24h()
    usdt_24h_change  = usdt_24h()
    ltc_24h_change = ltc_24h()

    # Sending BTC price to SMS number

    message = client.messages.create(
    to = "+15106790082", 
    from_ = "your number",
    body = str(current_day_formatted) + "BTC | " + str(btc_price)
    )

    # Color coding 24 Hour percentage changes 

    if btc_24h_change.startswith('-'): # Bitcoin color adjustment
      color_btc_24h_change = Fore.RED + str(btc_24h_change)
    else: 
      color_btc_24h_change = Fore.LIGHTGREEN_EX + str(btc_24h_change)
      
    if eth_24h_change.startswith('-'): # Ethereum color adjustment
      color_eth_24h_change = Fore.RED + str(eth_24h_change)
    else: 
      color_eth_24h_change = Fore.LIGHTGREEN_EX + str(eth_24h_change)

    if xrp_24h_change.startswith('-'): # XRP color adjustment
      color_xrp_24h_change = Fore.RED + str(xrp_24h_change)
    else: 
      color_xrp_24h_change = Fore.LIGHTGREEN_EX + str(xrp_24h_change)

    if usdt_24h_change.startswith('-'): # Tether color adjustment
      color_usdt_24h_change = Fore.RED + str(usdt_24h_change)
    else: 
      color_usdt_24h_change = Fore.LIGHTGREEN_EX + str(usdt_24h_change)
      
    if ltc_24h_change.startswith('-'): # Litecoin color adjustment
      color_ltc_24h_change = Fore.RED + str(ltc_24h_change)
    else: 
      color_ltc_24h_change = Fore.LIGHTGREEN_EX + str(ltc_24h_change)
    
    clearnine()
    
    if btc_price > new_btc_prices: # Bitcoin up / down movement color coder
      print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(btc_price) + Fore.WHITE + " | 24H/" + str(color_btc_24h_change.replace("+","")))
    elif btc_price < new_btc_prices:
      print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + Fore.RED + str(btc_price) + Fore.WHITE + " | 24H/" + str(color_btc_24h_change.replace("+","")))
    else:
        print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + Fore.WHITE + str(btc_price) + Fore.WHITE + " | 24H/" + str(color_btc_24h_change.replace("+",""))) 

    if eth_price > new_eth_prices: # Ethereum up / down movement color coder
      print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(eth_price) + Fore.WHITE + " | 24H/" + str(color_eth_24h_change))
    elif eth_price < new_eth_prices:
      print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + Fore.RED + str(eth_price) + Fore.WHITE + " | 24H/" + str(color_eth_24h_change))
    else:
      print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + Fore.WHITE + str(eth_price) + Fore.WHITE + " | 24H/" + str(color_eth_24h_change))

    if xrp_price > new_xrp_prices: # XRP up / down movement color coder
      print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(xrp_price) + Fore.WHITE + " | 24H/" + str(color_xrp_24h_change))
    elif xrp_price < new_xrp_prices:
      print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + Fore.RED + str(xrp_price) + Fore.WHITE + " | 24H/" + str(color_xrp_24h_change))
    else:
      print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + Fore.WHITE + str(xrp_price) + Fore.WHITE + " | 24H/" + str(color_xrp_24h_change))

    if usdt_price > new_usdt_prices: # Tether up / down movement color coder
      print(Fore.GREEN + "Tether " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(usdt_price) + Fore.WHITE + " | 24H/" + str(color_usdt_24h_change))
    elif usdt_price < new_usdt_prices:
      print(Fore.GREEN + "Tether " + Fore.WHITE + "is trading at " + Fore.RED + str(usdt_price) + Fore.WHITE + " | 24H/" + str(color_usdt_24h_change))
    else:
      print(Fore.GREEN + "Tether " + Fore.WHITE + "is trading at " + Fore.RED + str(usdt_price) + Fore.WHITE + " | 24H/" + str(color_usdt_24h_change))

    if ltc_price > new_ltc_prices: # Litecoin up / down movement color coder
      print(Fore.BLUE + "Litecoin " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(ltc_price) + Fore.WHITE + " | 24H/" + str(color_ltc_24h_change))
    elif ltc_price < new_ltc_prices:
      print(Fore.BLUE + "Litecoin " + Fore.WHITE + "is trading at " + Fore.RED + str(ltc_price) + Fore.WHITE + " | 24H/" + str(color_ltc_24h_change))
    else:
      print(Fore.BLUE + "Litecoin " + Fore.WHITE + "is trading at " + Fore.WHITE + str(ltc_price) + Fore.WHITE + " | 24H/" + str(color_ltc_24h_change))

    print(Fore.LIGHTGREEN_EX + "\nSMS " + Fore.WHITE + "ID: ")
    print(message.sid)
    checker = 1
  sleep(1)
  
