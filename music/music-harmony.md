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
	- Phisically there are infinite octaves up and down since you can divide or multiply infinitely
	- But not all of them are audible
		- Average human audible range is 31Hz - 19KHz (aprox C0 - C10)
		- Digital recording range is 20Hz - 22KHz (C-1 - C11
		- Higher octaves have few musical interest because the harmonics of the notes are lost
		- Standard piano is A0-C8
- Black keys (altered notes):
	- Tonal distance betweens succesive white notes is not uniform
	- B-C and E-F intervals are half the interval between other succesive white keys
	- Piano black keys fill the gap between those full tones
	- Two ways of expressing them referring the neighbouring notes:
		- As sharp notes: C#, D# and F#, G#, A#. The lower note up a semitone. (sostenido/sustingut)
		- As flat notes: Db, Eb and Gb, Ab, Bb. The higher note down a semitone. (bemol)
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
- Audible range
	- You can divide a frequency by 2 never reaching 0, and of course, you can always multiply by 2
	- But at some point we fall outside the human audible range (20Hz - 22000Hz)
	- So, if we tune A4 to 440Hz (which is the standard) octaves 0 to 9 are the audible ones.
	- Reference frequency is 440Hz for A4
	- You can always divide by 2 never reaching 0: A3=220Hz, A2=110Hz, A1=55Hz, A0=27.5Hz, A-1=13.75Hz...
	- You can always multiply by 2: A5=880Hz, A6=1760Hz, A7=3520Hz, A8=7040Hz, A9=14080Hz, A10=28160Hz
- When a melodic instrument plays a note, it generates a main frequency, the **fundamental** one (f), and then many frequencies at integer multiples, the **harmonics** (2f, 3f, 4f...)
	- The fundamental frequency determines the perceived pitch
	- The harmonics, by means of its relative strenghts, gives the distintive timber to the instrument
	- Why those frequencies? Instrument vibration builds an [standing wave](https://en.wikipedia.org/wiki/Standing_wave).
		- The modes of vibration of the standing wave correspond to the harmonics
	- High pitches of an instrument lose the timber because harmonics move outside the audible range
- Disonance and consonance:
	- Two sounds sound disonant or detuned if many of their harmonics do not align
	- Frequencies for musical notes are chosen to be integer ratios among them so that many of their harmonics align.
	- Octave: ratio of 2, one of each pair of harmonics match (C3-C4)
	- Fifth: ratio of 3/2, the triple and second harmonics of both tones will match (C-G)
	- Augmented Fourth: More complex ratio of 64/729 (6 fiths jumps, thus (2/3)^6) generates disonance (C-F#/Gb)
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
- A scale is fully specified by a tonic plus an interval pattern:
	- CMajor scale is the _Major Diatonic_ interval pattern starting at C

Derived scales: different scales can be obtained from a reference one, by rotation and transposition:

- **Degree rotation:** Playing the same set of notes but starting with a different note as tonic
	- The result is a different interval pattern obtained by rotation
		- 2 2 1 2 2 2 1 -> 2 degree rotation -> 1 2 2 2 1 2 2
	- **Mode:** Each one of those different interval patterns
	- Same set of notes, different interval pattern
	- As many modes as degrees has the scale (7 in C Major)
	- Modes named after the degree of the tonic in the reference scale
	- The mode of the chosen scale affects the emotional mood of the music
- **Chromatic transposition:** Applying the same interval pattern, starting at a different tonic
	- Generates a diferent set of notes
	- The interval pattern is kept
	- Transposition unit: semitones
	- A transposition does not change the mood but it can ease the performance with a given instrument

Scale families: each is a circular sequence of intervals, you can transpose and rotate.

- Pentatonic: 5 notes
	- 2 2 3 2 3: **Pentatonic** (5 Modes)
- Hexatonic: 6 notes
	- 2 2 2 2 2 2: **Whole tone** (1 Mode)
	- 3 2 1 1 3 2: **Blues:** (6 Modes)
- Heptatonic: 7 notes
	- 2 2 1 2 2 2 1: **Diatonic:** Dos semitonos separados por 2 y 3 tonos en cada lado (7 Modes)
	- 2 1 2 2 2 2 1: **Melodic Minor:** Dos semitonos separados 1 y 4 tonos en cada lado (7 Modes)
	- 2 2 1 2 1 3 1: **Harmonic Major:**  (7 Modes)
	- 2 1 2 2 1 3 1: **Harmonic Minor:** (7 Modes)
- Octatonic: 8 notes
	- 2 1 2 1 2 1 2 1: **Diminished** (2 Modes)
- Dodecatonic: 12 notes
	- 1 1 1 1 1 1 1 1 1 1 1 1: **Chromatic scale** (1 Mode)

[Scale list](music-harmony-scales.md)


## Intervals

Regardless to what frequency you tune a note, or to what note you start a melody,
the important musical fact is the tonal distance between the notes.

The interval is the tonal distance between two notes.

Knowing the traditional names of the intervals is useful
to understand chords names:

|semitones | tradit. not. | interval name |
|---:|- ---:|:--------|
| 0  |   I | unison |
| 1  |  ii | second minor |
| 2  |  II | second major |
| 3  | iii | third minor |
| 4  | III | third major |
| 5  |  IV | perfect fourth |
| 6  | IV+ v | augmented fourth, or diminished fifth or tritone |
| 7  |   V | perfect fifth |
| 8  |  vi | minor sixth |
| 9  |  VI | major sixth |
| 10 | vii | minor seventh |
| 11 | VII | major seventh |
| 12 | VIII | octave |
| 13 |  ix | minor nineth |

Nmemotecnics for the nomenclature:

- If the first note is C, major and perfects are the white keys and the ordinal means which white key: second, third...
- Minor and diminished are bemoled tones
- Augmented are sharpened notes
- Octave means eighth, literally

### Song examples

- 1 - ii: (Minor 2nd)
	- Jaws (tiburon) [010101...] 
	- All my loving - Beatles [10 "All my"]
	- Fur Elise - Bethoven [10101]
- 2 - II: (Major 2nd)
	- Frere Jacques [02 "Fre-re"]
	- Happy birthday [0020 "Ha-ppy birth-day"]
	- Yesterday - Beatles [200 "Yes-ter-day"]
	- Noche de paz [020 "No-che-de"]
	- Enter Sandman [202 "En-ter-Light"]
- 3 - iii: (Minor 3rd)
	- Mad World - Tears for Fears [003300 "All-a-round-me-are-fa-..miliar faces"]
	- Greensleeves [03] 
	- Smoke in the water - Deep Purple [035 Riff]
	- Hey Jude - Beatles [3003 "Hey-Jude  don't-make.."]
	- Superdetective en Hollywood [03005..]
- 4 - III (Major 3rd)
	- When the saints go marching in [0457]
	- Obladi, oblada - Beatles [047047047 "O-bla-di O-bla-da..."]
	- Campanadas cuartos [40 ding dong]
	- Summertime - George Gershwin [404 "sum-mer-time"]
	- Doce cascabeles - [**04040404**] "**do-ce-cas-ca-be-les-tie-ne** ... mi caballo..."]
- 5 - IV (Perfect 4th)
	- Here comes the bride - Wagner [0555 "here-comes-the-bride"]
	- We wish you a Merry Christmas [055 "we-wish-you..."
	- Summer nights - Grease [0.05.57.75750 bass]
	- El patio de mi casa [**05**55 "**el-pa**-tio-de"]
	- Under pressure - Queen (ice-ice-baby) [5555550 bass]
	- Cannon de Pachenbel [50 - primeras dos notas blancas]
	- Pinocho fue a pescar [050505 "pi-no-cho-fuea-pes-car..."]
	- El intervalo entre las cuerdas de la guitarra menos entre la 2a y 3a
- 6 - IV+ (Augmented 4th)
	- The Simpsons Theme [06 "The-Simp..."]
	- Mariano el primo se llama mariano [067 "Ma-ria-no"] (Maria de west side story)
	- Evenflow - Pearl Jam [60 "E-ven"]
- 7 - V (Perfect 5th)
	- Starwars - John Williams [0000.7]
	- Superman - John Williams [0007.7]
	- ET - John Williams [07..]
	- Twinkle Twinkle litle star [0055 "twin-kle twin-kle" "ca-da-di-a"] (canta el gall quiquiriqui)
	- Flinkstones (picapiedra) [70 "Pe-dro" "Flinks-tones"]
	- Game of thrones [70 main melody]
	- Bad Romance - Lady Gaga [007787 "rah-rah-a-ah-ah-ha"]
- 8 - vi (Minor 6th)
	- The entertainer - Scott Joplin (Willians add) [080808 tres en leif motive]
	- Orfeo Negro (Manhã De Carnaval) [08.. "ma-nhã...-tão bonita manhã"]
	- Love Story [80088 tiiruriruriiii] 
- 9 - VI (Major 6th)
	- Jingle bells (verse) [09 "Da-shing... thru the snow" "per-da ...munt la neu" ]
	- My Way - Sinatra [09 "And-now... the end is near"]
	- No surprises - Radiohead (piano inicial) [905090509050...]
- 10 - vii (Minor 7th) (A in sequences)
	- The winner takes it all - Abba [0**0A**%  "the-**win-ner**-ta-"]
	- Can't stop - Red Hot - bass - [00AC0000AC]  (son tres notas resuelve a octava)
- 11 - VII (Major 7th) (B in sequences)
	- Take on Me - Aha - [0BC "Take-on-me"]
	- I love you - Cole Porter [BB0 "I-love-you ...hums the april breeze]
- 12 - VII (Octave) (C in sequence)
	- Somewhere over the rainbow [0C "some-where..."]
	- Bulls on the parade - Rage aganist the machine [C0.CC0.CC0 chorus/intro bass]
	- The forest - The Cure [0C.0A0708]
- 13 - IX (Minor 9th)
	- Killing in the name of - Rage aganist the machine [000DDD000DDD000DDD000DDD intro bass]

More in:

- https://www.earmaster.com/products/free-tools/interval-song-chart-generator.html
- https://www.musicca.com/interval-song-chart

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



## Chords

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
| `x---x--x---x` | Major 7th | I III V VII | +4 +3 +4 | | CMaj7 CMa7 CM7 CΔ7 CΔ
| `x--x---x--x-` | Minor 7th | I bIII V bVII | +3 +4 +3 |  | Cmin7 Cm7 C-7
| `x---x--x--x-` | Dominant 7th | I III V bVII | +4 +3 +3 | | C7
| `x--x---x---x` | MinorMajor 7th | I bIII V VII | +3 +4 +4 | | CmM7
| `x--x--x--x--` | Diminished 7th | I bIII bV bbVII | +3 +3 +3 |  | Co7 Cdim7 
| `x--x--x---x-` | Half Diminished  7th| I bIII bV  | +3 +3 +4 |  | C∅7 Cm7b5

No augmented 7th?

### upper chord extensions

	x-x-x--x--x- C9 (c7add9) 
	x-x-x--x---- Cadd9 (c + 9th)
	x-x--x-x--x- C11 (C9add11)


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


### Inversion / Slash chords

**Inversion:** a different order in which play the notes of a chord
The standard inversion is the one with the bass note being the root.

**Slash chords:** Inversion of the chord which has the bass note different from the root.
Named because the notation: C/G means inversion with G as the bass note.

## Modulation

Changing the key/scale in the middle of the song

- Intensify the energy level (subidon-subidon)
- In duets, adapting to the singer key
- Create interest in a monotonous song (subidon-subidon, too)
- Could lead to akward sensation

Tactics:

- Dominant bridge up (energy push): For semitone up, use the dominant chord of the target key.
	- Examples: C  F  G  C  **Ab**  Db  Gb  Ab  Db
- Pivot chords: For wider jumps, usually use in duets. Use chords that are shared by both keys. Can be combined with target dominant.
	- Example: C  Dm  G  Am  Dm  Gm7  C11  F

Considerations:

- Upwards is easier than downwards since downwards sap energy from the song
	- Changing down 4th can be see as changing up a 5th, so ok
	- But changing down semitone or tone is trick
- Harder to modulate to different signatures (either sharps or flats)
- Better to use upward modulation along intensifications on the lyrics, the singing style or volume
- Early modulation could sound abrupt, better later in the song, when the harmony has been introduced


## Chord progression

**Chord progression:** A sequence of chords.

- Different chord progressions provides different feelings to the piece
- Two transposed chord progressions provide a similar feeling
- Because of that we characterize chords in a chord progression with the intervals to their roots from the key/scale root.
- We represent the chords with roman numerals, upper case if Major, lower case if minor
	- In C Major scale: D is _II_ and Am is _vi_
	- In A minor scale: D is _VI_ and Am is _i_

- In a Major Scale
    - I (C) completion/resolution
    - V (G) ask for fast resolution to I (twist and shout beatles, cuando añaden voces de V para resolver en I)
    - IV (F) ask for eventual resolution, but also release (Walk of the wild side, I-V loop)
    - vi (Am) resolves but in a darker place (Stand by me I - iv - ...)
    - ii (Dm) minor version of the IV (estrofa time after time: loop I - ii)
    - iii (Em) mix of tension and resolution (estrofa de Space Oddity loop I - iii)
- Out of the key root
    - bVII (Bb - D F) epic open sound (intro Dont you forget about me, simple minds D-E )
    - bIII (Eb - G Bb) Puente entre escalas menor y mayor tiene la tercera menor de la dominante (Love Shack B52)
    - bVI (Ab - C Eb)  (Poison Alice Cooper en el opening)
    - bII (Db F Ab) exotic arabesque
    - bV (Gb Bb Db) 
- Non diatonic versions (major scale chords but changing major <-> minor)
    - i (Cm)
    - III (E)
    - II (D)
    - VI (A) tendency to resolve to ii (i get around - beach boys
    - VII (B) not common (Radio Head KArma police (C-D-G-F# IV-V-I-VII)
    - v (g) reflective, nostalgic (ColdPlay Clocks)


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

Rotations and examples transposed in C Major and G major

- I–V–vi–IV : C–G–Am–F  G-D-Em-C
- V–vi–IV–I : G–Am–F–C  D-Em-C-G
- vi–IV–I–V : Am–F–C–G  Em-C-G-D
- IV–I–V–vi : F–C–G–Am  C-G-D-Em


### vi IV I V

Same of the axis but starting at half.

- Numb (linkin park) d..ud.u...u.d.u.
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


### I III IV iv  (Creep progression)

- Creep - Radio Head (G B C Cm)
- Space Oddity - Bowie - I III IV iv I (iv is shorter)
- Underweard - Pulp
- Magic City - Gorillaz
- Where is my mind - Pixies (Break before chorus)
- The air I breath - The hollies

- I Establishes tonality
- III chormatic mediant  chord not belonging to the scale
- IV 
- iv minor plagal cadence

	_x_x__x_x_x_
	  x    x   x  G
	   x  x    x  B
	x   x  x      C
	x  x   x      Cm


### ii V I



- Dm G C (CMajor)
- Gm A D (FMajor)


Function:

- Good for changing key (modulating)
- It's done by playing it first on the origin key and then in the destination key
- Chords have role in both keys

- Variaciones con la misma funcionalidad:
	- ii puede ser: II, ii7, iidim
	- I could be: I or i
	- V could be V7, but is the leading tone to the new key
		
C
Eb
F
Db
E
D
G
A
Ab
B
Gb
C


### iv (VI) V I

https://www.facebook.com/reel/2683564461820767


- September - Earth wind & fire
- Dragula - Rob Zombie (taking over)
- Party night anathem - 
- Call me maybe - Carly Rae Jepsen
- Gimme A man after midnight - ABBA
- Ain't No Mountain High Enough - Marvin Gaye (verse)
- Lovefool- Cardigans (love me, love me, say that you love me)
- Anti-hero - Taylor Swift
- We found love - Rianna
- i can't feel my face - the weekend
- I wanna dance with 


