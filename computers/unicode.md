# Unicode

Unicode és un estàndard que unifica múltiples conjunts de caràcters internacionals
en una sola taula de correspondència representacional.

## Context històric

Abans d'Unicode:

- Cada idioma i fabricant feia servir una o varies correspondències de bytes a caràcters
- Per interpretar correctament un text calia saber primer quina correspondència fa servir. Els mateix stream de bytes pot correspondre a diferents caràcters depenent de la codificació.
- No es podia barrejar en un mateix text caràcters de diferents taules de correspondència.

Estandards pre-existents

- Primeres codificacions del telègraf traspasades al teletip (boudot i variants nacionals, ITA...)
    - No ordenables, sense caixa (majúscules, minúscules)
- ASCII primer estàndard, abarca només anglés modern, 7bits
    - Ordenats, el valor numèric es pot fer servir per ordernar alfabèticament
    - Conversió de caixa (majúscules, minúscules) amb inversió d'un bit.
- Extensions d'ASCII
    - Com ASCII està molt establert la majoria de codificacions el respecten com a base
    - Fan servir el 8è bit per extendre-ho a d'altres idiomes
    - Cada fabricant proposava la seva extensió fins i tot pel mateix llenguatge: (IBM/DOS/Windows code pages, MacRoman/MacCirilic, JI, KO...)
    - Alguns idiomes com ara el asiàtics, no tenien prou amb un byte i sovint comencen a fer-se servir codificacions multibyte.
- ISO-8859-N (N=[1..16]) estandaritzà taules estandars de caràcters per cada grup de llenguatges (Latin1-16, Latin/Arabic, Latin/Cirilic...)
    - Resol el problema de les codificacions depenent del fabricant
    - Encara calia saber quin encoding fas servir i no pots combinar llenguatges amb diferents scripts

En aquest context es proposa Unicode que consisteix en:

- Incloure tots els caràcters internacionals en un sól mapa de caràcters
- Com que tots els caràcters possibles no hi caben a un sol byte, cal superar la correspondència entre un byte i un caràcter, i es proposa que els codis siguin de 21 bits.
- S'estableixen diferents codificacions per convertir de forma òptima els codis de caràcters de 21 bits en seqüències de bytes (UTF-32/16/8).

## Definicions

**Caràcter:** En informàtica, l'unitat mínima d'un text que té valor semàntic.
Correspon normalment a un _graphema_ en lingüística, tot i que no sempre ho és.

**Glif:** Unitat gràfica que composa un text. Més a veure amb la caixa de tipus d'una impremta.

- Un gliph pot juntar diversos caràcters
- Un mateix caràcter es pot representar amb més d'un glif.

**Diacrític:** marca que modifica un caràcter, com ara el accents, la cedilla...
Una codificació pot establir dos estratègies:

- Modificadors: el diacrític es un modificador d'un caràcter base
- Precomposats: Codificar les variacions integrades amb el caràcter principal

Els modificadors serien anàlogs al que fan les màquines d'escriure antigues,
no movien el carro perque la següent lletra es sobre imprimís.
ELs precomposats serien anàlogs als tipus de les empremtes.
Les empremtes tenien que tenir un tipus per cada accent que es volia fer servir amb cada lletra.

Sovint ambdues estratègies estan disponibles.
Els precomposats existeixen sovint perque les codificacions antigues els incloien.
Si el mateix caracter compost es pot fer de dues maneres,
és un handicap de cara a comparar cadenes que haurien de ser equivalents.
Les aplicacions normalitzen tot el text en una o l'altra forma:

- FNC: Forma normal C: Tot precompost
- FND: Forma normal D: Tot decompost, si hi ha diversos modificadors, en un ordre establert.


**Lligadura:** Variació en el glif d'un caràcter que depén dels caràcters que l'envolten.
Per exemple, les lletres de l'àrab s'escriuen de forma diferent si van lligades, o no, per davant o per darrera.
De fet, en l'script llatí, quan s'escriu a mà sovint es fa lligadura.

**Codi de control:** Codis especials que en comptes de representar un caràcter, representen instruccions: Canvi de línia, tabulacions, canvis de posició

**Script o Sistema d'escriptura:** Mètode simbòlic i regular de representar el llenguatge. Llatí, Arabic, Hebreu, Cirílic, Grec, Chinés, Japonés...

