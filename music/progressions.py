#import mingus

note_names = "C C#/Db D D#/Eb E F F#/Gb G G#/Ab A A#/Bb B".split()

chord_qualities = dict(
    major = '100010010000',
    minor = '100100010000',
    dim   = '100100100000',
    aug   = '100010001000',
)

intervals = [
    "I",
    "bII",
    "II",
    "bII",
    "III",
    "IV",
    "bV",
    "V",
    "bVI",
    "VI",
    "bVII",
    "VII",
]

intervals = "I II III IV V VI VII".split()



original = "C D# Am G"

def chord2notes(chord):
    return " ".join(
        note for active, note in zip(chord, note_names) if int(active)
    )

print(chord2notes(chord_qualities['major']))

def solveProgression(progression):
    progression = progression.split()
    for chord in progression:
        root, quality = solveChord(chord)

def solveRoot(chord):
    """
    >>> solveRoot('III'
    """
    offset = 0
    if chord[0] == 'b':
        offset = -1
    if chord[0] == '#':
        offset = +1

    if offset: chord=chord[1:]

    quality = 'minor' if chord[0].islower() else 'major'


    for root, roman in (
        # Sorting is important
        (11, 'VII'),
        (9, 'VI'),
        (7, 'V'),
        (5, 'IV'),
        (4, 'III'),
        (2, 'II'),
        (0, 'I'),
    ):
        if chord.startswith(roman):
            chord = chord[len(roman):]
            break
    else:
        raise Exception("No root found")

    root = (root + offset)%12










