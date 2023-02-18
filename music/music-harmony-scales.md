# Harmony: Scales 🎶

## Diatonic scales

A diatonic scale is a scale of 7 tones (heptatonal)
that has 2 semitones steps and 5 tone steps
where the semitones are separated at least by two full tones

In summary: any rotation or transposition of the CMajor scale

Diatonic Modes:

	| N   | Name       | Pattern       | On C                | Natural notes | AKA
	|-----|------------|---------------|---------------------|---------------|----------
	| I   | Ionian     | 2 2 1 2 2 2 1 | C D  E  F  G  A  B  | C D E F G A B | Major
	| II  | Dorian     | 2 1 2 2 2 1 2 | C D  Eb F  G  A  Bb | D E F G A B C | 
	| III | Phrygian   | 1 2 2 2 1 2 2 | C Db Eb F  G  Ab Bb | E F G A B C D | 
	| IV  | Lydian     | 2 2 2 1 2 2 1 | C D  E  F# G  A  B  | F G A B C D E | 
	| V   | Mixolydian | 2 2 1 2 2 1 2 | C D  E  F  G  A  Bb | G A B C D E F | 
	| VI  | Aeolian    | 2 1 2 2 1 2 2 | C D  Eb F  G  Ab Bb | A B C D E F G | Natural Minor
	| VII | Locrian    | 1 2 2 1 2 2 2 | C Db Eb F  Gb Ab Bb | B C D E F G A | 

Insights:

- We can get any mode with white keys just by stressing the proper root.
- Keeping the root in C, we can obtain all the modes by adding progresivelly flats (or sharps)

A mechanical way of learning modes on C,

- as we jump to the next 5th mode, we just add a flat.
- flats are chosen interleaving one from the 3 blacks and next from 2 blacks group
- pick the flat on the right
- to obtain IV we sharp instead flat and pick from left

In action:

	_x_x__x_x_x_
	o o o Xo o o IV  #4 Lydian (Exception from major sharps F)
	o o oo o o o I      Ionian (Major, the reference, all whites)
	o o oo o oX  V   b7 Mixolydian (flats B)
	o oX o o ox  II  b3 Dorian (flats E)
	o ox o oX x  VI  b6 Aeolian (flats A)
	oX x o ox x  III b2 Phrygian (flats D)
	ox x oX x x  VII b5 Locrian (flats G)
	_x_x__x_x_x_
	 4 2  5 3 1  (Order to add flats)

::: note
	If we extend the method we will get the other 5 tonalities,
	but they do not include the root (C) so they are not modes of the scale.

Each mode has their chords:

	| N   | Name       | Natural notes | Tonic | 7th | Dom  | Dom7th |
	|-----|------------|---------------|-------|-----|------|--------|
	| I   | Ionian     | C D E F G A B | CMaj  | CM7 | GMaj | G7     |
	| II  | Dorian     | D E F G A B C | Dmin  | Dm7 | Amin | Am7    |
	| III | Phrygian   | E F G A B C D | Emin  | Em7 | Bdim | B∅7    |
	| IV  | Lydian     | F G A B C D E | FMaj  | FM7 | GMaj | GM7    |
	| V   | Mixolydian | G A B C D E F | GMaj  | GM7 | Dmin | Gm7    |
	| VI  | Aeolian    | A B C D E F G | Amin  | Am7 | Emin | Em7    |
	| VII | Locrian    | B C D E F G A | Bdim  | B∅7 | FMaj | FM7    |

- The tonic (rest) chord: I III V
- The dominant (tension) chord: V VII II
- The 7th: I III V VII
- The dominant 7th: V VII II IV

The tonic chord provides the majority or minority or neither (locrian) character of the mode.

Moods of modes: https://www.youtube.com/watch?v=8i7K9GYzbIY

### Major modes (Ionian, Lydian, Mixolydian)

- Modes with a major third (+4) are called major.
- Resting chord (tonic) is Major: I
- They bring a happy mood

Which are

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

### Minor modes (Aeolian, Dorian, Phrygian)

