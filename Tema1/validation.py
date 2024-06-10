def createDict(file):
    dict = {} # using a dictionary to store the input file
    state = 0 # changing from 0 or 1 depending on if we need to store elements of a section
              # 1 - need , 0 - dont 

    for line in file:

        if state == 1 and 'End' not in line:
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
    
    return dict

def validate(dict):
    # importing data from the created dict
    states = dict.get('States')
    sigma = dict.get('Sigma')
    transitions = dict.get('Transitions')

    for transition in transitions:
        transitionList = transition.split(' , ')

        # checking for every state or letter from the transition table
        # if they exist in the list of states or letters from the dictionary
        if transitionList[0] not in ' '.join(states):
            return False
        
        if transitionList[1] not in sigma:
            return False
        
        if transitionList[2] not in ' '.join(states):
            return False
        
    return True