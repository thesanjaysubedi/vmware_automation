import csv

def get_data_from_csv(file_path, row_num):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if row_num < len(rows):
            return rows[row_num]
        else:
            return None

# Example usage
data = get_data_from_csv("vmReq.csv", 1)
cred_data = get_data_from_csv("vmcreds.csv",1)

vm_spec = {
    "name": str(data[0]),
    "cpu": int(data[1]),
    "ram": int(data[2]),
    "storage": int(data[3]),
    "network": "All Vms",
}
vm_cred = {
    "host": cred_data[0],
    "username": cred_data[1],
    "password": cred_data[2]
}

def get_spec():
    return vm_spec

def get_cred():
    return vm_cred