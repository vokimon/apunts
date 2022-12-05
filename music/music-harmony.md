# Harmony: Notes, Scales and Chords 🎶

## Notes

- White keys (natural notes):
	- They are the notes forming the C Scale (Do Scale)
	- In Solfege they are named: Do, Re, Mi, Fa, Sol, La, Si
	- In Anglosaxon notation: C, D, E, F, G, A, B
- Octaves:
	- Notes repeat in successive octaves
	- The same note doubles its frequency on the next octave
	- We diferentiate notes in different scales with the number of the octave
	- A4 is the A on the 4th octave (the middle A)
	- Phisically there are infinite octaves up and down but not all of them are audible
- Black keys (altered notes):
	- Tonal distance betweens succesive white notes is not uniform
	- B-C and E-F intervals are half the interval between other succesive white keys
	- Piano black keys fill the gap between those full tones
	- Two ways of expressing them referring the neighbouring notes:
		- As sharp notes: C#, D# and F#, G#, A#. The lower note up a semitone.
		- As flat notes: Db, Eb and Gb, Ab, Bb. The higher note down a semitone.
	- The black keys starting at F#/Gb form a _Major Pentatonic Scale_
- Black and white notes build a pattern in a piano keyboard
	- `_x_x_ _x_x_x_`
	- `C D E F G A B`
	- Useful to locate the notes (start locating C)
	- Counting both, black and white notes, each octave has 12 semitones
	- Playing them all in sequence is the _Chromatic Scale_


## Tones and frequencies

https://www.youtube.com/watch?v=P7iC-fbdKmQ

- Pitch vs frequency
	- Pitch is our perception of frequency
	- Linear increments in pitch (adding a semitone) has logaritmic increase in frequency (multiply frequency by a factor)
	- _Adding_ an octave is multiplying the frequency by 2
	- _Adding_ a semitone (12th of an octave) is multiplying the frequency by 2^(1/12) ~= 1,00057779
	- A cent is the 100th part of a semitone, so one cent multipies by 2^(1/(12*100))
