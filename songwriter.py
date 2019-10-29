from instrument import instrument

def play_music(filename, octave):
    notes = []
    inst = instrument()
    
    with open(filename, "r") as f:
        for line in f:
            for char in line.strip():
                notes.append(char)
            notes.append("empty")

    find_note(notes, octave, inst)
    inst.queue_play()


def find_note(notes, octave, inst):
    multiplier = 2 ** (octave - 1)

    for i in notes:
        if i == "A":
            inst.queue_sound(55*multiplier)
        elif i == "B":
            inst.queue_sound(61*multiplier)
        elif i == "C":
            inst.queue_sound(32*multiplier)
        elif i == "D":
            inst.queue_sound(36*multiplier)
        elif i == "E":
            inst.queue_sound(41*multiplier)
        elif i == "F":
            inst.queue_sound(43*multiplier)
        elif i == "G":
            inst.queue_sound(49*multiplier)
        elif i == "empty":
            inst.queue_sound(0, 0.25)


