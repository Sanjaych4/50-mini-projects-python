# Day 25: Website blocker

import time
import ctypes

# Define the path to the hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Define the IP address to redirect to
redirect_ip = "127.0.0.1"

# Take the list of websites to block as input
website_list = input("Enter the websites to block (separated by space): ").split()

# Block the websites by adding their IP and address to the hosts file
with open(hosts_path, 'r+') as file:
    content = file.read()
    for website in website_list:
        if website in content:
            pass
        else:
            # Write the website IP and address to the hosts file
            file.write(redirect_ip + " " + website + "\n")

# Reload the DNS cache to apply the changes
ctypes.windll.kernel32.SetDllDirectoryW(None)
ctypes.windll.dnsapi.DnsFlushResolverCache()

# Keep the program running until the user stops it
while True:
    time.sleep(1) # repeat the loop every 1 second
