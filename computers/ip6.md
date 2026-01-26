# IPv6

Millores:

- Adreces de 32bits (4k3 millions) a 128bits (gairebé infinites, 3.4e+38)
- Deixa obsolet el NAT (ip's privades sortint per IP's públiques)
- Simplificació capceleres (gestió més eficient)
- IPSec (xifrat) de serie, a ipv4 era afegitò
- Autoconfiguració via SLAAC (deixa obsolet DHCP)

Capcelera: 5 paraules de 64

1. Metadades
    - Versió (4bits)
    - Traffic class (8bits) prioritat, QoS, congestio
        - DSCP (6bits) cua de prioritat que farà servir (normal, voip, video stream, alta, baixa...)
        - ECN (2bits) els dispositius intermitjos els modifiquen per indicar congestió
    - Flow label (20bits) id de fluxe permet als dispositius pendre les decissions ja presses pels paquets anteriors sense mirar més a dins
    - Payload lenght (16bits)
    - Next header (8bits) identificador del protocol contingut (Extension Header, TCP, UDP...)
    - Hop Limit (8bits) anàleg al TTL
2. Subxarxa origen
3. Host origen
4. Subxarxa desti
5. Host desti

S'eliminen respecte a IP4

- Check-sum: Ja es fa a d'altres nivells de la pila
- Fragmentació: Es fa de forma diferent
    - Si no hi caben donat l'MTU, els dispositius de xarxa reboten un missatge de "Packet too big" amb l'mtu del cami i l'emisor el reenvia amb el tamany adient.
- Tamany de la capcelera: Ara es fixe donat que no inclou les extensions.
    - Les extensions van a part amb capceleres addicionals
    - Si s'indica el tamany del payload

Extensions no reserven espai a la capcelera, son opcionals i son capceleres posteriors indicades al "next header".
Els nodes intermitjos només necessiten procesar aquelles que els incumbeixen i poden ignorar les que no.
IPSec esdevé part del protocol i els dispositius l'han de suportar.

SLAAC autoconfiguració d'adreces, substitueix HDCP.
L'adreça consta de dos meitats la de subxarxa que proporciona el router,
i la del host que proporciona el dispositiu connectat (com la MAC).
SLAAC es el protocol pel cual, en connectar-se el dispositiu
pregunta quina es la subxarxa i comproba que ningú altre en la subxarxa tingui la mateixa part de host.


