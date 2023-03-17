# Relay för att överföra koordinater från ZeroKey UWB till pepper

Relay är ett python program som använder SignalR-core för att koppla till ZeroKeys UWB system som kräver Python 3 och för över informationen via http till Pepper som kör Python 2.  

## Installation-guide

För att komma igång, klona repo:et 

`https://github.com/mebakid74/Human-Health-and-Activity-Laboratory-H2Al-UWB-navigering-av-robot.git`

1, Installera signalR-core för python

`pip install signalrcore`

2, Modiferiera addresserna för urlEH och urlApi till den för din ZeroKey hub

3, Kör koden

