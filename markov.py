import collections, random

class State(collections.defaultdict):
 
    def __init__(self, dict=None):
        collections.defaultdict.__init__(self, int)
        
        if dict != None:
            for state, weight in dict.iteritems():
                self[state] = weight
 
    def add_state(self, state):
        self[state] += 1
        
        return self
        
    def set_state(self, state, weight):
        self[state] = weight
        
        return self
 
    def total_states(self):
        return sum(self.values())
 
    def next_state(self):
        rand = random.randint(0, self.total_states())
        total_pos = 0
        for state, total in self.items():
            total_pos += total
            if rand <= total_pos:
                return state

class MarkovChain(collections.defaultdict):
    def __init__(self):
        collections.defaultdict.__init__(self, State)
        
        self.state = None
    
    def set_state(self, name, state):
        self[name] = state
    
    def set_current_state(self, name):
        self.state = name
        
        return name
    
    def next(self):
        if self.state == None:
            raise ValueError("No current state set")
        else:
            next_state = self[self.state].next_state()
            
            return next_state
        