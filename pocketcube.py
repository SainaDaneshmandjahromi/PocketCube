def myBFS(state):
    myQueue = []
    myQueue.append([state,""]) #state,harekat haii k ta hala baes shode behesh berecm ro too saf bezar
    if (isFinal(state[0])):
        return state[1]

    while(True):
        newstate = myQueue.pop(0) #oon state ro barmidare har seri va bachehasho expand mikone
                                  #bachehash mishe oon 12 harekat k bahashoon az in state mirim b state jadid

        myStat = moveOne(newstate[0])
        myQueue.append([myStat,newstate[1]+"1 "])
        if(isFinal(myStat)):
            return newstate[1] + "1 " #state dar asare oon harekat va harekat haii k ta hala baes shode be in node berecm ro mizare too saf

        myStat = moveTwo(newstate[0])
        myQueue.append([myStat,newstate[1]+"2 "])
        if(isFinal(myStat)):
            return newstate[1] + "2 "

        myStat = moveThree(newstate[0])
        myQueue.append([myStat,newstate[1]+"3 "])
        if(isFinal(myStat)):
            return newstate[1] + "3 "

        myStat = moveFour(newstate[0])
        myQueue.append([myStat,newstate[1]+"4 "])
        if(isFinal(myStat)):
            return newstate[1] + "4 "

        myStat = moveFive(newstate[0])
        myQueue.append([myStat,newstate[1]+"5 "])
        if(isFinal(myStat)):
            return newstate[1]+ "5 "

        myStat = moveSix(newstate[0])
        myQueue.append([myStat,newstate[1]+"6 "])
        if(isFinal(myStat)):
            return newstate[1]+ "6 "

        myStat = moveSeven(newstate[0])
        myQueue.append([myStat,newstate[1]+"7 "])
        if(isFinal(myStat)):
            return newstate[1]+ "7 "

        myStat = moveEight(newstate[0])
        myQueue.append([myStat,newstate[1]+"8 "])
        if(isFinal(myStat)):
            return newstate[1]+ "8 "

        myStat = moveNine(newstate[0])
        myQueue.append([myStat,newstate[1]+"9 "])
        if(isFinal(myStat)):
            return newstate[1]+ "9 "

        myStat = moveTen(newstate[0])
        myQueue.append([myStat,newstate[1]+"10 "])
        if(isFinal(myStat)):
            return newstate[1]+ "10 "

        myStat = moveEleven(newstate[0])
        myQueue.append([myStat,newstate[1]+"11 "])
        if(isFinal(myStat)):
            return newstate[1]+ "11 "

        myStat = moveTwelve(newstate[0])
        myQueue.append([myStat,newstate[1]+"12 "])
        if(isFinal(myStat)):
            return newstate[1]+ "12 "



def readInput():
    lines = []
    for i in range(6):
        newLine = input()
        lines.append(newLine[0])
        lines.append(newLine[2])
        lines.append(newLine[4])
        lines.append(newLine[6])

    return lines

def moveOne(state):
    newState = state[:]
    newState[4] = state[8] #F1-U1
    newState[6] = state[10] #F3-U3
    newState[23] = state[4] #U1-B4
    newState[21] = state[6] #U3-B2
    newState[12] = state[23] #B4-D1
    newState[14] = state[21] #B2-D3
    newState[8] = state[12] #D1-F1
    newState[10] = state[14] #D3-F3
    newState[0] = state[1] #L2-L1
    newState[1] = state[3] #L4-L2
    newState[3] = state[2] #L3-L4
    newState[2] = state[0] #L1-L3
    return newState


def moveTwo(state):
    newState = state[:] #reverse
    newState[8] = state[4] #F1-U1
    newState[10] = state[6] #F3-U3
    newState[4] = state[23] #U1-B4
    newState[6] = state[21] #U3-B2
    newState[23] = state[12] #B4-D1
    newState[21] = state[14] #B2-D3
    newState[12] = state[8] #D1-F1
    newState[14] = state[10] #D3-F3
    newState[1] = state[0] #L2-L1
    newState[3] = state[1] #L4-L2
    newState[2] = state[3] #L3-L4
    newState[0] = state[2] #L1-L3
    return newState


def moveThree(state):
    newState = state[:]
    newState[5] = state[9] #F2-U2
    newState[7] = state[11] #F4-U4
    newState[22] = state[5] #U2-B3
    newState[20] = state[7] #U4-B1
    newState[13] = state[22] #B3-D2
    newState[15] = state[20] #B1-D4
    newState[9] = state[13] #D2-F2
    newState[11] = state[15] #D4-F4
    newState[17] = state[16] #R1-R2
    newState[16] = state[18] #R3-R1
    newState[18] = state[19] #R4-R3
    newState[19] = state[17] #R2-R4
    return newState


def moveFour(state):
    newState = state[:] #reverse
    newState[9] = state[5] #F2-U2
    newState[11] = state[7] #F4-U4
    newState[5] = state[22] #U2-B3
    newState[7] = state[20] #U4-B1
    newState[22] = state[13] #B3-D2
    newState[20] = state[15] #B1-D4
    newState[13] = state[9] #D2-F2
    newState[15] = state[11] #D4-F4
    newState[16] = state[17] #R1-R2
    newState[18] = state[16] #R3-R1
    newState[19] = state[18] #R4-R3
    newState[17] = state[19] #R2-R4
    return newState


