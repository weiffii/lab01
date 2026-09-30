from .errors import CalculatorError


def validate(tokens: list) -> bool:
    """Проверка корректности выражения"""
    if not tokens:
        raise CalculatorError("Пустое выражение")
    if not validate_brackets(tokens):
        raise CalculatorError("Неправильно расставлены скобки")
    except_operand = True
    flag = 0
    for token in tokens:
        if len(token)>1 and token[0]=='0' and token[1]!='.':
                raise CalculatorError("Незначащий ноль")
        if except_operand:
            if is_number(token):
                if token.count('.')>1:
                    return False
                except_operand = False
                flag = 0
            elif token in ['+','-'] and flag == 0:
                except_operand = True
                flag = 1
            elif token == '(':
                except_operand = True
            else:
                return False
        else:
            if token in ['+','-','*','/','%','//']:
                except_operand = True
            elif token == ')':
                except_operand = False
            else:
                return False

    if not except_operand:
        return True
    else:
        return False


def validate_brackets(exp: list) -> bool:
    """Проверка на правильное расположение скобок в выражении"""
    count = 0
    count_numbers = 0
    for i in exp:
        if i == '(':
            count+=1
        elif i == ')':
            count -=1
            if count<0:
                return False
            if count_numbers==0:
                return False
        elif is_number(i):
            count_numbers += 1
    return count==0

def is_number(a: str) -> bool:
    """Проверка, является ли строка числом"""
    try:
        float(a)
        return True
    except (ValueError, TypeError):
        return False

