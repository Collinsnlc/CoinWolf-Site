from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/news')
def news():
    return render_template('news.html') 

@app.route('/projects')
def projects():
    api_requests = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    api = json.loads(api_requests.content)
    btcname = api[0]['name']
    btcsymbol = api[0]['symbol']
    btcprice = api[0]['current_price']
    btc_msupply = api[0]['max_supply']
    btcmcap = api[0]['market_cap']
    btcchange1 = api[0]['price_change_percentage_24h']
    btcchange2 = api[0]['price_change_24h'] 
    btcrank = api[0]["market_cap_rank"]
    #eth
    ethname = api[1]['name']
    ethsymbol = api[1]['symbol']
    ethprice = api[1]['current_price']
    eth_msupply = api[1]['max_supply']
    ethmcap = api[1]['market_cap']
    ethchange1 = api[1]['price_change_percentage_24h']
    ethchange2 = api[1]['price_change_24h']
    ethrank = api[1]['market_cap_rank']

    #bnb
    bnbname = api[2]['name']
    bnbsymbol = api[2]['symbol']
    bnbprice = api[2]['current_price']
    bnb_msupply = api[2]['max_supply']
    bnbmcap = api[2]['market_cap']
    bnbchange1 = api[2]['price_change_percentage_24h']
    bnbchange2 = api[2]['price_change_24h']
    bnbrank = api[2]['market_cap_rank']

    #ada
    adaname = api[3]['name']
    adasymbol = api[3]['symbol']
    adaprice = api[3]['current_price']
    ada_msupply = api[3]['max_supply']
    adamcap = api[3]['market_cap']
    adachange1 = api[3]['price_change_percentage_24h']
    adachange2 = api[3]['price_change_24h']
    adarank = api[3]['market_cap_rank']

    #c5
    c5name = api[4]['name']
    c5symbol = api[4]['symbol']
    c5price = api[4]['current_price']
    c5_msupply = api[4]['max_supply']
    c5mcap = api[4]['market_cap']
    c5change1 = api[4]['price_change_percentage_24h']
    c5change2 = api[4]['price_change_24h']
    c5rank = api[4]['market_cap_rank']

    #c6
    c6name = api[5]['name']
    c6symbol = api[5]['symbol']
    c6price = api[5]['current_price']
    c6_msupply = api[5]['max_supply']
    c6mcap = api[5]['market_cap']
    c6change1 = api[5]['price_change_percentage_24h']
    c6change2 = api[5]['price_change_24h']
    c6rank = api[5]['market_cap_rank']

    #c7
    c7name = api[6]['name']
    c7symbol = api[6]['symbol']
    c7price = api[6]['current_price']
    c7_msupply = api[6]['max_supply']
    c7mcap = api[6]['market_cap']
    c7change1 = api[6]['price_change_percentage_24h']
    c7change2 = api[6]['price_change_24h']
    c7rank = api[6]['market_cap_rank']

    #c8
    c8name = api[7]['name']
    c8symbol = api[7]['symbol']
    c8price = api[7]['current_price']
    c8_msupply = api[7]['max_supply']
    c8mcap = api[7]['market_cap']
    c8change1 = api[7]['price_change_percentage_24h']
    c8change2 = api[7]['price_change_24h']
    c8rank = api[7]['market_cap_rank']

    #c9
    c9name = api[8]['name']
    c9symbol = api[8]['symbol']
    c9price = api[8]['current_price']
    c9_msupply = api[8]['max_supply']
    c9mcap = api[8]['market_cap']
    c9change1 = api[8]['price_change_percentage_24h']
    c9change2 = api[8]['price_change_24h']
    c9rank = api[8]['market_cap_rank']

    #c10
    c10name = api[9]['name']
    c10symbol = api[9]['symbol']
    c10price = api[9]['current_price']
    c10_msupply = api[9]['max_supply']
    c10mcap = api[9]['market_cap']
    c10change1 = api[9]['price_change_percentage_24h']
    c10change2 = api[9]['price_change_24h']
    c10rank = api[9]['market_cap_rank']

    c11name = api[10]['name']
    c11symbol = api[10]['symbol']
    c11price = api[10]['current_price']
    c11_msupply = api[10]['max_supply']
    c11mcap = api[10]['market_cap']
    c11change1 = api[10]['price_change_percentage_24h']
    c11change2 = api[10]['price_change_24h']
    c11rank = api[10]['market_cap_rank']

    c12name = api[11]['name']
    c12symbol = api[11]['symbol']
    c12price = api[11]['current_price']
    c12_msupply = api[11]['max_supply']
    c12mcap = api[11]['market_cap']
    c12change1 = api[11]['price_change_percentage_24h']
    c12change2 = api[11]['price_change_24h']
    c12rank = api[11]['market_cap_rank']

    c13name = api[12]['name']
    c13symbol = api[12]['symbol']
    c13price = api[12]['current_price']
    c13_msupply = api[12]['max_supply']
    c13mcap = api[12]['market_cap']
    c13change1 = api[12]['price_change_percentage_24h']
    c13change2 = api[12]['price_change_24h']
    c13rank = api[12]['market_cap_rank']

    c14name = api[13]['name']
    c14symbol = api[13]['symbol']
    c14price = api[13]['current_price']
    c14_msupply = api[13]['max_supply']
    c14mcap = api[13]['market_cap']
    c14change1 = api[13]['price_change_percentage_24h']
    c14change2 = api[13]['price_change_24h']
    c14rank = api[13]['market_cap_rank']

    c15name = api[14]['name']
    c15symbol = api[14]['symbol']
    c15price = api[14]['current_price']
    c15_msupply = api[14]['max_supply']
    c15mcap = api[14]['market_cap']
    c15change1 = api[14]['price_change_percentage_24h']
    c15change2 = api[14]['price_change_24h']
    c15rank = api[14]['market_cap_rank']

    return render_template('Projects.html',btcname=btcname,btcsymbol=btcsymbol,btcprice=btcprice,btcmcap=btcmcap,btcchange1=btcchange1,btcchange2=btcchange2,btcrank=btcrank,
    ethname=ethname,ethsymbol=ethsymbol,ethprice=ethprice,ethmcap=ethmcap,ethchange1=ethchange1,ethchange2=ethchange2,ethrank=ethrank,
    bnbname=bnbname,bnbsymbol=bnbsymbol,bnbprice=bnbprice,bnbmcap=bnbmcap,bnbchange1=bnbchange1,bnbchange2=bnbchange2,bnbrank=bnbrank,
    adaname=adaname,adasymbol=adasymbol,adaprice=adaprice,adamcap=adamcap,adachange1=adachange1,adachange2=adachange2,adarank=adarank,
    c5name=c5name,c5symbol=c5symbol,c5price=c5price,c5mcap=c5mcap,c5change1=c5change1,c5change2=c5change2,c5rank=c5rank,
    c6name=c6name,c6symbol=c6symbol,c6price=c6price,c6mcap=c6mcap,c6change1=c6change1,c6change2=c6change2,c6rank=c6rank,
    c7name=c7name,c7symbol=c7symbol,c7price=c7price,c7mcap=c7mcap,c7change1=c7change1,c7change2=c7change2,c7rank=c7rank,
    c8name=c8name,c8symbol=c8symbol,c8price=c8price,c8mcap=c8mcap,c8change1=c8change1,c8change2=c8change2,c8rank=c8rank,
    c9name=c9name,c9symbol=c9symbol,c9price=c9price,c9mcap=c9mcap,c9change1=c9change1,c9change2=c9change2,c9rank=c9rank,
    c10name=c10name,c10symbol=c10symbol,c10price=c10price,c10mcap=c10mcap,c10change1=c10change1,c10change2=c10change2,c10rank=c10rank,
    c11name=c11name,c11symbol=c11symbol,c11price=c11price,c11mcap=c11mcap,c11change1=c11change1,c11change2=c11change2,c11rank=c11rank,
    c12name=c12name,c12symbol=c12symbol,c12price=c12price,c12mcap=c7mcap,c12change1=c12change1,c12change2=c12change2,c12rank=c12rank,
    c13name=c13name,c13symbol=c13symbol,c13price=c13price,c13mcap=c13mcap,c13change1=c13change1,c13change2=c13change2,c13rank=c13rank,
    c14name=c14name,c14symbol=c14symbol,c14price=c14price,c14mcap=c14mcap,c14change1=c14change1,c14change2=c14change2,c14rank=c14rank,
    c15name=c15name,c15symbol=c15symbol,c15price=c15price,c15mcap=c15mcap,c15change1=c15change1,c15change2=c15change2,c15rank=c15rank,





    )


