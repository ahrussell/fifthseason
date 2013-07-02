import collections
from fractions import Fraction
import json

from constants import NOTES

class Note:
    def __init__(self, pitch, octave, duration, other = None):
        
        self.pitch = pitch
        self.octave = octave
        self.duration = Fraction(duration)
        self.abs_value = NOTES[self.pitch] + (self.octave * 12)
        
        self.other_attributes = other
    
    def __repr__(self):
        return "Note: " + self.pitch + str(self.octave)


class MusicSequence(list):
    '''
    A list of Notes with some helper functions
    '''

    def __init__(self, file):
        
        with open(file) as fp:

            piece = json.load(fp)

            for note in piece["notes"]:
                self.append(Note(note['pitch'], note['octave'], note['duration'], note['other']))
    
    def to_string(self):
        str = ""
        
        for note in self:
            str += note.pitch
        
        return str
    
    def relative(self):
            
        lst = []
        
        previous = self[0]
        lst.append(0)
        
        for note in self[1:]:
            lst.append(note.abs_value - previous.abs_value)
            
            previous = note
        
        return lst
    
    def to_relative_string(self):
        str = ""
        
        for val in self.relative():
            str += chr(val + 75) # 75, or 'K', is the 0 point
        
        return str
    
    def to_abs_value_string(self):
        string = ""
        
        for note in self:
            string += chr(note.abs_value+50)
        
        return string