from .errors import CalculatorError

def tokenize(exp: str) -> list[str]:
    """Разделение выражения на токены"""
    tokens = []
    number = ''
    for i in range(len(exp)):
        char = exp[i]
        if char == ' ' and 0 < i < (len(exp)-1) and (exp[i-1].isdigit() or exp[i-1]=='.')  and (exp[i+1].isdigit() or exp[i+1]=='.'):
            raise CalculatorError("Пробел в числе")
        elif char == ' ':
            pass
        elif char.isdigit() or char == '.':
            number += char
        elif char in ['-','+','*','(',')','%']:
            if number != '':
                tokens.append(number)
                number = ''
            tokens.append(char)
        elif char == '/':
            if tokens and tokens[-1]=='/':
                tokens.pop()
                tokens.append('//')
            else:
                if number != '':
                    tokens.append(number)
                    number = ''
                tokens.append(char)

        else:
            raise CalculatorError("Неправильно введено выражение")
    if number != '':
        tokens.append(number)
    return tokens
