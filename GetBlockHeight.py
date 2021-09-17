from bitcoinrpc.authproxy import AuthServiceProxy
import json


fruits = ["143.198.12.138", "143.198.12.14", "209.97.145.51", "161.35.136.97"]
for x in fruits:
        access = AuthServiceProxy("http://demo:tester@"+x+":80")
        print(access.getblockchaininfo()["blocks"])
