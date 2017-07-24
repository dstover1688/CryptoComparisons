#coin[s] as param
#loop through switch statement
#>>> Do we put the Switch statement here or would we want to keep that logic in the getStats function to return any coins value
##different api's required for some coins
#calculate which coin to mine
##coin to mine=fastest to target coin stack size in 30d?

def calculateCoins([string[]]coins){
  #create an empty object to store the list of coin info
  coinObject = {}
  
  foreach (coin in coins){
    #create an empty object to store the relevant data for each coin as the loop iteerates
    coinValue = {}
  
    switch coin {
      'etc' = {
        #Code for ETC, return coins/day
      }
  
      'ubq' = {
        #Code for UBIQ, return coins/day
      }
  
      default = {
      #Code to scrape API's for $coin, return coins/day
      }
  
  }
 
 #create resultant object
 coinObject+=coinValue
 
  }
 #If object is JSON, we should be able to do a sort by property "CoinProfitability" for all objects and return the highest value. 
 # To do this we should make sure we are storing the values of CoinProf as a Float type in all of the objects and we can use something like JSON sort to get the best coin.
 #do math to sort coins here
 coinObjectSorted = coinObject.sort_keys

#  print('Sorted Coin Object' = ' + json.dumps(coinObject, sort_keys=True) + ';')
}
