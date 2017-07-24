import requests
import json
import sys
import time

###<#
coin='etc'
rewardurl='https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=ETH&tsym=BTC'
rewardreq=requests.get(rewardurl).json()
reward = (rewardreq['Data']['BlockReward'])
print(reward)
#>
###
#Get statistic for a given coin
def getstats(coin,hash):

 rewardurl='https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=ETH&tsym=BTC'
 rewardreq=requests.get(rewardurl).json()
 reward = (rewardreq['Data']['BlockReward'])

 url = 'http://coinmarketcap-nexuist.rhcloud.com/api/'
 r = requests.get('https://etherchain.org/api/basic_stats').json()
 def avg(l): return sum([i for i in l])/float(len(l))
 blockTimeAvg = avg([int(b['blockTime']) for b in r['data']['blocks']])
 difficultyAvg = avg([int(b['difficulty']) for b in r['data']['blocks']])
 r = requests.get(url + coin).json()

 data = {
    'blockTime': blockTimeAvg,
    'difficulty': difficultyAvg,
    'priceUsd': float(r['price']['usd']),
    'lastUpdate': time.time(),
    'blockReward' : reward,
    'coinsOut' : ((hash * reward) / difficultyAvg) * 60 * 60
 }

 print('ethereumStates = ' + json.dumps(data) + ';')
###
getstats('eth',30000000)
#