- Logogràfic: Un símbol correspon a una idea
- Silàbic: Un símbol correspon una sílaba
- Abjad: Un simbol per consonant, les vocals s'obvien
- Abujida: Silabarics, fan servir diacrítics per canviar la vocal per omisió
- Alfabètic: Un símbol normalment codifica un fonema

**Conjunt de caràcters (charset):** Una correspondència númerica concreta establerta entre números i caràcters per la seva representació informàtica.

**Codificació:** Una forma de representar com a seqüència de bytes el números que representen caràcters.
Pot ser directa si és single bit. No pas si és multibyte.
Col·loquialment es parla indistintament de conjunt de caràcters i codificació, però formalment no ho són, i de fet a Unicode la distinció és important.

## Proposta d'unicode

Unicode proposa estombar la limitació de codificació amb 8bits
i codificar tots els caràcters de totes les llengües en un sol conjunt de caràcters.
Per fer-ho, separa la codificació numèrica dels caràcters (code points)
de la seva representació en fluxos de bytes (encodings).

**Code Point:** Número de 21 bits que representa un caràcter (o part perque és un modificador o cap perque és un control).

- Es denoten com `U+XXXX`, on `XXXX` es la representació hexadecimal del número.

**Codificacions:** com enmagatzemar code points de forma optima en un stream de bytes.

Unicode defineix diverses codificacions:

- UTF32 (alias UCS-4): Codifica el 21 bits dintre dels 32. Simple però, ocupa molt!
- UCS-2 (obsolet): 2 bytes de longitud fixa. No pot codificar codepoints per sobre dels 16 bits (només el BMP).
- UTF16: 2 bytes amb combinacions especials de 4 bytes.
  Segueix ocupant molt, té la complexitat del byte order.
  Tenim les varietes UTF16-BE (Big endian) i UTF16-LE (litle endian) segons quin dels dos bytes del caràcter va primer.
- UTF8: 1 byte amb longitud variable de 2, 3, o 4 bytes.
  Les combinacions de 1byte son compatibles amb ASCII.

## Estructura dels code points

**Planes:** Estructura principal contenint 65.536 code points U+PPXXXX

- 0: Basic Multilingual Plane (BMP) (U+0000...U+FFFF) Lletres comunes, numeros, puntuació i símbols de la majoría de llengues actuals
- 1: Suplemental Multilingual Plane (SMP) (U+10000..U+1FFFF) Emojis, símbols no inclosos en antigues code pages, música, jocs, jerolífics...
- 2: Suplemental Ideogràfic Plane (IMP) (U+20000..U+2FFFF) Ideogrames CJK extres (xinès, japonès, coreà)
- 3-D: Sense ús actualment (U+30000..U+EFFFF)
- E: Suplemental Special Purpose Plane (U+F0000..U+10FFFF) Tags (com html pero un sól caràcter, obsolet) i _Indicadors de variant_ que serveixen per cambiar el glyph d'un caràcter. 
- F-10: Suplemental Private Area Use Plane (U+F0000..U+10FFFF)  

**Blocs:** Codepoints contigus dintre d'una plana que es reserven per una funció/script/ús.

- Basic Latin: U+0000..U+007F
- Greec and Coptic: U+0370..U+03FF
- Mathematical Operators: U+2200..U+22FF (∀∑∞)
- Box Drawing: U+2500..U+257F (╤╘)
- Emoticons: U+1F600..U+1F64F (😊)
- ...

<https://www.unicode.org/charts/About.html?utm_source=chatgpt.com>

**Categories:** Propietat del code point que indica com interpretar el símbol <https://www.compart.com/en/unicode/category>

Es marquen amb dos lletres, una majúscula que indica supercategoria i una minúscula que indica la subcategoria:

