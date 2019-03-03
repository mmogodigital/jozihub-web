const dns = require('dns');

dns.resolve('mycolour.co', 'ANY', (err, records) => {
  console.log(records);
});
