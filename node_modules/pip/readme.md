# Pip
_'Cuz Pippi has freckles._

Basic command line tool for logging hours in [let's freckle](http://letsfreckle.com). Uses the excellent [freckle api bindings](https://github.com/tbranyen/nodefreckle) from the Node.js library created by Tim Branyan [@tbranyen](http://twitter.com/tbranyen).

## Setup
Create a ~/.freckle file using the config.json file as a template. Modify each variable to your specific information.

## Use
```
Usage: pip [command] [options]

[Commands]
list            List projects associated with your subdomain. This will give you a list of project names and their IDs which you need for logging your entries.
                  ex: pip list

log             Log time entries using various options.
                  ex: pip log -p 101814 -m "quick update" -t 15m

[Options]
-h, --help      Display this help page.
                  ex: pip -h

-t, --time      Time entry in freckle specified format.
                  ex: pip -t 15m
                  ex: pip -t 1.5h

-p, --project   The project ID.
                  ex: pip -p 101814

-m, --message   Post a message to yammer
                  ex: pip -m "I'm working on pip"
                  ex: pip -m "tag, tag, tag"

-d, --date      Optional date formated in YYYY-MM-DD. Defaults to today.
                  ex: pip -d 2012-07-20

-u, --user      Optional user to log time for. Defaults to user in config.json.
                  ex: pip -u apitest@letsfreckle.com
```

## Todo
* I'd like to have tab completion for project names and tags.