- Categoria: Dos lletres, la primera lletra es majuscula i indica supercategoria, la segona subcategoria en minúscula
    - L lletra
        - Lu upper
        - Ll lower
        - Lt titol, combina Maj+Min
        - Lm lletres que fan de modificadores d'altres (per fonética)
        - Lo altres (no consideren majuscules ni minúscules)
    - M marca combinable
        - Mn no afegeixen espai: acents, cedilles...
        - Mc ocupen espai addicional (scripts subasiàtics)
        - Me enclosing, afegeixen un mark (tecla, multiplicadors numerics al cirílic...)
    - N números
        - Nd dígits decimals (0-9 en diferents scripts i glifs)
        - Nl números literaris (romans, maies...)
        - No altres números (sub/superindexos, fraccions...)
    - P puntuació
        - Pc Connector: `l_i‿g⁀a⁔d﹏u＿r﹎a﹍s` (underline and friends)
        - Pd Dash: Indican ruptura o separación hyphen and friends.
        - Ps Start: Apertura parentesis, claudators... {[(
        - Pe End: Cierre parentesis, claudators... }])
        - Pi Initial: Inicio de frase: apertura comillas orientadas, virguillas «‘“
        - Pf Final: Final de frase: cierre comillas orientadas, virguillas »’”›
        - Po Other: El resto
    - S símbols
        - Sc Coin $€¢£¥¤₿
        - Sm Math 
        - Sk Modificadors (El símbol combinable Mn pero aillat sense combinar)
        - So Altres: ©®࿕⌬⏯⏳
    - Z separadors
        - Zs paraules
        - Zl línies
        - Zp parrafs
    - C Other
        - Cc control
        - Cf formateig
        - Cs surrogats
        - Co us privat
        - Cn no assignat

Cada code point té un seguit de propietats importants:

- Direcció (LTR RTL)
- Script: (Common, Arabic, Han, Latin...)
- Descomposable: Si es pot reduir a una composicio (caràcters amb accent, emojis...)
- Emoji combinable: Amb quins sets d'emojis es pot combinar (skin tone, sex, country, activity...)
- Default presentation: Si es text, podem canviar-ho a emoji posant despres U+FE0F, si es emoji a text amb U+FE0E


## Combinacións de caràcters

- Precomposats: sovint ja existeix la combinació perque historicament ja hi era als code pages: à ñ...
- S'habiliten mecanismes genèrics per obtenir-los U+0061 a + U+0301 ◌́
- Aixó genera dos formes de obtindre la mateixa paraula, important per fer cerques
- Forma normal C: Tot en precompost si existeix
- Forma normal D: Tot en descompost amb modificadors ordenats 




Propietats relacionades:

- Representació dual: text (shape monocrom) i emoji (imatge) `Default_Presentation = text / emoji /none`
    - Si es text o emoji ho podem canviar sufixant U+FE0F (-> emoji) o U+FE0E (-> text)
    - U+2764 ♥ però U+2764 U+FE0F ❤️ 
    - U+1F600 😄pero U+1F600 U+FE0E 
- Banderes nacionals: U+1F1E6..U+1F1FF representen les lletres pel codi de nació
    - U+1F1EA U+1F1F8 -> E+S -> 
- To de pell: Base (usually hard yellow) + To de pell
    - La base ha de tenir la propietat `Emoji_Modifier_Base = Yes`
    - Normalment son persones o parts de persones o animals humanitzats 👍
    - Tons de pell U+1F3FB..U+1F3FF segons l'escala Fitzpatrick
- Genere: Person + U+200D (ZWJ) + ♀ U+2640  o ♂ U+2642

https://www.unicode.org/Public/emoji/latest/emoji-zwj-sequences.txt 



## Codificació UTF8:

- `0xxx_xxxx` Si el bit mes significatiu es 0, es single byte (compatible ASCII 7bits) 
- `11xx_xxxx` Si els dos o més bits mes significatiu son 1, es un multibyte, de tants bytes com bits a un més significatius hi ha 
- `10xx_xxxx` Si només hi ha un 1 més significatiu és un byte de continuació d'un multibyte aportant 6 bits de valor.

Bytes, interval, patró, bits d'informació

- 1 bytes:    U+00 -     U+7F   0xxx_xxxx (7 bits)
- 2 bytes:    U+80 -   U+07FF   110x_xxxx 10xx_xxxx (11 bits)
- 3 bytes:  U+0800 -   U+FFFF   1110_xxxx 10xx_xxxx 10xx_xxxx (16 bits)
- 4 bytes: U+10000 - U+10FFFF   1111_0xxx 10xx_xxxx 10xx_xxxx 10xx_xxxx (21 bits)

