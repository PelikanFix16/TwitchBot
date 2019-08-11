var twitchStreams = require('twitch-get-stream')('jzkbprff40iqj646a697cyrvl0zt2m6');

  twitchStreams.get('szpanel')
      .then(function(streams) {
          console.log(streams[1].url);
      });
