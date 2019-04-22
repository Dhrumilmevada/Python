import netifaces
def ipv4():
    """ Get all IPv4 addresses for all interfaces. """
    addresses = []
    for interface in netifaces.interfaces():
        config = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in config.keys():
            for link in config[netifaces.AF_INET]:
                #print link
                if 'addr' in link.keys() and 'peer' not in link.keys():
                    ip = link['addr']
                    print ip 
                    #addresses.append(link['addr'])
                    #addresses.append(ip) 
    #print addresses
    #return addresses
ipv4()
































#import socket
#def get_ip():
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    try:
        # doesn't even have to be reachable
#        s.connect(('10.255.255.255', 1))
#        IP = s.getsockname()[0]
#    except:
 #       IP = '127.0.0.1'
  #  finally:
 #       s.close()
 #   print IP
 #   return IP
#get_ip()


#import netifaces
#print "Hello"
#print netifaces.interfaces()
#print netifaces.ifaddresses('enp2s0')


#from netifaces import interfaces, ifaddresses, AF_INET
#for ifaceName in interfaces():
 #   addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
  #  print '%s: %s' % (ifaceName, ', '.join(addresses))


