#required imports
import subprocess
from VM.getFromCsv import vm_spec, vm_cred
#get vm secrets
vm_creds = vm_cred
#get the vm specs
vm_specs = vm_spec
#run os commands
def run_command(command1):
    result = subprocess.run(["powershell.exe", "-Command", command1], capture_output=True, text=True)
    return result
#create vm
def createScript(fileName, content):
    script = open(fileName, "w")
    script.write(content)
    script.close()
def create_vm(vm_creds, vm_specs, iso_path):
    connectCommand = f'Connect-VIServer -Server {vm_creds["host"]} -User {vm_creds["username"]} -Password "{vm_creds["password"]}"'
    createVm = f"New-VM -Name {vm_specs['name']} -VMHost {vm_creds['host']} -Datastore datastore1 -DiskGB {vm_specs['storage']} -MemoryGB {vm_specs['ram']} -NumCpu {vm_specs['cpu']} -NetworkName 'All Vms' -CD -DiskStorageFormat Thin -Confirm:$false -ScsiController 'LSI Logic SAS'"
    addIso = f'Add-CDDrive -VM {vm_specs["name"]} -ISOPath {"iso_path"}'
    scriptName = "script.ps1"
    createScript(scriptName, connectCommand+"\n"+createVm+"\n"+addIso)
    print(run_command(f".\{scriptName}"))


create_vm(vm_creds, vm_specs, "")