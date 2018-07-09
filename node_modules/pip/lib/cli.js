var freckle = require('freckle')
  , fs = require('fs')
  , path = require('path')
  , opt = require('optimist').argv
  , ConfigObj = require('./config')
  , config = new ConfigObj()
  , utils = require('./utils')
  , data
  , project_names = {};

// Add subdomain and token information here. Leaving this blank will keep API
// test account information.
freckle( config.subdomain, config.token );

/**
 * Run Ginger
 *
 * @api private
 */
run_pip = function() {

  // Collect string passed in with params.

  data = opt._;
  data.missing = new Array();

  if (opt._.length === 0) {
      opt._ = null;
  } else {

    // Pick up the command.

    command = opt._[0];

    // Display help if no command provided.

    if (command == null) {
      // @todo: display useage
    }

  }

  if (opt._ !== null) {

    // 'help' command

    if (command == 'help') {

      var help = 'Usage: pip [command] [options]'+
      '\n[Commands]'+
      '\n\tlist\t\tList project associated with your subdomain. This will give you a list of project names and their IDs which you need for logging your entries.'+
      '\n\t\t\t  ex: pip list'+
      '\n\tlog\t\tLog time entries using various options.'+
      '\n\t\t\t  ex: pip log -p 101814 -m \"quick update\" -t 15m'+
      '\n[Options]'+
      '\n\t-h, --help\tDisplay this help page.'+
      '\n\t\t\t  ex: pip -h'+
      '\n\t-t, --time\tTime entry in freckle specified format.'+
      '\n\t\t\t  ex: pip -t 15m'+
      '\n\t\t\t  ex: pip -t 1.5h'+
      '\n\t-p, --project\tThe project ID.'+
      '\n\t\t\t  ex: pip -p 101814'+
      '\n\t-m, --message\tPost a message to yammer'+
      '\n\t\t\t  ex: pip -m "I\'m working on pip"'+
      '\n\t\t\t  ex: pip -m "tag, tag, tag'+
      '\n\t-d, --date\tOptional date formated in YYYY-MM-DD. Defaults to today.'+
      '\n\t\t\t  ex: pip -d 2012-07-20'+
      '\n\t-u, --user\tOptional user to log time for. Defaults to user in config.json.'+
      '\n\t\t\t  ex: pip -u apitest@letsfreckle.com';
      console.log( help );
    }

    // 'list' command

    if (command == 'list') {
      freckle.projects.list(function( err, projects ) {
        if (err) {
          console.log(err);
        }
        for (var i = projects.length - 1; i >= 0; i--) {
          project_names[projects[i].project.id] = projects[i].project.name;
        }
        var json = JSON.stringify(project_names);
        fs.writeFileSync(config.subdomain + '-projects.json', json);
        console.log('Projects saved to ' + path.join(__dirname, config.subdomain + '-projects.json'));
      });
    }

    // 'log' command

    if (command == 'log') {

      opt.project = opt.project || opt.p;
      opt.message = opt.message || opt.m;
      opt.time = opt.time || opt.t;
      opt.date = opt.date || opt.d;
      opt.user = opt.user || opt.u;

      // --project | -p

      if (opt.project == null) {
        data.missing.push('project');
      } else {

        var intRegex = /^\d+$/
          , projects
          , keys
          , len;

        // Check to see if the project is NOT an integer (text).
        if (!intRegex.test(opt.project)) {

          var projects_path = config.subdomain + '-projects.json';

          utils.file_exists(false, projects_path, function(success, file, err){
              if (success) {

                projects = JSON.parse(fs.readFileSync(projects_path, "utf8"));
                keys = Object.keys(projects);
                len = keys.length;

                // Search for project.
                for (var i = 0; i < len; ++i) {
                  if (projects[keys[i]] == opt.project) {
                    opt.project = keys[i];
                  }
                }

                if (intRegex.test(opt.project)) {
                  console.log('Found project id: ' + opt.project);
                }
                else {
                  console.log('Could not find project: ' + opt.project + '. Please do a listing to get the exact name or id (pip list).');
                  data.missing.push('project');
                }
              } else {
                // msg that listing needs generated
              }
          });

        } else {
          // @todo: we should probably validate the id as well before we send it along
        }

      }

      // --message | -m

      if (opt.message == null) {
        data.missing.push('message');
      }

      // --time | -t

      if (opt.time == null) {
        data.missing.push('time');
      } else {
        // @todo: validate format. must be int w/m or h suffix
      }

      // --date | -d

      if (opt.date == null) {
        var current = new Date();
        opt.date = freckle.date(current);
      } else {
        // @todo: validate format if date is given
      }

      // --user | -u

      if (opt.user == null) {

        // Load user from config.
        if (config.user !== null) {
          opt.user = config.user;
        }
        else {
          data.missing.push('user');
        }

      }

      if (data.missing.length == 0) {

        // If we have all of the params then create an entry

        freckle.entries.add({
          'entry': {
            'minutes': opt.time
          , 'user': opt.user
          , 'project_id': opt.project
          , 'description': opt.message
          , 'date': opt.date
          }
        }, function( err, data ) {
          console.log( err, data );
        });

        console.log("Logged " + opt.time + " for " + opt.project);
      } else {
        console.log("missing " + data.missing);
      }
    }
  }

};
run_pip();