Encara que un codepoint baix, pe. 0xAF, es pogues representar amb 1, 2, 3 o 4 bytes,
ha de representar-se amb el nombre minim de bytes possibles.

**Overlong:** Error per representar un codepoint amb més bytes dels que li cal.
Fa que algunes combinacions de bits siguin il·legals.

**Surrogates:**
Un seguit de codepoints (U+D800 - U+DFFF) reservats per a que utf16 pugui codificar més enllà dels 16bits.
UTF16 codifica amb 32 bits els codepoints que tenen 21bits.
`1101_10xx` per la part alta i `1101_11xx` per la part baixa.

High and low parts codify 10 bits, and the 11th bit is 1.

Els surrogate code points no tenen caràcter associat i
per això les codificacions que els correspondrien també són invàlids a UTF8.
U+D800..U+DFFF (ED A0 80..ED BF BF)

També són invàlides les seqüència en les que toca un continuation byte,
però, es menor que 08, o major que BF.

Codificacio:

    funcio package(codepoint: uint32, bitshift):
        six_lower_bits = 0x3f
        return (codepoint >> (bitshift)) & six_lower_bits

    funcio codifica(codepoint: uint32, stream):
        codepoint <= 0x7F ->
            stream.put(codepoint)
        codepoint <= 0x7FF ->
            stream.put(0xC0 | package(codepoint, 6))
            stream.put(0x80 | package(codepoint, 0))
        codepoint <= 0xFFFF ->
            0xD800 <= codepoint <= 0xDFFF -> error("Surrogate no vàlid")
            stream.put(0xE0 | package(codepoint, 12))
            stream.put(0x80 | package(codepoint, 6))
            stream.put(0x80 | package(codepoint, 0))
        codepoint <= 0x10FFFF ->
            stream.put(0xF0 | package(codepoint, 18))
            stream.put(0x80 | package(codepoint, 12))
            stream.put(0x80 | package(codepoint, 6))
            stream.put(0x80 | package(codepoint, 0))
        else -> error
    
Validació:

```C
static inline int is_cont(unsigned char b) {
    /* continuation byte: 10xxxxxx (80–BF) */
    return (b & 0xC0) == 0x80;
}

static inline int advance_utf8_char(const unsigned char *s, const unsigned char *end) {

    /* 1 byte
     * U+0000..U+007F (00..7F)
     */
    if (s[0] <= 0x7F) return 1;

    /* 2 bytes
     * U+0080..U+07FF (C2 80..DF BF)
     */
    if (s[0] <= 0xDF) {
        if (s[0] < 0xC2) return 0; /* overlong */
        if (s+2 > end) return 0; /* too short */
        if (!is_cont(s[1])) return 0;
        return 2;
    }

    /* 3 bytes
     * U+0800..U+FFFF (E0 A0 80..EF BF BF)
     * excl. surrogates U+D800..U+DFFF (ED A0 80..ED BF BF)
     */
    if (s[0] <= 0xEF) {
        if (s+3 > end) return 0; /* too short */

        if (!is_cont(s[1]) || !is_cont(s[2]))
            return 0;

        if (s[0] == 0xE0 && s[1] < 0xA0) return 0; /* overlong */
        if (s[0] == 0xED && s[1] >= 0xA0) return 0; /* surrogates */

        return 3;
    }

    /* 4 bytes
     * U+10000–U+10FFFF (F0 90 80 80 – F4 8F BF BF)
     */
    if (s[0] <= 0xF4) {
        if (s+4 > end) return 0; /* too short */

        if (!is_cont(s[1]) || !is_cont(s[2]) || !is_cont(s[3]))
            return 0;

        if (s[0] == 0xF0 && s[1] < 0x90) return 0 /* overlong */
        if (s[0] == 0xF4 && s[1] > 0x8F) return 0 /* beyond range */

        return 4;
    }

    /* invalid leading byte (F5–FF) */
    return 0;
}

static inline size_t first_non_zero_byte(uint64_t mask) {
#ifdef __GNUC__
    return __builtin_ctzll(mask) >> 3;
#else
    // portable fallback
    for (size_t i = 0; i < 8; i++) {
        if (mask & (0x80ULL << (i * 8))) return i;
    }
    return 8;
#endif
}

/* Valida */
size_t utf8_validate_block(const unsigned char *s, size_t len) {
    size_t i = 0;
    while (i < len) {
        uintptr_t p = (uintptr_t)(s + i);

        // Fast-path ASCII: 8 bytes aligned
        if ((p & 0x7) == 0 && i + 8 <= len) {
            uint64_t block = *(uint64_t*)(p);
            uint64_t mask = block & 0x8080808080808080ULL;
            if (mask == 0) {
                i += 8;
                continue;
            }
            i += first_non_zero_byte(mask)
        }

        // Fallback multibyte
        size_t adv = advance_utf8_char(s + i, s + len);
        if (adv == 0) return i;  // first invalid char
        i += adv;
    }

    return len; // todo válido
}
```

