# urls
def get_urls_folders(id):
    return [
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/WEBPXTICK_DT.zip", "data/tick"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TickData_structure.dat", f"data/tickDs/TickData_structure{id}.dat"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TC.txt", "data/tradeCancel"),
        (f"https://links.sgx.com/1.0.0/derivatives-historical/{id}/TC_structure.dat", f"data/tradeCancelDs/TC_structure{id}.dat"),
    ]

# base ID
base_id = 5379

# ID file path
ID_FILE_PATH = 'IDs_list.txt'

