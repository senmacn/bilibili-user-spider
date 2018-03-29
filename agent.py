import random
def LoadUserAgents():
    uas = []
    with open('D:\\myPython\\project\\user_agents.txt','r') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip('\n').strip('"'))
    return uas