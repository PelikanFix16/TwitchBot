const TwitchBot = require('node-twitchbot')
var fs = require('fs');


const Bot = new TwitchBot({
  username : 'fssfgsfgsfgsf',
  oauth    : 'oauth:9nbc2b5jba18ekeoybz31t0heiq3px',
  channel  : 'powerdwarffather'
})

Bot.connect().then(()=>{
  console.log("Connected");
  Bot.msg("Dzisiaj tylko overwatch ?")
});
//  Bot.msg('this is the message text PogChamp')

fs.readFile('', 'utf8', function(err, contents) {
    console.log(contents);
});
