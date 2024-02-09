from socket import *
import time

class Scanner:
    def __init__(self, target):
        self.target = target
        self.t_IP = gethostbyname(target)

    def scan(self):
        raise NotImplementedError("Subclasses must implement the scan method.")

class PortScanner(Scanner):
    def __init__(self, target):
        super().__init__(target)

    def scan_ports(self, start_port, end_port):
        print('Starting scan on host:', self.t_IP)
        
        for i in range(start_port, end_port + 1):
            s = socket(AF_INET, SOCK_STREAM)
            conn = s.connect_ex((self.t_IP, i))
            
            if conn == 0:
                print('Port %d: OPEN' % (i,))
                
            s.close()

if __name__ == "__main__":
    startTime = time.time()
    target_host = input('Enter host for scanning: ')
    
    scanner = Scanner(target_host)
  

    port_scanner = PortScanner(target_host)
    port_scanner.scan_ports(50, 500)
    
    print("Time taken:", time.time() - startTime)