- Modes with a minor third (+3) are called major.
- Resting chord (tonic) is a minor triad: ia
- They bring a sad mood

Which are

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

### Neither major neither minor

VII Locrian mode is quite special as the resting triad is a dim chord, neither major nor minor.

- VII Locrian tonic chord is neither Major nor minor, it is a dim chord
	- Weird mood
	- Resting chord is a diminished 5th chord
	- The only one with the bV

## Pentatonic scale

Pentatonic scale is used by many cultures.
An octave has 5 notes a fifth away (7 semitones).

C3 -(+7)-> G3 -(+7)-> D4 -(+7)-> A4 -(+7)-> E5

Folded in a octave and sorted: C D E G A, resulting in +2 +2+ 3 +2 +3 interval pattern.

Among the 12 existing **transpositions**, 4 are specially useful:

The ones that fit into natural notes:

- C: C D E G A
- G: G A B D E
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

	| N   | Western             | Intervals | On C         | CMaj Rot  |
	|-----|---------------------|-----------|--------------|-----------|
	| I   | Major pentatonic    | 2 2 3 2 3 | C D  E G  A  | C D E G A |
	| II  | Egyptian, suspended | 2 3 2 3 2 | C D  F G  A# | D E G A C |
	| III | Blues minor         | 3 2 3 2 2 | C D# F G# A# | E G A C D |
	| IV  | Blues major         | 2 3 2 2 3 | C D  F G  A  | G A C D E |
	| V   | Minor pentatonic    | 3 2 2 3 2 | C D# F G  A# | A C D E G |

	| N   | Western             | CMaj Rot  | Natural transpositions | Altered trans. |
	|-----|---------------------|-----------|------------------------|----------------|
	| I   | Major pentatonic    | C D E G A | F G A C D - G A B D E  | Gb Ab Bb Db Eb |
	| II  | Egyptian, suspended | D E G A C | G A C D F - A B D E G  | Ab Bb Db Eb Gb |
	| III | Blues minor         | E G A C D | A C D F G - B D E G A  | Bb Db Eb Gb Ab |
	| IV  | Blues major         | G A C D E | C D F G A - D E G A B  | Db Eb Gb Ab Bb |
	| V   | Minor pentatonic    | A C D E G | D F G A C - E G A B D  | Eb Gb Ab Bb Db |

