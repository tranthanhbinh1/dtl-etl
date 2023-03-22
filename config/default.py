

def get_urls_folders(id):
    return [
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/WEBPXTICK_DT.zip", "data/tick"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TickData_structure.dat", "data/tickDs"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TC.txt", "data/tradeCancel"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TC_structure.dat", "data/tradeCancelDs"),
    ]