var fs = require('fs-extra')
var path2 = require('path')

var chokidar = require('chokidar');

// One-liner for current directory, ignores .dotfiles
watcher = chokidar.watch('D:\\workspace_eclipse-SDK-3.3.2-win32_2\\jar_depend\\pickup', {ignored: /[\/\\]\./});

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
      //TODO copy file

      var filename = path2.basename(path);
      console.log(filename);
      fs.copy(path, 'E:\\workspace\\yycoin\\osgi\\pickup\\'+filename, function (err) {
        if (err) return console.error(err)
        console.log("success!")
      }) // copies file
    })
  //.on('unlink', function(path) { log('File', path, 'has been removed'); })
  //// More events.
  //.on('addDir', function(path) { log('Directory', path, 'has been added'); })
  //.on('unlinkDir', function(path) { log('Directory', path, 'has been removed'); })
  //.on('error', function(error) { log('Error happened', error); })
  //.on('ready', function() { log('Initial scan complete. Ready for changes.'); })
  //.on('raw', function(event, path, details) { log('Raw event info:', event, path, details); })


// Example of a more typical implementation structure:
//
//// Initialize watcher
//var watcher = chokidar.watch('file, dir, glob, or array', {
//  ignored: /[\/\\]\./,
//  persistent: true
//});
//
//// something to use when events are received
//var log = console.log.bind(console);
//
//// Add event listeners
//watcher
//  .on('add', function(path) { log('File', path, 'has been added'); })
//  .on('change', function(path) { log('File', path, 'has been changed'); })
//  .on('unlink', function(path) { log('File', path, 'has been removed'); })
//  // More events.
//  .on('addDir', function(path) { log('Directory', path, 'has been added'); })
//  .on('unlinkDir', function(path) { log('Directory', path, 'has been removed'); })
//  .on('error', function(error) { log('Error happened', error); })
//  .on('ready', function() { log('Initial scan complete. Ready for changes.'); })
//  .on('raw', function(event, path, details) { log('Raw event info:', event, path, details); })
//
//// 'add', 'addDir' and 'change' events also receive stat() results as second
//// argument when available: http://nodejs.org/api/fs.html#fs_class_fs_stats
//watcher.on('change', function(path, stats) {
//  if (stats) console.log('File', path, 'changed size to', stats.size);
//});
//
//// Watch new files.
//watcher.add('new-file');
//watcher.add(['new-file-2', 'new-file-3', '**/other-file*']);
//
//// Un-watch some files.
//watcher.unwatch('new-file*');
//
//// Only needed if watching is `persistent: true`.
//watcher.close();
//
//// Full list of options. See below for descriptions. (do not use this example)
//chokidar.watch('file', {
//  persistent: true,
//
//  ignored: '*.txt',
//  ignoreInitial: false,
//  followSymlinks: true,
//  cwd: '.',
//
//  usePolling: true,
//  interval: 100,
//  binaryInterval: 300,
//  alwaysStat: false,
//  depth: 99,
//  awaitWriteFinish: {
//    stabilityThreshold: 2000,
//    pollInterval: 100
//  },
//
//  ignorePermissionErrors: false,
//  atomic: true
//});