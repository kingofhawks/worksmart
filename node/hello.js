/**
 * Created by dell on 2015/10/27.
 */
var watchman = require('fb-watchman');
var client = new watchman.Client();
console.log('hello')

  var fs = require('fs-extra')

  fs.copy("E:\\workspace\\hello.txt", 'E:\\hello.txt', function (err) {
    if (err) return console.error(err)
    console.log("success!")
  }) // copies file
  
  var data = {};
  Object.getPrototypeOf(data);
  