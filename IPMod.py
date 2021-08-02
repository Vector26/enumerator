import nmap
import whois
class IPMod():
    ip=tuple()
    nm = nmap.PortScanner()
    Ports=dict()
    def __init__(self,tempIP):
        self.ip=self.fromString(tempIP)
    def scan(self):
        self.nm.scan(f"{self.toString()}", '22-444')
        self.displayNM()
    def enum(self):
        self.scan()
    def toString(self):
        str = '.'.join(self.ip)
        return str
    def fromString(self,IP):
        res = tuple(map(str,IP.split('.')))
        return res
    def displayNM(self):
        for i in self.nm[self.toString()]['tcp'].keys():
            self.Ports[f"{i}"]=self.nm[self.toString()]['tcp'][i]
            self.displayPORT(self.nm[self.toString()]['tcp'][i])
    def displayPORT(self,port):
        print(f"\tState:{port['state']}\tName:{port['name']}\tProduct:{port['product']} {port['version']}\tExtra:{port['extrainfo']}\tCPE:{port['cpe']}")