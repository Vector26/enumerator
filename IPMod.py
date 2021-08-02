import nmap
class IPMod():
    ip=tuple()
    scanResults=dict()
    def __init__(self,tempIP):
        self.ip=self.fromString(tempIP)
        print(self.ip)
    def scan(self):
        nm = nmap.PortScanner()
        self.scanResults=nm.scan(f"{self.toString()}", '22-10000')
        print(self.scanResults)
    def toString(self):
        print(self.ip)
        str = '.'.join(self.ip)
        return str
    def fromString(self,IP):
        res = tuple(map(str,IP.split('.')))
        return res
