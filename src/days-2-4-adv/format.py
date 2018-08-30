def print_format_string(color, message):
    colors = {
        'success': '\x1b[6;30;42m',
        'error': '\x1b[1;31;40m'
    }
    print(f'${colors[color]}{message}\x1b[0m')