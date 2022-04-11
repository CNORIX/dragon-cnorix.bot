var http = require('https');
 
// The following 4 are the actual values that pertain to your account and this specific metric.
var apiKey = '8e9f0620-0804-45e2-842f-f32c656ba7f1';
var pageId = 'm8gdg9976x9j';
var metricId = 'flzd8rbz1zjm';
var apiBase = 'https://api.statuspage.io/v1';
 
var url = apiBase + '/pages/' + pageId + '/metrics/' + metricId + '/data.json';
var authHeader = { 'Authorization': 'OAuth ' + apiKey };
var options = { method: 'POST', headers: authHeader };
 
// Need at least 1 data point for every 5 minutes.
// Submit random data for the whole day.
var totalPoints = 60 / 5;
var epochInSeconds = Math.floor(new Date() / 1000);
 
// This function gets called every second.
function submit(count) {
  count = count + 1;
 
  if(count > totalPoints) return;
 
  var currentTimestamp = epochInSeconds - (count - 1) * 5 * 60;
  var randomValue = Math.floor(Math.random() * 1000);
 
  var data = {
    timestamp: currentTimestamp,
    value: randomValue,
  };
 
  var request = http.request(url, options, function (res) {
    if (res.statusMessage === "Unauthorized") {
      const genericError =
        "Error encountered. Please ensure that your page code and authorization key are correct.";
      return console.error(genericError);
    }
    res.on("data", function () {
      console.log("Submitted point " + count + " of " + totalPoints);
    });
    res.on("end", function () {
      setTimeout(function () {
        submit(count);
      }, 1000);
    });
    res.on("error", (error) => {
      console.error(`Error caught: ${error.message}`);
    });
  });
 
  request.end(JSON.stringify({ data: data }));
}
 
// Initial call to start submitting data.
submit(0);