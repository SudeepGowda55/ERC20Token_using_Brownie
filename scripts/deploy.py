from brownie import accounts, config, MyToken

def main():
   account=accounts.add(config["wallets"]["from_key"])
   erc20=MyToken.deploy({"from":account})
