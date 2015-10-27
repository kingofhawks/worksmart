var fs = require('fs-extra')
var path2 = require('path')

var chokidar = require('chokidar');

// One-liner for current directory, ignores .dotfiles
var watcher = chokidar.watch('D:\\workspace_eclipse-SDK-3.3.2-win32_2\\jar_depend\\pickup', {ignored: /[\/\\]\./});

var log = console.log.bind(console);
watcher
  .on('add', function(path) {
      log('File', path, 'has been added');
      //TODO copy file

      //var filename = path2.basename(path);
      //console.log(filename);
      //fs.copy(path, 'E:\\workspace\\yycoin\\osgi\\pickup\\'+filename, function (err) {
      //  if (err) return console.error(err)
      //  console.log("success!")
      //}) // copies file
    })
  .on('change', function(path) {
      log('File', path, 'has been changed');
      //copy file
      var filename = path2.basename(path);
      var destinationPath = 'G:\\OneDrive\\Workspace\\yycoin\\osgi\\pickup\\'+filename;
      fs.copy(path, destinationPath, function (err) {
        if (err) return console.error(err)
        console.log(destinationPath+" updated success!")
      }) // copies file
    })
