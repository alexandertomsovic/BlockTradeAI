# Crypto price checker bot by Alexander Tomsovic

import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore
import sys

def clearpage():
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
  
# Webscraping function for Bitcoin
def btc_prices():
  btc_url='https://crypto.com/price/bitcoin' # URL we use
  btc_response = requests.get(btc_url)
  btc_soup = BeautifulSoup(btc_response.text, 'html.parser') # soup variable parses 
  btc_price = btc_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text # Bitcoin price
  return btc_price

# Webscraping function for Ethereum
def eth_prices(): 
  eth_url = 'https://crypto.com/price/ethereum'
  eth_response = requests.get(eth_url)
  eth_soup = BeautifulSoup(eth_response.text, 'html.parser')
  eth_price = eth_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text # Ethereum price
  return eth_price

# Webscraping function for XRP
def xrp_prices():
  xrp_url = 'https://crypto.com/price/xrp'
  xrp_response = requests.get(xrp_url)
  xrp_soup = BeautifulSoup(xrp_response.text, 'html.parser')
  xrp_price = xrp_soup.find('span', {"class": "chakra-text css-13hqrwd"}).text # Ethereum price
  return xrp_price

# Attributes function price to actual price
btc_price = btc_prices()
eth_price = eth_prices()
xrp_price = xrp_prices()

# Prints prices in terminal
print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + str(btc_price))
print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + str(eth_price))
print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + str(xrp_price))

# price checker

checker = 1

while True:

  print("")
  print(Fore.MAGENTA + str(checker) + Fore.WHITE + " ticks since last price change")
  checker += 1
  sleep(0.001)
  clearpage()
  
  new_btc_prices = btc_prices()
  new_eth_prices = eth_prices()
  new_xrp_prices = xrp_prices()

  if new_eth_prices != eth_prices or new_btc_prices != btc_prices():
    
    btc_price = btc_prices()
    eth_price = eth_prices()
    xrp_price = xrp_prices()
    
    clearpage()
    clearpage()
    clearpage()
    clearpage()
    if btc_price > new_btc_prices: # Bitcoin up / down movement color coder
      print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(btc_price))
    elif btc_price < new_btc_prices:
      print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + Fore.RED + str(btc_price))
    else:
        print(Fore.LIGHTYELLOW_EX + "Bitcoin " + Fore.WHITE + "is trading at " + Fore.WHITE + str(btc_price)) 

    if eth_price > new_eth_prices: # Ethereum up / down movement color coder
      print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(eth_price))
    elif eth_price < new_eth_prices:
      print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + Fore.RED + str(eth_price))
    else:
      print(Fore.LIGHTCYAN_EX + "Ethereum " + Fore.WHITE + "is trading at " + Fore.WHITE + str(eth_price))

    if xrp_price > new_xrp_prices: # XRP up / down movement color coder
      print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + Fore.LIGHTGREEN_EX + str(xrp_price))
    elif xrp_price < new_xrp_prices:
      print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + Fore.RED + str(xrp_price))
    else:
      print(Fore.LIGHTBLACK_EX + "XRP " + Fore.WHITE + "is trading at " + Fore.WHITE + str(xrp_price))

    checker = 1
  sleep(1)
  
