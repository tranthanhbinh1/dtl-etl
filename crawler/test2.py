import wget


url = f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/WEBPXTICK_DT.zip"

for id in range(2756, 2771):
    url1 = url.format(id)
    wget.download(url1)