Decodificació:

```C
uint32_t decode_utf8_char(const unsigned char * buffer, size_t char_size) {
    switch (char_size) {
        case 1: return buffer[0];
        case 2: return (
            (uint32_t(buffer[0] & 0x1F) << 6) |
            (uint32_t(buffer[1] & 0x3F))
        )
        case 3: return (
            (uint32_t(buffer[0] & 0x0F) << 12) |
            (uint32_t(buffer[1] & 0x3F) << 6) |
            (uint32_t(buffer[2] & 0x3F))
        )
        case 4: return (
            (uint32_t(buffer[0] & 0x07) << 18) |
            (uint32_t(buffer[1] & 0x3F) << 12) |
            (uint32_t(buffer[2] & 0x3F) << 6) |
            (uint32_t(buffer[3] & 0x3F))
        )
    }
    return 0
}
```
Printables (Utf-8 valido y visible):

    0x0000 - 0x001F C0 Control
    0x0020 - 0x009F Printable ASCII
    0x00A0 - 0xD7FF Most BMP (Basic Multilingual Plane)
    0xD800 - 0xDFFF Surrogates and non chars
    0xE000 - 0xFDCF Printable
    0xFDD0 - 0xFDEF Surrogates and non chars
    0xFDF0 - 0xFFFD Printable
    0xFFFE Surrogates and non chars
    0xFFFF - 0x10ffff Printable
    U+200B - U+200F (Zero Width Space, etc.), 3 bytes.
    U+2028 - U+202F (Line Separator, Narrow No-Break Space), 3 bytes.              


