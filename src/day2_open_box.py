import ctypes


def open_box(title, message, style=0):
    ctypes.windll.user32.MessageBoxW(0, message, title, style)


open_box('Selam',
         'Burada bir hata oluştu. İyisi mi siz bu kutuyu kapatın.', 0)

# Styles:
# 0 : OK
# 1 : OK | Cancel
# 2 : Abort | Retry | Ignore
# 3 : Yes | No | Cancel
# 4 : Yes | No
# 5 : Retry | No
# 6 : Cancel | Try Again | Continue
