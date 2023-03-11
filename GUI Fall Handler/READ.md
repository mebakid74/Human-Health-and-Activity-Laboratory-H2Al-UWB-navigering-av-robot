# GUI Fall Handler via Zoom SDK

Denna mapp är en HTML / CSS / JavaScript / NodeJS som används [Zoom möte SDK] (https://marketplace.zoom.us/docs/sdk/native-sdks/web)
för att gå med i ett zoom video samtal.

## Installation-guide

För att komma igång, klona repo:et 

`https://github.com/mebakid74/Human-Health-and-Activity-Laboratory-H2Al-UWB-navigering-av-robot.git`

1, Navigera till `GUI Fall Handler` katalogen:

`$ cd Server`

 `npm --version`

 `npm install`

 `npm init`

 `npm install express`

 `npm install path`

2, Navigera till `Server -> public` för att ändra filerna `html` `css`

3, Navigera till `Server -> app.js` för att ändra servern 

4, Navigera till `Frontend -> gui.py` för att kalla filerna från `Server -> public`

5, Starta server från `cd Server` i terminalen skriv `node app.js` då 

6, Öppna i webbläsaren på din localhost https://localhost:3000 eller på servern t.ex http://130.240.200.103:5000/

## Pepper's surfplatta

För att visa upp webbsidan, då kan du använda två sätt:

    **OBS** Roboten hjärna och den inbyggda surfplattan kommunicerar ej på samma sätt:

För att aktivera utvecklarläget på surfplattan bör du följa dessa steg:

     1, Logga in med pepper's egen inloggningsuppgifter på terminalen.

     2, I terminalen skriv `qicli call ALTabletService._openSettings`.

     3, Under `Device` navigera till `Home`. 

     4, Byte till `Launcher3` och starta om roboten.


## Showcase

Bilderna nedanför visar den övergripande demo/prototyp av vår applikation med ett obefintlig personnnumer `909090-0000` 
och lösenord `pepper`:

  ### Patient login sida
![Inloggningsida](https://user-images.githubusercontent.com/76616663/224494276-4b0d26f3-4db1-469e-92e0-ee29fe8d6d69.jpg)

  ### Huvudsidan
![Huvudsida](https://user-images.githubusercontent.com/76616663/224494324-559da4d3-59e0-4f75-8a5f-0e0e634ea61c.jpg)

  ### Video demonstration

https://www.youtube.com/watch?v=2ZL-X0YFo0Y


## Alternativ användning

Exempel:

   ```js
   var CLIENT_ID = "YOUR_CLIENT_ID_OR_SDK_KEY"
   var CLIENT_SECRET = "YOUR_CLIENT_SECRET_OR_SDK_SECRET"
   ```

   ```js
   var authEndpoint = ''
   var sdkKey = ''
   var meetingNumber = ''
   var passWord = ''
   var role = 0
   var userName = ''
   var userEmail = ''
   var registrantToken = ''
   var leaveUrl = ''
   ```

## Behöver hjälp?
Om du letar efter mer stöd, vänligen ta ett kik på: https://marketplace.zoom.us/docs/sdk/native-sdks/web/
