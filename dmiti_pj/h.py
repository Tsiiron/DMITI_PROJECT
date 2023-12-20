import sys

type_errors = [] # типы ошибок
errors = [] # сами ошибки

try:
    pass
except Exception: # крч вылавливает все ошибки, там уже делай че хочешь
    type_errors.append(sys.exc_info()[1].__class__.__name__)
    errors.append(str(sys.exc_info()[1]))