```C
/* . == #x0A */
(str[offset] == 0x0A)

/* #x20 <= . <= #x7E */
(str[offset] >= 0x20 && str[offset] <= 0x7E)

/* #0xA0 <= . <= #xD7FF */
(str[offset] == 0xC2
          && HAS_BYTES_AVAILABLE(string, offset, 2)
          && str[offset+1] >= 0xA0)

(str[offset] > 0xC2 && str[offset] < 0xED)
     
(str[offset] == 0xED
          && HAS_BYTES_AVAILABLE(string, offset, 2)
          && str[offset+1] < 0xA0)

(str[offset] == 0xEE)

/* #xE000 <= . <= #xFFFD */
(str[offset] == 0xEF
          && HAS_BYTES_AVAILABLE(string, offset, 3)
          && !(str[offset+1] == 0xBB        /* && . != #xFEFF */
              && str[offset+2] == 0xBF)
          && !(str[offset+1] == 0xBF
              && (str[offset+2] == 0xBE
                  || str[offset+2] == 0xBF))
)

/* #x10000 <= . <= #x10FFFF */
(str[offset] >= 0xF0 && str[offset] <= 0xF4)




if (c < 0x20) {
    return true;  // C0 control codes
} else if (c <= 0x7e) {
    return false;  // printable ASCII
} else if (c <= 0x9f) {
    return true;  // C1 control codes
} else if (c < 0xd800) {
    return false;  // most of the BMP
} else if (c <= 0xdfff || (0xfdd0 <= c && c <= 0xfdef) || (c & 0xfffe) == 0xfffe) {
    return true;  // surrogate or noncharacter code points
} else if (c <= 0x10ffff) {
    return false;  // all else
} else {
    return true;  // not a code point
}

#define IS_PRINTABLE_AT(string,offset) (                                        \                               
      /* 1 byte utf8/ascii U+0000.. U+0073 (00..7E) */                          \                               
      /* Excludes ascii C0 control codes 00..1F but x0A (\n) */                 \                               
      ((string).pointer[offset] == 0x0A)                                        \                               
      /* Printable ascii: (20..7E), skips x7F (Del) */                          \                               
      || ((string).pointer[offset] >= 0x20                                      \                               
          && (string).pointer[offset] <= 0x7E)                                  \                               
      /* 2 bytes UTF8: U+0080..U+07FF (C2 80..DF BF) */                         \                               
      /* U+00A0 (C2 A0)..U+00bf (C2 BF) */                                        \                             
      /* Exclude overlong < (C2 80) */                                          \                               
      /* Exclude C1 Control U+80..U+9F (C2 80..C2 9F) */                          \                             
      /* Lazily accepting bad continuation bytes, so accepts till C2 FF */      \                               
      || ((string).pointer[offset] == 0xC2                                      \                               
          && (string).pointer[offset+1] >= 0xA0)                                \                               
      /* U+00E0 (C3 A0)..U+07ff (DF BF) */                                        \                             
      /* U+0800 (E0 A0 80)..U+CFFF (EC BF BF) */                                  \                             
      || ((string).pointer[offset] > 0xC2                                       \                               
          && (string).pointer[offset] < 0xED)                                   \                               
      /* U+D000 (ED 80 80)..U+D7FF (ED 9F BF) */                                  \                             
      || ((string).pointer[offset] == 0xED                                      \                               
          && (string).pointer[offset+1] < 0xA0)                                 \                               
      /* skipping U+D800 (ED A0 80)..U+DFFF (ED BF BF) surrogates */              \                             
      /* U+E000 (EE 80 80)..U+EFFF (EE BF BF) */                                         \                      
      || ((string).pointer[offset] == 0xEE)                                     \                               
      /* uF000 (EF 80 80)..U+FFFF (EF BF BF) */                                  \                              
      /* Excluding BOM \uFEFF (EF BB BF) */                                     \                               
      /* Excluding Non caracter U+FFFE (EE BF BE) */                            \                               
      /* Excluding Non caracter U+FFFF (EE BF BF) */                            \                               
      || ((string).pointer[offset] == 0xEF      /* #xE000 <= . <= #xFFFD */     \                               
          && !((string).pointer[offset+1] == 0xBB        /* && . != #xFEFF */   \                               
              && (string).pointer[offset+2] == 0xBF)                            \                               
          && !((string).pointer[offset+1] == 0xBF                               \                               
              && ((string).pointer[offset+2] == 0xBE                            \                               
                  || (string).pointer[offset+2] == 0xBF)))                      \                               
      || ((string).pointer[offset] >= 0xF0       /* #x10000 <= . <= #x10FFFF */ \                               
          && (string).pointer[offset] <= 0xF4)                                  \                               
      )                                                                         \                               

#define IS_NON_PRINTABLE_AT(string, offset) (                               \
    /* ASCII control (except LF) */                                         \
    (((string).pointer[offset] < 0x20 &&                                   \
      (string).pointer[offset] != 0x0A))                                    \
 || ((string).pointer[offset] == 0x7F)                                     \
                                                                           \
    /* C1 control: U+0080..U+009F (C2 80..C2 9F) */                          \
 || ((string).pointer[offset] == 0xC2 &&                                   \
     (string).pointer[offset+1] < 0xA0)                                     \
                                                                           \
    /* Surrogates: U+D800..U+DFFF (ED A0..ED BF) */                          \
 || ((string).pointer[offset] == 0xED &&                                   \
     (string).pointer[offset+1] >= 0xA0)                                    \
                                                                           \
 || ((string).pointer[offset] == 0xEF &&                                   \
     (string).pointer[offset+1] == 0xBB &&                                  \
     (string).pointer[offset+2] == 0xBF)                                    \
                                                                           \
 || ((string).pointer[offset] == 0xEF && (                                  \
        /* BOM: U+FEFF (EF BB BF) */                                            \
        ((string).pointer[offset+1] == 0xBB &&                              \
         (string).pointer[offset+2] == 0xBF) ||                             \
        /* Non-characters: U+FFFE, U+FFFF */                                    \
        ((string).pointer[offset+1] == 0xBF &&                              \
         (((string).pointer[offset+2] & 0xFE) == 0xBE))
    )))
```

