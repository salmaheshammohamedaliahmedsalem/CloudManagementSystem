import subprocess
import tkinter as tk
from tkinter import Label, Entry, Button
class CloudManagementSystem:
    def create_vm(self):
        memory = input("Enter memory for VM (in MB): ")
        disk = input("Enter disk size for VM (in GB): ")


        if not self.validate_input(memory, disk):
            print("Invalid input. Please enter numeric values for memory and disk.")
            return

        # Create a virtual disk image using qemu-img
        try:
            subprocess.run(["qemu-img", "create", "-f", "qcow2", f"vm_disk_{disk}GB.img", f"{disk}G"])
            print(f"Virtual disk image 'vm_disk_{disk}GB.img' created successfully!")
        except Exception as e:
            print(f"Error creating virtual disk image: {e}")

        # Call QEMU command to create a virtual machine
        try:
            subprocess.run(["qemu-system-x86_64", "-m", memory, "-hda", f"vm_disk_{disk}GB.img"])
            print("Virtual machine created successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def validate_input(self, *values):
        try:
            # Check if all values can be converted to numbers
            [float(value) for value in values]
            return True
        except ValueError:
            return False

self = CloudManagementSystem()
self.create_vm()