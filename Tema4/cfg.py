import re
import sys

class CFG:
    def __init__(self):
        self.rules = {}
    
    def load(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                self._parse_rule(line)
    
    def _parse_rule(self, rule):
        pattern = re.compile(r"(\w+)\s*->\s*(.+)")
        match = pattern.match(rule)
        if not match:
            raise ValueError(f"Invalid rule: {rule}")
        
        lhs, rhs = match.groups()
        rhs_alternatives = rhs.split('|')
        rhs_alternatives = [alt.strip().split() for alt in rhs_alternatives]
        
        if lhs in self.rules:
            self.rules[lhs].extend(rhs_alternatives)
        else:
            self.rules[lhs] = rhs_alternatives
    
    def validate(self):
       
        if not self.rules:
            raise ValueError("No rules found in the CFG.")
    
        if 'S' not in self.rules:
            raise ValueError("The start symbol 'S' is not defined.")
      
        print("CFG is valid.")
    
    def __str__(self):
        result = []
        for lhs, rhs_list in self.rules.items():
            rhs = " | ".join([" ".join(rhs) for rhs in rhs_list])
            result.append(f"{lhs} -> {rhs}")
        return "\n".join(result)


cfg = CFG()
cfg.load(sys.argv[1])  
cfg.validate()

class CFGCreator:
    def __init__(self):
        self.cfg = CFG()
    
    def create_cfg(self, rules):
        for rule in rules:
            self.cfg._parse_rule(rule)
    
    def save_cfg(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self.cfg))


rules = [
    "S -> NP VP",
    "NP -> Det N",
    "VP -> V NP",
    "Det -> 'a' | 'the'",
    "N -> 'cat' | 'dog'",
    "V -> 'chased' | 'caught'"
]

cfg_creator = CFGCreator()
cfg_creator.create_cfg(rules)
cfg_creator.save_cfg('new_cfg.txt')
