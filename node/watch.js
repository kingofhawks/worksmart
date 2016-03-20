var fs = require('fs-extra')
var path2 = require('path')

var chokidar = require('chokidar');
var nconf = require('nconf');
nconf.argv()
   .env()
   .file({ file: 'config/config.json' });
   
  //
  // Set a few variables on `nconf`.
  //
  nconf.set('yycoin:jar_depend', '127.0.0.1');
  nconf.set('yycoin:pickup', 5984);

  //
  // Get the entire database object from nconf. This will output
  // { host: '127.0.0.1', port: 5984 }
  //
  console.log('foo: ' + nconf.get('foo'));
  console.log('NODE_ENV: ' + nconf.get('NODE_ENV'));
  console.log('database: ' + nconf.get('database'));

  //
  // Save the configuration object to disk
  //
//   nconf.save(function (err) {
//     fs.readFile('config/config.json', function (err, data) {
//       console.dir(JSON.parse(data.toString()))
//     });
//   });

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
        var now = new Date();
        console.log(destinationPath+" updated success at time:"+now);
      }) // copies file
      
      var destinationPath2 = 'D:\\workspace_eclipse-SDK-3.3.2-win32_2\\jar_depend\\'+filename;
      fs.copy(path, destinationPath2, function (err) {
        if (err) return console.error(err)
        var now = new Date();
        console.log(destinationPath+" updated success at time:"+now);
      }) // copies file
    })
