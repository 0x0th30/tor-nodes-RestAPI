from database_operations import returnAllIPs, returnAllBans
from get_ips import getAll


def filterIPs():

    try:
        ipList = returnAllIPs()
        banList = returnAllBans()

        for ip in ipList:

            for ban in banList:
                
                if(ip == ban):
                    index = ipList.index(ip)
                    ipList[index] = ip.replace(ip, 'xxx.xxx.xxx.xxx')
                    
        with open('./api/app/lists/ip_list.txt', 'w') as file:
            for ip in ipList:
                file.write(f'{ip}\n')

    except FileNotFoundError:
        getAll()

        ipList = returnAllIPs()
        banList = returnAllBans()

        for ip in ipList:

            for ban in banList:
                
                if(ip == ban):
                    index = ipList.index(ip)
                    ipList[index] = ip.replace(ip, 'xxx.xxx.xxx.xxx')
                    
        with open('api/app/lists/ip_list.txt', 'w') as file:
            for ip in ipList:
                file.write(f'{ip}\n')

    return ipList 

