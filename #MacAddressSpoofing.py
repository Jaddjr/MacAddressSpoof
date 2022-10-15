#MacAddressSpoofing

import subprocess

def change_mac(iFace,newMac):
    print(f"[+] Changing Mac Address to {newMac}")
    subprocess.call({"sudo ifconfig{iFace} down" })
    subprocess.call({"sudo ifconfig{iFace} hw ether {newMac}"})
    subprocess.call({"sudo ifconfig{iFace} up"})

change_mac("eth0","00:00:22:33:44:55")