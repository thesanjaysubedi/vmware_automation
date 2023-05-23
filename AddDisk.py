import subprocess
from VM.getFromCsv import get_cred
vm_creds =  get_cred()
def run_command(command1):
    result = subprocess.run(["powershell.exe", "-Command", command1], capture_output=True, text=True)
    return result
def createScript(fileName, content):
    script = open(fileName, "w")
    script.write(content)
    script.close()
def create_disk(storage_in_gb, vm_name):
    vm = f"Get-VM {vm_name}"
    connectCommand = f"Connect-VIServer -Server '{vm_creds['host']}' -User {vm_creds['username']} -Password '{vm_creds['password']}'"
    create_disk = f"{vm} | New-HardDisk -CapacityGB {storage_in_gb} -Persistence persistent"
    createScript("disk.ps1",connectCommand+"\n"+create_disk)
    print(run_command(".\disk.ps1"))

create_disk(10,"MyFirstVm")