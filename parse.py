import json

def parse(file):
    fp = open(file, "r")
    notes = {}
    
    lines = fp.readlines()
    
    # build keysignature
    unparsed = lines[0].split()
    time_sig = [int(unparsed[0][0]), int(unparsed[0][2])]
    key_sig = []
    
    for key in unparsed[1:]:
        key_sig.append(key)

    notes["key_signature"] = key_sig
    notes["time_signature"] = time_sig
    notes["notes"] = []
    
    for line in lines[1:]:
        info = line.split()
        
        if len(info) == 0:
            continue
        
        if len(info[0]) == 3:
            pitch = info[0][:2]
            octave = int(info[0][2])
        else:
            pitch = info[0][0]
            
            for key in key_sig:
                if pitch in key[0]:
                    pitch += key[1]
                    break
                    
            octave = int(info[0][1])
        
        duration = info[1]
        other = []
        
        if len(info) > 2:
            other = info[2:]

        notes["notes"].append({'pitch': pitch, 'octave': octave, 'duration': duration, 'other': json.dumps(other)})

    with open(file[:-4]+".json", "w+") as fp1:
        json.dump(notes, fp1)
