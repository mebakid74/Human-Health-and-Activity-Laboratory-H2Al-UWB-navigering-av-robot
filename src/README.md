# Fallhandler och navigering av pepper

Denna mapp innehåller koden som körs på Pepper

## Installation-guide

1, För över filerna till Pepper genom SSH

`ssh nao@(ip för din pepper)`

2, Kör relay i mappen relaysrc

3, Modifiera main.py:

`Ändra ip i relayUrl till ip:n på den maskin som kör relay`

`Ändra robotIp till IP:n för din Pepper`

`Om allt är korrekt ska koordinaterna från ditt ZeroKey UWB system skrivas ut`

4, Modifiera "goal" i funktionen turn som finns i navigation till Peppers rotation när den står i nagativ X riktning enligt ZeroKeys koordinater.

`Kör motion.getRobotPosition(True) på Pepper för att få dens koordinater`

`Den tredje utskriften i dessa koordinater lägger du in som "goal" i turn i nav.py`

5, Starta GUI Fall Fandler enligt instruktionrna i Readme:
`https://github.com/mebakid74/Human-Health-and-Activity-Laboratory-H2Al-UWB-navigering-av-robot/blob/main/GUI%20Fall%20Handler/README.md`
