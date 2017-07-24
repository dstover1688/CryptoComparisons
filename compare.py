import requests
import json
import sys
import time

###
#whattomine api
#only place i've found with ubiq (UBQ coin) info
coin='Ubiq'
uri='http://www.whattomine.com/coins.json'
r=requests.get(uri).json()
reward= (r['coins'][coin]['block_reward'])
difficulty = (r['coins'][coin]['difficulty'])
print(reward, difficulty)

###
#coinwarz api
coin='etc'
apik='942f61a7fda04a18ba52af7765b3d848'
uri='http://www.coinwarz.com/v1/api/coininformation/?apikey=' + apik + '&cointag=' + coin
r=requests.get(uri).json()
reward=(r['Data']['BlockReward'])
difficulty=(r['Data']['Difficulty'])
print(reward, difficulty)

###
coin='etc'
rewardurl='https://www.cryptocompare.com/api/data/coinsnapshot/?fsym=ETH&tsym=BTC'
rewardreq=requests.get(rewardurl).json()
reward = (rewardreq['Data']['BlockReward'])
print(reward)
#

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
