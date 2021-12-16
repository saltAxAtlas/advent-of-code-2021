f = open('./input.txt', 'r')
packet = f.readline()[:-1]
bPacket = ''.join(bin(int(c, 16))[2:].zfill(4) for c in packet)
sVersions = 0

def parseOperator(packet):
    packet = packet[6:]
    pLength = int(packet[6])
    newPackets = []
    if pLength == 0:
        # 15 bits, # of bits
        nBits = int(packet[7:22], 2)
        
    else:
        # 11 bits, # of packets
        nPackets = int(packet[7:18], 2)

    return

def parseLiteral(packet):
    packet = packet[6:]
    value = ''
    for x in range(0, len(packet), 5):
        value += packet[x + 1 : x + 5]
        if packet[x] == 0:
            break
    return int(value, 2)

def parseType(packet):
    return int(packet[3:6], 2)

def parseVersion(packet):
    return int(packet[:3], 2)


def parsePacket(packet):
    global sVersions 
    sVersions += parseVersion(packet)
    pType = parseType(packet)
    if pType == 4:
        parseLiteral(packet)
    else:
        parseOperator(packet)
    return

parsePacket(bPacket)

print(sVersions)
