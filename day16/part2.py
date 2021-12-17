f = open('./input.txt', 'r')
packet = f.readline()[:-1]
bPacket = ''.join(bin(int(c, 16))[2:].zfill(4) for c in packet)

def parseOperator(packet):
    pLength, packet = int(packet[0]), packet[1:]
    nPackets = []
    if pLength == 0:
        nBits, packet = int(packet[:15], 2), packet[15:]
        original = packet
        while len(original) - len(packet) < nBits:
            sPacket, packet = parsePacket(packet)
            nPackets.append(sPacket)
    else:
        nPacket, packet = int(packet[:11], 2), packet[11:]
        for _ in range(nPacket):
            sPacket, packet = parsePacket(packet)
            nPackets.append(sPacket)
    return [nPackets, packet]

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

def parsePacket(packet):
    pType = parseType(packet)
    rPacket = packet[6:]
    if pType == 4:
        return parseLiteral(rPacket)
    else:
        sPackets, rPacket = parseOperator(rPacket)
        if pType == 0:
            sPackets = sum(sPackets)
        elif pType == 1:
            sPackets = eval('*'.join(map(str, sPackets)))
        elif pType == 2:
            sPackets = min(sPackets)
        elif pType == 3:
            sPackets = max(sPackets)
        elif pType == 5:
            sPackets = 1 * (sPackets[0] > sPackets[1])
        elif pType == 6:
            sPackets = 1 * (sPackets[0] < sPackets[1])
        elif pType == 7:
            sPackets = 1 * (sPackets[0] == sPackets[1])
        return [sPackets, rPacket]
        
print(parsePacket(bPacket)[0])
