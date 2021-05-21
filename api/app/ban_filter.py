from database_operations import returnAllIPs, returnAllBans


def filterIPs():
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