- When a melodic instrument plays a note it generates a main frequency, the **fundamental** one (f), and then many frequencies at integer multiples, the **harmonics** (2f, 3f, 4f...)
	- The fundamental frequency determines the perceived pitch
	- The harmonics and its relative strenghts gives the distintive timber to the instrument
	- Why those frequencies? Instrument vibration builds an [standing wave](https://en.wikipedia.org/wiki/Standing_wave). The modes of vibration correspond to the harmonics
- Disonance and consonance:
	- Two sounds sound disonant or detuned if many of their harmonics do not align
	- Frequencies for musical notes are chosen to be integer ratios among them so that many of their harmonics align.
	- Octave: ratio of 2, one of each pair of harmonics match (C3-C4)
	- Fifth: ratio of 2/3, the triple and second harmonics of both tones will match (C-G)
- Pitagorean construction: By jumping fifths (2/3 factor) and folding the octaves in a cercle
	- 5 times, builds a pentatonic scale (CAGED)
	- 7 times, builds a diatonic scale (ie, C major scale)
	- 12 times, builds a chromatic scale
- Equal temperament
	- Notes obtained like by previous ratios (Pitagorean tunning) are not evenly distributed in frequency
	- Modern standardization moves those first 12 fifths frequencies to be evenly distributed in an octave (equal temperament)
	- The shift is not perceptually noticeable
	- Enables a single tunning for any transposition
- Referece note tunning
	- Notes are defined relative to other notes frequencies
	- Tunning is setting the frequency for a reference note
	- It could be arbitrary and still it would work as long as all the instruments use the same
	- Standard tunning plays A4 as 440Hz (often refered A440). Thus, A5 at 880Hz and A3 at 220Hz
	

## Scales

### Concepts

- **Scale:** an ordered set of pitches within an octave that are used for a given musical work.
	- in CMajor: C D E F G A B [C]
- **Degree:** is the position of a note within the scale. Expresed as ordinal (3rd) or in roman numerals (III).
	- In CMajor: C is I, D is II, E is III...
	- [C] is the VIII (octave=eighth)
- **Tonic note:** is the first note of the scale
	- In CMajor: The tonic is C, the first
	- In traditional western music:
		- The tonic is the note that starts a piece and returning to it is perceived as closure or tension release
		- This comes from language intonation: Returning to the starting pitch is closure.
		- Other cultures use intonation differently.
- **Step:** Refers to the tonal distance between two consecutive notes in the scale
	- CMajor scale has Tone (T) and Semitone (S) steps.
- **Interval pattern:** Tonal distances between the succesive notes of the scale.
	- In CMajor has a _Major Diatonic_ interval pattern: T T S T T T S (T=Tone, S=Semitone)
	- Expressed in semitones would be: 2 2 1 2 2 2 1
- A tonic and an interval pattern specifies an scale:
	- CMajor scale is the _Major Diatonic_ interval pattern starting at C
- **Mode:** Interval pattern that can be constructe by rotating a different pattern
	- A rotated interval pattern can be obtained by playing the same set of notes of a given scale but starting with a different tonic
	- Same notes, different interval pattern
- **Chromatic transposition:** Applying the same interval pattern, starting at a different tonic
	- Different notes, same interval pattern
- The mode of the chosen scale affects the emotional mood of the music
- A transposition does not change the mood but it can ease the performance with a given instrument

### Diatonic scales

A diatonic scale is a scale of 7 tones (heptatonal) that has 2 semitones steps and 5 tone steps where the semitones are separated at least by two full tones

In summary: any rotation of the CMajor scale

Diatonic Modes:

	| N   | Name       | Pattern       | On C                | Natural notes | Tonic | 7th | Dom  | Dom7th | AKA
	|-----|------------|---------------|---------------------|---------------|-------|-----|------|--------|----------
	| I   | Ionian     | 2 2 1 2 2 2 1 | C D  E  F  G  A  B  | C D E F G A B | CMaj  | CM7 | GMaj | G7     | Major
	| II  | Dorian     | 2 1 2 2 2 1 2 | C D  Eb F  G  A  Bb | D E F G A B C | Dmin  | Dm7 | Amin | Am7    | 
	| III | Phrygian   | 1 2 2 2 1 2 2 | C Db Eb F  G  Ab Bb | E F G A B C D | Emin  | Em7 | Bdim | B∅7    | 
	| IV  | Lydian     | 2 2 2 1 2 2 1 | C D  E  F# G  A  B  | F G A B C D E | FMaj  | FM7 | GMaj | GM7    | 
	| V   | Mixolydian | 2 2 1 2 2 1 2 | C D  E  F  G  A  Bb | G A B C D E F | GMaj  | GM7 | Dmin | Gm7    | 
	| VI  | Aeolian    | 2 1 2 2 1 2 2 | C D  Eb F  G  Ab Bb | A B C D E F G | Amin  | Am7 | Emin | Em7    | Natural Minor
	| VII | Locrian    | 1 2 2 1 2 2 2 | C Db Eb F  Gb Ab Bb | B C D E F G A | Bdim  | B∅7 | FMaj | FM7    | 

- Modes with a major third (+4) are called major:
	- Resting chord (tonic) is Major: I
	- Happy mood
	- I Ionian:
		- Major key
		- The dominant 7th is the only dominant minor 7th
		- Contains B and F that lead to C and G
		- G7 C is a perfect closure (Chinpon)
		- Happy + Ritmic
	- IV Lydian
		- F -> F# (augmented 4th)
		- Happy + Brilliant, magic
	- V Mixolydian
		- Dominant 7th is minor with minor 7th
		- Sounds milder but also epic
		- Also epic because bVII  BbMaj
		- Happy + Epic
- Modes with a minor third (+3) are called minor:
	- Resting chord (tonic) is Minor: i
	- Sad mood
	- VI Aeolian:
		- Mood: Sad + epic
		- Dominant vii
	- II Dorian
		- In between Aeolean and Mixolyidian
		- Has the Epic chord of Mixolydian bVII BbMaj
		- IVMaj FMaj is also a happy/force contrast
	- III Phrygian
		- Domminant is a B∅7
		- Inquietante
- VII Locrian tonic chord is neither Major nor minor, it is a dim chord
	- Weird mood
	- Resting chord is a diminished 5th chord
	- The only one with the bV
 

Moods of modes: https://www.youtube.com/watch?v=8i7K9GYzbIY


### Pentatonic scale

Pentatonic scale is used by many cultures.
An octave has 5 notes a fifth away (7 semitones).

C3
-(+7)->
G3
-(+7)->
D4
-(+7)->
A4
-(+7)->
E5

Folded in a octave and sorted: C D E G A, resulting in +2 +2+ 3 +2 +3 interval pattern.

Among the 12 existing **transpositions**, some are specially useful:

The ones that fit into natural notes:

- C: C D E G A
- D: D E G A B
- F: F G A C D

And the one that uses all and only altered notes:

- F#: F# G# A# C# D#

Yep, the black piano keys conforms a pentatonic scale!
A melody that you can transpose in order to use just black keys
is using a pentatonic scale.

Songs in pentatonics

- Starway to heaven - Led Zeppelin
- Sunshine Of Your Love – Cream
- Under the bridge - Red Hot
- My Girl - The Temptations
- Wandrin' Star - Lee Marvin (Western)
- Hoochie Coochie - Muddy Waters
- Don't worry be happy - McFerri


Modes:

	| N   | Western             | Intervals | On C         | CMaj Rot  | Natural transpositions | Altered trans. |
	|-----|---------------------|-----------|--------------|-----------|------------------------|----------------|
	| I   | Major pentatonic    | 2 2 3 2 3 | C D  E G  A  | C D E G A | F G A C D - G A B D E  | Gb Ab Bb Db Eb |
	| II  | Egyptian, suspended | 2 3 2 3 2 | C D  F G  A# | D E G A C | G A C D F - A B D E G  | Ab Bb Db Eb Gb |
	| III | Blues minor         | 3 2 3 2 2 | C D# F G# A# | E G A C D | A C D F G - B D E G A  | Bb Db Eb Gb Ab |
	| IV  | Blues major         | 2 3 2 2 3 | C D  F G  A  | G A C D E | C D F G A - D E G A B  | Db Eb Gb Ab Bb |
	| V   | Minor pentatonic    | 3 2 2 3 2 | C D# F G  A# | A C D E G | D F G A C - E G A B D  | Eb Gb Ab Bb Db |


Triads in Pentatonics are limited as not all diatonic notes are available.

- I, IIsus4, IIIsus4, Vsus4, vi (expressed in diatonic intervals)
- C, Dsus4, Esus4, Gsus4, Amin (C transposition)

Because of these limitations pentatonic melodies are usually harmonized with diatonic chords.

Also, pentatonics on C can be considered by the notes shared by three Diatonic Scales on C

	| Ionian I | Lydian IV | Mixolydian V | CD_F_GA | Major Pentatonic I 
	| Ionian I | Dorian II | Mixolydian V | CD*E*G_A_ | Blues Major Pentatonic IV
	| Aeolian VI | Dorian II | Mixolydian V | C_D_EG*B* | Suspended Pentatonic II
	| Aeolian VI | Dorian II | Mixolydian V | CE*F*GA | Minor Pentatonic VI

	|-----|------------|---------------|---------------------|---------------|-------|-----|------|--------|----------
	| I   | Ionian     | 2 2 1 2 2 2 1 | C D  E  F  G  A  B  | C D E F G A B | CMaj  | CM7 | GMaj | G7     | Major
	| II  | Dorian     | 2 1 2 2 2 1 2 | C D  Eb F  G  A  Bb | D E F G A B C | Dmin  | Dm7 | Amin | Am7    | 
	| III | Phrygian   | 1 2 2 2 1 2 2 | C Db Eb F  G  Ab Bb | E F G A B C D | Emin  | Em7 | Bdim | B∅7    | 
	| IV  | Lydian     | 2 2 2 1 2 2 1 | C D  E  F# G  A  B  | F G A B C D E | FMaj  | FM7 | GMaj | GM7    | 
	| V   | Mixolydian | 2 2 1 2 2 1 2 | C D  E  F  G  A  Bb | G A B C D E F | GMaj  | GM7 | Dmin | Gm7    | 
	| VI  | Aeolian    | 2 1 2 2 1 2 2 | C D  Eb F  G  Ab Bb | A B C D E F G | Amin  | Am7 | Emin | Em7    | Natural Minor
	| VII | Locrian    | 1 2 2 1 2 2 2 | C Db Eb F  Gb Ab Bb | B C D E F G A | Bdim  | B∅7 | FMaj | FM7    | 


## Chromatic


## Whole-tone hexatonic

- Whole-tone hexatonic scale has just whole-tone intervals (6*2semitones=12)
- Because the intervals are uniform, has no sense to talk about diferent modes
- Just has two transpositions:
	- The one with the lower keys of the scale in natural keys
		- C D E F# G# A#
	- The one with the lower keys of the scale in altered keys
		- Db Eb F G A B
- Only two triads are available.
	- In C:
		- Caug (Eaug and G#aug are just inversions)
		- Daug (F#aug and A#aug are just inversions)
	- In F:
		- Faug (Aaug and Dbaug are just inversions)
		- Gaug (Baug and Ebaug are just inversions)
- Function and mood
	- Because all the intervals are the same,
	  a listener used to diatonic scale will not find the patterns and leading tones
	- So, the scale has an unsettling and weird mood
	- Also gives the sensation of being lost
	- Used in horror movies, in the dream carrillion

## Diatonic scale

- A Diatonic Scale is an scale behaving like this: Transpositions and permutations of the C scale
- Scale is
- Chromatic scale: A sequence of 12 notes evenly separated within an octave.
- Diatonic scale: A sequence of 7 notes with 5 tones intervals and 2 semitones intervals so that 
	- Any rotation or transposition of the CMaj scale.
	- Major scales:
		- Intervals in semitones: 2 2 1 2 2 2 1
		- Transpositions of CMaj scale, starting at a different note
	- Minor scales:
		- Rotations of a Major scale so that the third degree is a third minor
		


- Transposition: changing the tone a set of notes to play a fixed amount of positions up or down.
	- Chromatic transposition: by n semitones
	- Diatonic transposition: by n degrees


## Intervals

Regardless to what frequency you tune a note, or to what note you start a melody,
the important musical fact is the tonal distance between the notes.

The interval is the tonal distance between two notes.

Knowing the traditional names of the intervals is useful
to understand chords names:

|semitones | interval name |
|---:|:-----|
| 0  | unison |
| 1  | second minor |
| 2  | second major |
| 3  | third minor |
| 4  | third major |
| 5  | perfect fourth |
| 6  | augmented fourth, or diminished fifth |
| 7  | perfect fifth |
| 8  | minor sixth |
| 9  | major sixth |
| 10 | minor seventh |
| 11 | major seventh |
| 12 | octave |

Nmemotecnics for the nomenclature:

- If the first note is C, major and perfects are the white keys and the ordinal means which key: second, third...
- Minor and diminished are bemoled tones
- Augmented are sharpered notes
- Octave means eighth

## Scale degrees

A scale degree is the position of a note within a given scale.

Within a major Diatònic scale

- 1st Tonic (C Do):
	- The first note in whichever diatonic scale.
	- Key note of the scale
	- Gives name to the "tonic triad" chord, depending on the scale is major or minor.
	- Tonal center and resolution tone
- 5th Dominant (G Sol)
	- Ratio of 2/3 with the Tonic
	- Creates tension that "wants" to resolve on tonic
- 3rd Mediant (E Mi)
	- Mitad de la triada.
	- A 3rd above the tonic
- 4th Subdominant (F Fa)
	- a 5th away down the Tonic
	- Ratio of 3/2
	- Dominant and subdominant are simetrical to the Tonic, a distance of a 5th up and down each
- 6th Submediant (A La)
	- A 3rd below the tonic
- 2nd Supertonic (D Re)
	- The note above the tonic
- 7th Leading tone (major scales) (B Si)
	- Catalan/Spanish: _Sensible_
	- The note below the tonic when at a semitone below
	- Leads to the tonic
	- 7th major interval
- 7th Subtonic (in minor scales) (B Si)
	- When the scale is minor
	- 7th minor interval


Depending on the diatonic scale we are using,
the interval between two consecutive degrees
might be a tone or a semitone.




A **chord** is a combination of notes that sounds good played at once.
Chords usually sounds good because its frequencies have a multiplicative factor among them.
Say, each 4 cicles of one for 7 of the other.

Chords are named after the main note, called the **root note**,
and its **quality** which indicates the intervals from the root
of the other notes of the chord.


For instance, "C Major" means that the main note is C (Do).
The "Major" part of the means that the companion notes are:

- E (Mi), 4 semitones, a **major** third interval
- G (Sol), 7 semitones, a fifth interval

TODO: C Major marked in piano

We can construct a F (Fa) Major using the same 

Note that all three notes are white keys on the piano.
When this happens, it just means that the chord fits with the C scale.
But not all major chords fit in the C escale.

If we move the chord to the key D (Re),
the major third becomes a F# (Fa sostenido)
and the fifth A (La).
Note that in order the chord to become 

If we move the chord two semitones up

### Basic (Tertian) triads

Three note chords constructed by notes a major third (+4 semitones) or minor third (+3 semitones) apart.

- Both major and minor chords rely on the V dominant
- Major chord includes III (major 3rd)
- Minor chords contains bIII (minor 3rd)
- Major sounds happy, while minor sound sad
- Diminished is constructed by 2 minor 3rd intervals
- Augmented is constructed by 2 major 3rd intervals
- Diatonic scales have 3 major chords, 3 minor chords and 1 diminished chord.
- ie. CMajor: C d e F G a Bdim


| Structure | Name | Intervals | Jumps | Symbols
|------------|----|----|----|--|--|
| `C D EF G A B` | |  |  |  | 
| `x---x--x----` | Major | I III V | +4 +3 | C CMaj CM Cdelta
| `x--x---x----` | Minor | I bIII V | +3 +4 | c Cmin Cm C-
| `x--x--x-----` | Diminished | I bIII bV | +3 +3 | Cdim C^o 
| `x---x---x---` | Augmented | I III bVI | +4 +4 | Caug C+ 


### Suspended chords

Suspended chords are triads where the
third is moved (suspended) to the 2nd or the 4th.

| Structure | Name | Intervals | Jumps | Roles | Symbols
|------------|----|----|----|--|--|
| `C D EF G A B` | |  |  |  | 
| `x----x-x----` | Suspended 4th | I IV V | +5 +2 | | Csus4 Csus
| `x-x----x----` | Suspended 2nd | I II V | +2 +5 | | Csus2

Notice that:

- Sus2 on one note I is equivalent to Sus4 on its dominant V.
- Sus4 on one note I is equivalent to Sus2 on its subdominant IV.




### 7th chords

Add a major or minor 7th to a triad

| Structure | Name | Intervals | Jumps | Roles | Symbols
|------------|----|----|----|--|--|
| `C D EF G A B` | |  |  |  | 
| `x---x--x---x` | Major 7th | I III V VII | +4 +3 +4 | | CMaj7 CMa7 CM7 Cdelta7
| `x--x---x--x-` | Minor 7th | I bIII V bVII | +3 +4 +3 |  | Cmin7 Cm7 C-7
| `x---x--x--x-` | Dominant 7th | I III V bVII | +4 +4 +3 | | C7
| `x--x--x--x--` | Diminished 7th | I bIII bV bbVII | +3 +3 +4 |  | Co7 Cdim7 
| `x--x--x---x-` | Half Diminished  7th| I bIII bV  | +3 +3 +4 |  | C∅7 Cm7b5

No augmented 7th?


### Extended chords

Add a 9th an 11th or 13th to a 7th chord

- Major from major/ionian scale  Cmaj9 CM9
- Minor from natural minor/aeolian scale  Cmin9 Cm0
- Dominant from the mixolydian scale (Major with a flattened 7th)  C9


### Add chords


Add a 9th an 11th or 13th to a triad

| Structure | Name | Intervals | Jumps | Roles | Symbols
|------------|----|----|----|--|--|
| `C D EF G A B` | |  |  |  | 
| `x---x--x----` | Major | I III V | +4 +3 | Tonic, Major Mediant, Dominant | C CMaj CM Cdelta
| `x--x---x----` | Minor | I bIII V | +3 +4 | Tonic, Minor Mediant, Dominant | c Cmin Cm C-
| `x--x--x-----` | Diminished | I bIII bV | +3 +3 |  | Cdim C^o 
| `x---x---x---` | Augmented | I III bVI | +4 +4 |  | Caug C+ 
| `x-----------` | Half Diminished | I  |  |  | C∅






### Neapolitan chords

Outside any diatonic scale.


### Slash chords

Inversion of the chord which has the bass note different from the root.

C/G means inversion with G as the bass note.







## Inversions

Diferrent order in which we play the notes of a chord


## Common Pop chord progressions

https://www.youtube.com/watch?v=dyDFcchDl2M&list=PLlx2eo2tD6KpfGmE-MXwcIRQh21neAKsK&index=4

https://en.wikipedia.org/wiki/List_of_chord_progressions

### I V vi IV (aka Axis progression)

https://en.wikipedia.org/wiki/I%E2%80%93V%E2%80%93vi%E2%80%93IV_progression#Songs_using_the_progression

Instances:

- C - G - a - F


Examples

- For ever young - Key C
- Pachembel
- Let it be - Key C
- Take on me - Key A
- Some one like you (Adele)
- When I come arround (Green Day)
- Let it go (Frozen)
- No woman no cry (Bob Marley) Key Db
- My name is Jonas (Weezer) Key B
- When I come around (Green Day)

Cool for continuous looping along the song.
The last chord adds tensions, ask for another loop.

Rotations and examples in C Major:

- I–V–vi–IV : C–G–Am–F
- V–vi–IV–I : G–Am–F–C
- vi–IV–I–V : Am–F–C–G
- IV–I–V–vi : F–C–G–Am

### vi IV I V

Same of the axis but starting at half.

- Numb (linkin park)
- Africa (Toto) F#minor
- Grenade (Bruno Mars) 
- Sant Francisco (Scott McKenzie Hippies)
- Starting at 
- Despacito
- Zombie (Cramberries)
- Self Steem (Offspring)



Loop, pero mas dramatico, empieza en menor.

Variant in order: I V vi IV

### i - bVII - bVI - V -  Andalusian cadence

Also vi - III - II - I

Instances:

- a - G - F - E
- d - C - Bb - A

Descending sensation.
Besides flamenco, in surf music.

- Hit the road Jack (Ray Charles) La de anis del mono (no more, no more...) (se cambia a blancas)
- Good vibrations (Beach boys)
- Happy together (The Turtles)

Empiezas con una cejilla en menor, y lo bajas ya en mayor 2, 2 y 1 traste.

###  i - bVII - bVI - bVII

Has a similar estructure than the andalusian cadence
but changes the last chord repeating the second one.

Instances:

- a - G - F - G

Songs:

- Stairway to heaven (final rythmic lyrics, from 'And as the wind on down the road') 
- Barcelona m'esborrona (els pets)
- Somebody i used to know
- My heart will go on (Titanic) (Celine Dyon)
- In the air tonith (Phill Collins)


### I - vi - IV - V (doo-wop changes, 50's chord progression)

Splitting away from the tonic one note at a time,
the final chord fully disengages to require resolution on the loop.

Instances:

C - a - F - G

Songs:

- Stand by me (BB King)
- All i have to do is dream (Everly Brothers)
- I will always love you (Dolly Parton, known also by The Body Guard)
- Enola Gay - OMD
- Pretty Woman - Roy Orbison
- Every breath you take - Police
- Don't Dream its over - Crowed house
- Nothing is gonna stop us now - Starship (80's)




### I - vi - ii - V : Blue moon progression

Similar to the doo-woop but changes the third chord 

Instances:

- C - A - D - G

Songs: 

- Blue Moon - The Marcels

### I - V - IV - V  Tonic Subdominant Dominant combinations

IV goes away but does not require going back.
Being all majors sounds happy.

Several instances:

- I - V - IV - V


- C - F - G

Songs:

- Luka - Suzanne Vega
- Tangerine - Led Zeppelin


### I - bVII - IV - I : Mixolidian Bamp

Pinta una escala Mixoliana (como la escala normal pero con el Bb)

- D C G (Sweet child of mine pero el D lo hacen Cadd9)
- F Eb Bb (final de hey jude

Songs:

- Hey Jude (Outro Na na na na) - Beatles
- Sympathy for the devil - Rolling Stones
- Sweet child of mine (Intro Arpeggio) - Guns
- Freedom - George Michel
- Sweet Home Alabama

### i bIII bVII IV (Plagal Cadence)

Concrete Chords:

- f - Ab - Eb - Eb
- Em G D A7sus4 (Wonderwall)

Besides the first, the following resolve in a perfect 4th interval

Songs:

- Wonderwold (Oasis)
- Mad World (Tears for Fears) estrofa Am C Em G - verse Am D Am D..

### i bVII v bVI

- e D b C

Songs:

- Can't stop - Red Hot
- Can't hold us - Mackelmore (e a7 C B)



### Circle of fith progression

Jumps the circle of fifths in Dorian scale

- Am Dm G C F Bdim E Am

In keyboard,
for each chord, keep the first note of the triplet
and make it the last key of the next triplet.

- I will survive (Gloria Gaynor)
- Fly me to the moon (jazz standard)


In the other direction: C G d a E

- Here comes the sun - Beatles
- Hey you - Jimmy Hendrix


### I V ii IV

Similar tothe Axis but changing iv with ii.

- C G d F
- F C g Bb


Songs:

- All Start - Smash Mouth
- Just like heaven - The Cure


### IV I V vi

Tension resolution tension resolution.
Reordering of the axis

- F C G a


Songs:

- Umbrella - Rihanna
- Dragostea Din Tei - Ozone (Marica tu, marica yo)


### I IV vi V

- C F a G

Reorders the Axis cord by inverting the tension chords.
Reduces ups and downs moving the tension at the end.

Songs:

- More than a feeling - Boston
- She drives me crazy - Fine Young Cannibals


### 12 bar progression (blues

This one includes rhythm and it is 12 bars long

- I I I I
- IV IV I I
- V IV I I

The last 4 bars can be different to resolve.
Other common variations are:

- V V I I
- V V I V
- V IV I V

Songs (and endings)

- Rock arround the clock - Billy Holley V V I I
- Jonny B Good - Chuck Berry V V I I
- Cant buy me love - Beatles V IV IV I
- Got my mojo working - Muddy Waters V IV I V
- Summertime - Mungo Jerry - V IV I I
- Tutti frutti - Little Richard - V IV I I
- Black or White - M Jackson - V IV I I
- I still haven't found... - U2 - V IV I I
- I feel good - James Brown -  V IV I I
- Hound Dog - Elvis (me gusta bailar) - V IV I I


### bVI bVII i i


Climbing progression until get the 

- Ab Bb c c
- F G a a

- Equivalent to (IV V vi vi)

Songs:

- Running up that hill - Kate Bush
- Living on a player - Bon Jovi
- Bring me to life - Evanescence (just before the chorus)
- Wonderwall - Oasis (start of the last verse before the chorus)

### Descending step wise: I V vi I IV iii ii V

Going down in fifths:

- When a men loves a woman - Percy Sledge - https://www.youtube.com/watch?v=EYb84BDMbi0
	- I V/1inv vi I/2inv | IV V  I7  V 
	- C G/B    Am C/G    | F  G  C7  G 


Samples:
- I V vi I IV iii ii V
- G D/F# Em G/D C Bm Am D
- I iii/2inv vi I/2inv IV vi/2inv ii IV/2inv
- C Em/B Am C/G F Am/E Dm F/C
- A whiter shade of pale - 
- Piano Man - Billy Joal
	- I V/1 IV/1 I/2 IVM7 I/1 II7 V
	- C G/B F/A C/G FM7 C/E D7 G








