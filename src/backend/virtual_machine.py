class VirtualMachine:
    """
    Represents a virtual machine (VM)
    :param name: name of the VM
    :param vmx_file_path: path to the .vmx file of this VM
    """
    def __init__(self, name, vmx_file_path):
        self.name = name
        self.vmx_file_path = vmx_file_path
    
    def get_name(self):
        return self.name

if __name__ == "__main__":
    vm = VirtualMachine("myvm", "path")
    print(vm)