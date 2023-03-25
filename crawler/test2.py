import wget



for i in range(3500, 3500+51):
    url = f"https://links.sgx.com/1.0.0/derivatives-historical/{i}/TC.txt"
    wget.download(url, out="data/tradeCancel")
