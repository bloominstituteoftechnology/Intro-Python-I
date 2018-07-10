/**
 * Module dependencies.
 */
var fs = require('fs')
    , noop = function(){}
    , utils = require('./utils')
    , path = require('path')
    , PATH_CONFIG = path.join(__dirname,'../config.json');

exports.path = PATH_CONFIG;

/**
 * Expose constructor.
 */
module.exports = Config;

/**
 * Initialize a new `Config`.
 *
 * @param {Object} conf
 * @api public
 */
function Config() {
    var core_config_exists = true
    , override = false
    , config
    , keys;

    // handle core config
    utils.file_exists(false, PATH_CONFIG, function(success, file, err){
        if (success) config = file;
        else core_config_exists = false;
    });

    // handle override
    utils.file_exists(false, process.env.HOME + '/.freckle', function(success, file, err){
        if (success) {
            config = file;
            override = true;
        } else {
            keys = JSON.parse(fs.readFileSync(PATH_CONFIG, "utf8"));
        }
    });

    // token
    this.token =
        (core_config_exists) ? config.token :
        this.token || "";

    // subdomain
    this.subdomain =
        (core_config_exists) ? config.subdomain :
        this.subdomain || "";

    // user
    this.user =
        (core_config_exists) ? config.user :
        this.subdomain || "";

    this.override_status = (override) ? '\n[ Using override config at ~/.freckle ]' : '\n[ Using default keys config at ' + PATH_CONFIG + ' - to override see Readme ]';
    this.path = PATH_CONFIG;
};

/**
 * Load data.
 *
 * @param {Function} fn
 * @api public
 */
Config.prototype.load = function(fn){
  var self = this
    , fn = fn || noop;
  fs.readFile(PATH_CONFIG, 'utf8', function(err, json){
    if (err) return fn(err);
    var data = JSON.parse(json)
      , keys = Object.keys(data)
      , len = keys.length;
    for (var i = 0; i < len; ++i) {
      self[keys[i]] = data[keys[i]];
    }
    fn();
  });
  return this;
};
