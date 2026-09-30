from .errors import CalculatorError
from .config import load_config
from .tokenization import tokenize
from .validation import validate
from decimal import Decimal, ROUND_HALF_UP
from .history import add_history
SIGNS = load_config()["SIGNS"]

def is_number(a: str) -> bool:
    """Проверяет, является ли строка числом"""
    try:
        float(a)
        return True
    except (ValueError, TypeError):
        return False



def polish(exp: list) -> list:
    """Преобразование выражения в польскую запись"""
    exp.append(")")
    stek = ['(']
    flag = 1
    bin_sign = ''
    polish_notation= []
    for i in exp:
        if is_number(i):
            if bin_sign !='':
                polish_notation.append(Decimal(bin_sign+i))
                bin_sign = ''
            else:
                polish_notation.append(Decimal(i))
                flag = 0
        elif i in ['+','-','/','*','(',')','%','//']:
            if i == ')':
                while stek[-1]!='(':
                    sign = stek.pop()
                    polish_notation.append(sign)
                stek.pop()
            elif i in ['+','-'] and flag == 1:
                bin_sign = i
                flag = 0
            elif i in ['+','-','*','/','%','//']:
                flag = 1
                while SIGNS[stek[-1]]>=SIGNS[i]:
                    polish_notation.append(stek.pop())
                stek.append(i)
            else:
                flag = 1
                stek.append(i)
        else:
            raise CalculatorError("Выражение введено неправильно")
    return polish_notation



def calculator(exp: str) -> float:
    """Вычисление выражения по польской записи"""
    tokens = tokenize(exp)
    if validate(tokens):
        notation = polish(tokens)
        stek = []
        for i in notation:
            if is_number(i):
                stek.append(i)
            elif i in ['+','-','*','/','%','//']:
                b = stek.pop()
                a = stek.pop()
                if i == '+':
                    stek.append(a+b)
                elif i == '-':
                    stek.append(a-b)
                elif i == '*':
                    stek.append(a*b)
                elif i == '/':
                    if b==0:
                        raise CalculatorError("Деление на 0")
                    else:
                        stek.append(a/b)
                elif i == '%':
                    if b==0:
                        raise CalculatorError("Деление на 0")
                    else:
                        stek.append(abs(a)%abs(b))
                elif i == '//':
                    if b==0:
                        raise CalculatorError("Деление на 0")
                    else:
                        stek.append(Decimal(int(a//b)))
                else:
                    raise CalculatorError("Выражение введено неправильно")
            else:
                raise CalculatorError("Выражение введено неправильно")
        result = stek.pop()
        result = Decimal(str(result))
        result = result.quantize(Decimal("0.000000000000001"), rounding=ROUND_HALF_UP)
        add_history("calculator",exp, float(result))
        return float(result)
    else:
        raise CalculatorError("Введено некорректное выражение")




