f = open('./input.txt', 'r')
packet = f.readline()[:-1]
bPacket = ''.join(bin(int(c, 16))[2:].zfill(4) for c in packet)
sVersions = 0  

def parseOperator(packet):
    pLength, packet = int(packet[0]), packet[1:]
    if pLength == 0:
        nBits, packet = int(packet[:15], 2), packet[15:]
        oPacket = packet
        while len(oPacket) - len(packet) < nBits:
            x, packet = parsePacket(packet)
    else:
        nPacket, packet = int(packet[:11], 2), packet[11:]
        for _ in range(nPacket):
            x, packet = parsePacket(packet)
    return [0, packet]

def parseLiteral(packet):
    value = ''
    for x in range(0, len(packet), 5):
        value += packet[x + 1 : x + 5]
        if packet[x] == '0':
            packet = packet[x + 5:]
            break
    return [int(value, 2), packet]
    
def parseType(packet):
    return int(packet[3:6], 2)

def parseVersion(packet):
    return int(packet[:3], 2)

def parsePacket(packet):
    global sVersions 
    sVersions += parseVersion(packet)
    pType = parseType(packet)
    rPacket = packet[6:]
    if pType == 4:
        return parseLiteral(rPacket)
    else:
        return parseOperator(rPacket)

parsePacket(bPacket)

print(sVersions)
