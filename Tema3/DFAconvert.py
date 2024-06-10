def parse_nfa_dict(nfa_dict):
    sigma = nfa_dict['Sigma']
    states_lines = nfa_dict['States']
    transitions_lines = nfa_dict['Transitions']
    
    states = {}
    start_state = None
    final_states = set()
    
    for line in states_lines:
        parts = [part.strip() for part in line.split(',')]
        state = parts[0]
        states[state] = {'start': 'S' in parts, 'final': 'F' in parts}
        if 'S' in parts:
            start_state = state
        if 'F' in parts:
            final_states.add(state)
    
    transitions = {}
    for line in transitions_lines:
        parts = [part.strip() for part in line.split(',')]
        if len(parts) != 3:
            continue
        from_state, input_char, to_state = parts
        if (from_state, input_char) not in transitions:
            transitions[(from_state, input_char)] = set()
        transitions[(from_state, input_char)].add(to_state)
    
    return sigma, states, start_state, final_states, transitions

def nfa_to_dfa(sigma, states, start_state, final_states, transitions):
    def state_to_string(state_set):
        return ''.join(sorted(state_set))
    
    dfa_states = {}
    dfa_start_state = frozenset([start_state])
    dfa_final_states = set()
    dfa_transitions = {}
    
    unprocessed_states = [dfa_start_state]
    processed_states = set()
    
    while unprocessed_states:
        current = unprocessed_states.pop()
        if current in processed_states:
            continue
        processed_states.add(current)
        
        is_final = any(state in final_states for state in current)
        current_str = state_to_string(current)
        dfa_states[current_str] = is_final
        if is_final:
            dfa_final_states.add(current_str)
        
        for input_char in sigma:
            next_state = set()
            for state in current:
                if (state, input_char) in transitions:
                    next_state.update(transitions[(state, input_char)])
            next_state = frozenset(next_state)
            next_state_str = state_to_string(next_state)
            dfa_transitions[(current_str, input_char)] = next_state_str
            if next_state not in processed_states:
                unprocessed_states.append(next_state)
    
    return dfa_states, state_to_string(dfa_start_state), dfa_final_states, dfa_transitions

def format_dfa(sigma, dfa_states, dfa_start_state, dfa_final_states, dfa_transitions):
    result = []
    
    result.append('Sigma:')
    for char in sigma:
        result.append(char)
    result.append('End')
    
    result.append('States:')
    for state in dfa_states:
        state_str = state
        if state == dfa_start_state:
            state_str += ', S'
        if dfa_states[state]:  # Check if it's a final state
            state_str += ', F'
        result.append(state_str)
    result.append('End')
   
    result.append('Transitions:')
    for (from_state, input_char), to_state in dfa_transitions.items():
        result.append(f"{from_state}, {input_char}, {to_state}")
    result.append('End')
    
    return '\n'.join(result)

def convert_nfa_to_dfa_from_dict(nfa_dict, file):
    sigma, states, start_state, final_states, transitions = parse_nfa_dict(nfa_dict)
    dfa_states, dfa_start_state, dfa_final_states, dfa_transitions = nfa_to_dfa(sigma, states, start_state, final_states, transitions)

    f = open(file, 'w')

    f.write(format_dfa(sigma, dfa_states, dfa_start_state, dfa_final_states, dfa_transitions))

    f.close


