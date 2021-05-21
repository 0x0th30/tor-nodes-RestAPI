from database_operations import returnAllIPs, returnAllBans

lista = list()

def filterIPs():
    ipList = returnAllIPs()
    banList = returnAllBans()

    try:    
        for ip in ipList:
            for ban in banList:
                if(ip == ban):
                    index = ipList.index(ip)
                    ipList[index] = ip.replace(ip, 'xxx.xxx.xxx.xxx')
                    

    except ValueError:
        pass

    return ipList


def showFilter():
    ipList = returnAllIPs()
    banList = returnAllBans()

    try:    
        for ip in ipList:
            for ban in banList:
                if(ip == ban):
                    ipList.remove(ip)
                    

    except ValueError:
        pass

    return ipList