- Major: es la unica que puede construir un acorde mayor en C (C E G), es la unica que tiene E, construida con dos segundas
- Menor: es la única que puede construir un acorde menor en C (C D# G)
- Minor blues: Incluye la 3a menor pero no la 5a???
- Major blues: ???


Triads in Pentatonics are limited as not all diatonic notes are available.

- I, IIsus4, IIIsus4, Vsus4, vi (expressed in diatonic intervals)
- C, Dsus4, Esus4, Gsus4, Amin (C transposition)

Because of these limitations pentatonic melodies are usually harmonized with diatonic chords.

Also, pentatonics on C can be considered by the notes shared by three Diatonic Scales on C

	I IV V -> Major
	I II V -> Blues Major
	II V VI -> Suspended
	II III VI -> Minor
	III VI VII - Blues Minor


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


## Chromatic scale

Dodecatonic. Uses all piano keys, so 12 semitone intervals.
No modes available.

## Whole-tone hexatonic

- Whole-tone hexatonic scale has just whole-tone intervals (6*2semitones=12)
- Because the intervals are uniform, has no sense to talk about diferent modes
- Just has two transpositions:
	- The one with the lower keys of the scale in natural keys
		- C D E F# G# A#
	- The one with the lower keys of the scale in altered keys
		- Db Eb F G A B
	- On the semitone of the major scale switches from black to white keys and viceversa
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
	- A root can be built upon repetition or stress

## Melodic Minor scales

[Jazz scales: Melodic, Harmonic, Augmented, Diminished...](https://www.youtube.com/watch?v=Vq2xt2D3e3E)

Heptatonic scales which are chromatic transpositions or rotations of the C Melodic minor scale
Like diatonic scales, also has 2 halftones and 5 fulltones, but now the two halftones are separated one fulltone.

	| N   | Name        | Pattern       | Transposed on C      | Rotations            |
	|-----|-------------|---------------|----------------------|----------------------|
	| I   | Melodic Min | 2 1 2 2 2 2 1 | C  D  Eb F  G  A  B  | C  D  Eb F  G  A  B  |
	| II  | Dorian b2   | 1 2 2 2 2 1 2 | C  Db Eb F  G  A  Bb | D  Eb F  G  A  B  C  |
	| III | Lydian Aug  | 2 2 2 2 1 2 1 | C  D  E  F# G# A  B  | Eb F  G  A  B  C  D  |
	| IV  | Lydian Dom  | 2 2 2 1 2 1 2 | C  D  E  F# G  A  Bb | F  G  A  B  C  D  E  |
	| V   | Aeolian Dom | 2 2 1 2 1 2 2 | C  D  E  F  G  Ab Bb | G  A  B  C  D  Eb F  |
	| VI  | Half Dimin. | 2 1 2 1 2 2 2 | C  D  Eb F  Gb Ab Bb | A  B  C  D  Eb F  G  |
	| VII | Altered     | 1 2 1 2 2 2 2 | C  Db Eb E  Gb Ab Bb | B  C  D  Eb F  G  A  |

## Harmonic Minor scales

Heptatonic scale an harmonic sequence 1 3 1 and a minor sequence 2 1 2 2

	| N   | Name         | Pattern       | Transposed on C      | Rotations            |
	|-----|--------------|---------------|----------------------|----------------------|
	| I   | Harmonic Min | 2 1 2 2 1 3 1 | C  D  Eb F  G  Ab B  | C  D  Eb F  G  Ab B  |
	| II  | Locrian 6    | 1 2 2 1 3 1 2 | C  Db Eb F  Gb A  Bb | D  Eb F  G  Ab B  C  |
	| III | Major #5     | 2 2 1 3 1 2 1 | C  D  E  F  G# A  B  | Eb F  G  Ab B  C  D  | 
	| IV  | Dorian #4    | 2 1 3 1 2 1 2 | C  D  Eb F# G  A  Bb | F  G  Ab B  C  D  Eb | 
	| V   | Phrygian Dom | 1 3 1 2 1 2 2 | C  Db E  F  G  Ab Bb | G  Ab B  C  D  Eb F  | 
	| VI  | Lydian #2    | 3 1 2 1 2 2 1 | C  D# E  F# G  A  B  | Ab B  C  D  Eb F  G  |
	| VII | Altered bb7  | 1 2 1 2 2 1 3 | C  Db Eb Fb Gb Ab A  | B  C  D  Eb F  G  Ab | 

## Harmonic Major scales

Heptatonic scale an harmonic sequence 1 3 1 and a major sequence 2 2 1 2


	| N   | Name        | Pattern       | Transposed on C      | Rotations            |
	|-----|-------------|---------------|----------------------|----------------------|
	| I   | Melodic Maj | 2 2 1 2 1 3 1 | C  D  E  F  G  Ab B  | C  D  E  F  G  Ab B  |
	| II  | Dorian b5   | 2 1 2 1 3 1 2 | C  D  Eb F  Gb A  Bb | D  E  F  G  Ab B  C  |
	| III | Phrygian b4 | 1 2 1 3 1 2 2 | C  Db Eb E  G  Ab Bb | E  F  G  Ab B  C  D  |
	| IV  | Lydian b3   | 2 1 3 1 2 2 1 | C  D  Eb F# G  A  B  | F  G  Ab B  C  D  E  |
	| V   | Myxolyd. b2 | 1 3 1 2 2 1 2 | C  Db E  F  G  A  Bb | G  Ab B  C  D  E  F  |
	| VI  | Lyd. aug#2  | 3 1 2 2 1 2 1 | C  D# E  F# G# A  B  | Ab B  C  D  E  F  G  |
	| VII | Locryan bb7 | 1 2 2 1 2 1 3 | C  Db Eb F  Gb Ab A  | B  C  D  E  F  G  Ab |


## Double Harmonic scales

Has two harmonic sequences 1 3 1 and a full tone.

	| N   | Name        | Pattern       | Transposed on C      | Rotations            |
	|-----|-------------|---------------|----------------------|----------------------|
	| I   | D.Harm.Maj. | 1 3 1 2 1 3 1 | C  Db E  F  G  Ab B  | C  Db E  F  G  Ab B  | Bizantine
	| II  | Lydian #2#6 | 3 1 2 1 3 1 1 | C  D# F  F# G  A# B  | Db E  F  G  Ab B  C  |
	| III | UltraPhryg. | 1 2 1 3 1 1 3 | C  Db Eb E  G  Ab A  | E  F  G  Ab B  C  Db |
	| IV  | Gypsy Minor | 2 1 3 1 1 3 1 | C  D  Eb F# G  Ab B  | F  G  Ab B  C  Db E  | Hungarian minor
	| V   | Oriental    | 1 3 1 1 3 1 2 | C  Db E  F  Gb A  Bb | G  Ab B  C  Db E  F  |
	| VI  | Ionian #2#5 | 3 1 1 3 1 2 1 | C  D# E  F  G# A  B  | Ab B  C  Db E  F  G  |
	| VII | Loc. bb3bb7 | 1 1 3 1 2 1 3 | C  Db D  F  Gb Ab A  | B  C  Db E  F  G  Ab |

AKA

- North Indian Thaat named Bhairav
- South Indian (Carnatic) Melakarta named Mayamalavagowla. 

Songs:

- Misirlou E Double Harmonic


## Diminished scales

Octatonic scale of altering half and full tones.

	| N   | Name             | Pattern         | Transposed on C         | Rotations            |
	|-----|------------------|-----------------|-------------------------|----------------------|
	| I   | Diminished       | 2 1 2 1 2 1 2 1 | C  D  Eb F  Gb Ab A  B  | C  D  E  F  G  Ab B  |
	| II  | Dimini. inverted | 1 2 1 2 1 2 1 2 | C  Db Eb E  Gb F  A Bb  | D  E  F  G  Ab B  C  |


## Other scales

	C  Eb F  Gb G  Bb - 3 2 1 1 3 2 - Blues (minor pentatonic plus a perfect 4th)

## Non-western scales (Western classic view)

Taken from [here](https://ukebuddy.com/ukulele-scales/C-gypsy-scale)
Origins are western perspective on how it sounds.
Indeed each of those culture use many scales including some of the considered "western scales".

Pentatonics

	| Origin     | intervals           |               |                      |
	|------------|---------------------|---------------|----------------------|
	| Egyptian   | 1  2     4  5    b7 | 2 3 2 3 2     | C  D     F  G     Bb |
	| Chinese    | 1     3 #4  5     7 | 4 2 1 4 1     | C     E  F# G     B  |
	| Japanese   | 1 b2     4  5 b6    | 1 4 2 1 4     | C  Bb    F  G  Ab    |

Heptatonics:
[Egyptian](),
[Persian](https://en.wikipedia.org/wiki/Persian_scale),

	| Origin     | intervals           |               |                      |
	|------------|---------------------|---------------|----------------------|
	| Persian    | 1 b2  3  4 #4 b6  7 | 1 3 1 1 2 3 1 | C  Db E  F  Gb Ab B  |
	| Indian     | 1  2  3  4  5 b6 b7 | 2 2 1 2 1 2 2 | C  D  E  F  G  Ab Bb |
	| Arabic     | 1  2  3  4 #4 b6 b7 | 2 2 1 1 2 2 2 | C  D  E  F  Gb Ab Bb |
	| Jewish     | 1 b2  3  4  5 b6 b7 | 1 3 1 2 1 2 2 | C  Db E  F  G  Ab Bb |
	| Gypsy      | 1  2 b3 #4  5 b6 b7 | 2 1 3 1 1 2 2 | C  D  Eb F# G  Ab Bb |

1 3 1 2 1 3 1

C Db E F G Ab B


