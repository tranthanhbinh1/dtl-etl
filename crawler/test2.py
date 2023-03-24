import wget



for i in range(3700, 3751):
    url = f"https://links.sgx.com/1.0.0/derivatives-historical/{i}/TC.txt"
    wget.download(url, out="data/tradeCancel")
