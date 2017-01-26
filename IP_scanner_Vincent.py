import netaddr
import os
import openpyxl

os.chdir("/Users/Vincent1/Desktop")
# print netaddr.IPAddress()
ip_list = []
ip = netaddr.IPNetwork(raw_input("Geef ip adres en subnetmask op (ip/subnet): "))

for ip in list(ip):
  ip_addr = str(ip)
  response = os.system("ping -c1 -W0.1 " + ip_addr)

  if response == 0:
    print ip_list.append(str(ip))
  else:
    pass

# Write to excel file
wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = "Active IP Adresses"
ws.append([])

for ip in ip_list:
  ws.append([ip])

wb.save(raw_input("Geef een bestandsnaam op: ")+ ".xlsx")