def moveFive(state):
    newState = state[:]
    newState[3] = state[6] #U3-L4
    newState[1] = state[7] #U4-L2
    newState[13] = state[3] #L4-D2
    newState[12] = state[1] #L2-D1
    newState[18] = state[12] #D1-R3
    newState[16] = state[13] #D2-R1
    newState[7] = state[18] #R3-U4
    newState[6] = state[16] #R1-U3
    newState[8] = state[9] #F2-F1
    newState[10] = state[8] #F1-F3
    newState[11] = state[10] #F3-F4
    newState[9] = state[11] #F4-F2
    return newState

def moveSix(state):
    newState = state[:] #reverse
    newState[6] = state[3] #U3-L4
    newState[7] = state[1] #U4-L2
    newState[3] = state[13] #L4-D2
    newState[1] = state[12] #L2-D1
    newState[12] = state[18] #D1-R3
    newState[13] = state[16] #D2-R1
    newState[18] = state[7] #R3-U4
    newState[16] = state[6] #R1-U3
    newState[9] = state[8] #F2-F1
    newState[8] = state[10] #F1-F3
    newState[10] = state[11] #F3-F4
    newState[11] = state[9] #F4-F2
    return newState

def moveSeven(state):
    newState = state[:]
    newState[0] = state[5] #U2-L1
    newState[2] = state[4] #U1-L3
    newState[14] = state[0] #L1-D3
    newState[15] = state[2] #L3-D4
    newState[19] = state[14] #D3-R4
    newState[17] = state[15] #D4-R2
    newState[5] = state[19] #R4-U2
    newState[4] = state[17] #R2-U1
    newState[21] = state[20] #B1-B2
    newState[23] = state[21] #B2-B4
    newState[22] = state[23] #B4-B3
    newState[20] = state[22] #B3-B1
    return newState

def moveEight(state):
    newState = state[:]    #reverse
    newState[5] = state[0] #U2-L1
    newState[4] = state[2] #U1-L3
    newState[0] = state[14] #L1-D3
    newState[2] = state[15] #L3-D4
    newState[14] = state[19] #D3-R4
    newState[15] = state[17] #D4-R2
    newState[19] = state[5] #R4-U2
    newState[17] = state[4] #R2-U1
    newState[20] = state[21] #B1-B2
    newState[21] = state[23] #B2-B4
    newState[23] = state[22] #B4-B3
    newState[22] = state[20] #B3-B1
    return newState


def moveNine(state):
    newState = state[:]
    newState[20] = state[16] #R1-B1
    newState[21] = state[17] #R2-B2
    newState[0] = state[20] #B1-L1
    newState[1] = state[21] #B2-L2
    newState[8] = state[0] #L1-F1
    newState[9] = state[1] #L2-F2
    newState[16] = state[8] #F1-R1
    newState[17] = state[9] #F2-R2
    newState[5] = state[7] #U4-U2
    newState[4] = state[5] #U2-U1
    newState[6] = state[4] #U1-U3
    newState[7] = state[6] #U3-U4
    return newState


def moveTen(state):
    newState = state[:]  #reverse
    newState[16] = state[20] #R1-B1
    newState[17] = state[21] #R2-B2
    newState[20] = state[0] #B1-L1
    newState[21] = state[1] #B2-L2
    newState[0] = state[8] #L1-F1
    newState[1] = state[9] #L2-F2
    newState[8] = state[16] #F1-R1
    newState[9] = state[17] #F2-R2
    newState[7] = state[5] #U4-U2
    newState[5] = state[4] #U2-U1
    newState[4] = state[6] #U1-U3
    newState[6] = state[7] #U3-U4
    return newState


def moveEleven(state):
    newState = state[:]
    newState[18] = state[10] #F3-R3
    newState[19] = state[11] #F4-R4
    newState[22] = state[18] #R3-B3
    newState[23] = state[19] #R4-B4
    newState[2] = state[22] #B3-L3
    newState[3] = state[23] #B4-L4
    newState[10] = state[2] #L3-F3
    newState[11] = state[3] #L4-F4
    newState[13] = state[12] #D1-D2
    newState[15] = state[13] #D2-D4
    newState[14] = state[15] #D4-D3
    newState[12] = state[14] #D3-D1
    return newState


def moveTwelve(state):
    newState = state[:]  #reverse
    newState[10] = state[18] #F3-R3
    newState[11] = state[19] #F4-R4
    newState[18] = state[22] #R3-B3
    newState[19] = state[23] #R4-B4
    newState[22] = state[2] #B3-L3
    newState[23] = state[3] #B4-L4
    newState[2] = state[10] #L3-F3
    newState[3] = state[11] #L4-F4
    newState[12] = state[13] #D1-D2
    newState[13] = state[15] #D2-D4
    newState[15] = state[14] #D4-D3
    newState[14] = state[12] #D3-D1
    return newState

def isFinal(state):
    if state == ['w', 'w', 'w', 'w', 'b', 'b', 'b', 'b', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'y', 'y', 'y', 'y', 'o', 'o', 'o', 'o']:
        return True
    return False

input = readInput()
print(myBFS(input))