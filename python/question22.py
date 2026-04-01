#Automatisation, reseau simple
import ipaddress
liste = ["192.168.10.1", "192.168.20.1", "192.168.44.0", "172.16.100.0", "10.0.8.1", "255.255.0.1"]
def ReseauSimple(liste):
    i = 4
    for address in liste:
        try:
            ip = ipaddress.ip_address(address)
            if(ip.version == 4):
                format = "IPV4"
                print(f"Address: {ip} de format IPV4 est valide")
            else:
                print(f"Address: {ip} de format IPV6 est valide")
                format = "IPV4"
            with open("logs\\addresses.txt", "a") as file:
                file.write(f"\nAdress: {ip}")
        except ValueError:
            print(f"Address: {address} est invalide")

ReseauSimple(liste)