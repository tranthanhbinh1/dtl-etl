import os


#get path
current_path = os.getcwd()

# Create folders
def create_folder():
    list = ['tick', "tickDs", "tradeCancel", "tradeCancelDs"]
    for items in list:
        try:
            path = os.path.join(current_path, "data", items)
            os.makedirs(path)
        except FileExistsError:
            break


