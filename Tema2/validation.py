def createDict(file):
    dict = {} # using a dictionary to store the input file
    state = 0 # changing from 0 or 1 depending on if we need to store elements of a section
              # 1 - need , 0 - dont 

    for line in file:

        if state == 1 and 'End' not in line and line!='':
            # adding the section contents to the ditctionary 
            dict[section].append(line.replace('\n',''))
        else:
            state = 0

        if ':' in line and not line.startswith('#'):
            # making the keys in the dictionary based on the sections
            # and initializing them as a vector
            dict.setdefault(line.replace(':\n',''))
            dict[line.replace(':\n','')] = []
            section = line.replace(':\n','')

            state = 1

    if(validate(dict)):
        return dict
    else:
        print('rejected')
    
def validate(dict):
    # importing data from the created dict

    states = dict.get('States')
    sigma = dict.get('Sigma')
    transitions = dict.get('Transitions')

    for transition in transitions:
        transitionList = transition.split(', ')

        # checking for every state or letter from the transition table
        # if they exist in the list of states or letters from the dictionary
        if transitionList[0] not in ' '.join(states):
            return False
        
        if all(x not in transitionList[1] for x in sigma):
            return False
        
        if transitionList[2] not in ' '.join(states):
            return False
        
    return True

def checkString(file,str):
    # creating dict and importing data
    dict = createDict(file)

    states = dict.get('States')
    sigma = dict.get('Sigma')
    transitions = dict.get('Transitions')
    
    # setting up transition for easier comparation
    index = 0
    for transition in transitions:
        transitions[index] = transition.split(', ')
        index+=1

    # setting up states for easier comparation
    index = 0
    for state in states:
        states[index] = state.split(', ')
        index+=1

    str = list(str)

    S_State = 0
    F_State = []

    # checking which states are S and F
    for state in states:
        if 'S' in state[len(state)-1]:
            S_State = state[0]
        if 'F' in state[len(state)-1]:
            F_State.append(state[0])

    # going through the transition tree and finally checking if we end up on a F state
    for letter in str:
        for transition in transitions:
            if letter in transition[1]:         # Checking if correct letter
                if S_State == transition[0]:    # and correct state then go up tree
                    S_State = transition[2]     # and update S_State with new state
                    break

    #print(S_State)                
    #print(F_State)

    if S_State in F_State:
        print('accept')
    else:
        print('reject')


