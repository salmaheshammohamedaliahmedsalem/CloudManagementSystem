import subprocess
import tkinter as tk
from tkinter import Label, Entry, Button, filedialog

class CloudManagementSystem:
    def create_vm(self):
        memory = input("Enter memory for VM (in MB): ")
        disk = input("Enter disk size for VM (in GB): ")

        if not self.validate_input(memory, disk):
            print("Invalid input. Please enter numeric values for memory and disk.")
            return

        p = input("Do you have an ISO file for your VM? [Y/n]: ")
        if p.lower() == "y":
            try:
                subprocess.run(["qemu-img", "create", "-f", "qcow2", f"vm_disk_{disk}GB.img", f"{disk}G"])
                print(f"Virtual disk image 'vm_disk_{disk}GB.img' created successfully!")
            except Exception as e:
                print(f"Error creating virtual disk image: {e}")

            root = tk.Tk()
            root.withdraw() 
            iso_path = filedialog.askopenfilename(
                title="Select ISO file",
                filetypes=[("ISO Files", "*.iso")]
            )

            if not iso_path:
                print("ISO file selection canceled.")
                return

            print(f"ISO file path: {iso_path}")

            try:
                subprocess.run([
                    "qemu-system-x86_64.exe",
                    "-m", "1G",
                    "-smp", "2",
                    "-boot", "order=dc",
                    "-hda", f"vm_disk_{disk}GB.img",
                    "-cdrom", iso_path
                ])
                print("Virtual machine created successfully!")
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                subprocess.run(["qemu-img", "create", "-f", "qcow2", f"vm_disk_{disk}GB.img", f"{disk}G"])
                print(f"Virtual disk image 'vm_disk_{disk}GB.img' created successfully!")
            except Exception as e:
                print(f"Error creating virtual disk image: {e}")

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
