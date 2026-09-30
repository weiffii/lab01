import pytest
from toolkit.calculator import calculator
from toolkit.errors import CalculatorError
def test_summary():
    """Тест на сумму"""
    res = calculator("2+3")
    assert res == 5

def test_multiplication():
    """Тест на умножение с приоритетом"""
    res = calculator("1+5*2")
    assert res == 11

def test_division():
    """Тест на деление"""
    res = calculator("6/4")
    assert res == 1.5

def test_unary_sign_beginning():
    """Тест на считывание унарного знака в начале"""
    res = calculator("-1+7")
    assert res == 6

def test_unary_minus_after_binary_sign():
    """Тест на считывание унарного знака после бинарного"""
    res = calculator("2+-3")
    assert res == -1

def test_unary_plus_after_binary_sign():
    """Тест на считывание унарного плюса после бинарного"""
    res = calculator("2++3")
    assert res == 5

def test_brackets():
    """Тест на считывание скобок"""
    res = calculator("2*(3+4)")
    assert res == 14

def test_whitespace():
    """Тест на учет пробелов между тоекнами"""
    res = calculator("2 + 3                         *4")
    assert res == 14

def test_inter_division():
    """Тест на деление нацело"""
    res = calculator("7//2")
    assert res == 3

def test_remainder_division():
    """Тест на остаток от деления"""
    res = calculator("6%5")
    assert res == 1

def test_negative_operands_inter_division():
    """Тест на отрицательные операнды для деления нацело"""
    res = calculator("-5//2")
    assert res == -2

def test_negative_operands_remainder_division():
    """Тест на отрицательные операнды для поиска остатка от деления"""
    res = calculator("-7%2")
    assert res == 1

def test_fraction_starts_point():
    """Тест на считывание дроби, начинающейся с ."""
    res = calculator(".5")
    assert res == 0.5

def test_two_decimals():
    """Тест на несколько дробных чисел"""
    res = calculator("1.5+2.4")
    assert res == 3.9

def test_decimals_multiplication():
    """Тест на дробные операнды при умножении"""
    res = calculator("1.5*4")
    assert res == 6

def test_negative_decimals():
    """Тест на считывание отрицательных дробных чисел"""
    res = calculator("-0.5+1")
    assert res == 0.5

def test_positive_decimals():
    """Тест на считывание унарного плюса перед дробным числом"""
    res = calculator("+.5+1")
    assert res == 1.5

def test_brackets_decimals():
    """Тест на считывание скобок с дробями"""
    res = calculator("(1.5+2.5)*2+(-2)")
    assert res == 6

def test_division_zero():
    """Ошибка при делении на ноль"""
    with pytest.raises(CalculatorError):
        calculator("5/0")

def test_division_zero_2():
    """Ошибка при делении нацело на ноль"""
    with pytest.raises(CalculatorError):
        calculator("5//0")

def test_division_zero_3():
    """Ошибка при поиске остатка от деления на ноль"""
    with pytest.raises(CalculatorError):
        calculator("5%0")

def test_empty_string():
    """Ошибка при вводе пустой строки"""
    with pytest.raises(CalculatorError):
        calculator("")

def test_two_binary_signs():
    """Ошибка при вводе двух бинарных знаков рядом"""
    with pytest.raises(CalculatorError):
        calculator("5*/0")

def test_unknown_sign():
    """Ошибка при вводе неизвестного символа"""
    with pytest.raises(CalculatorError):
        calculator("5$3")

def test_no_operand_after_sign():
    """Ошибка при отсутствии операнда после знака"""
    with pytest.raises(CalculatorError):
        calculator("5+")

def test_no_operand_before_binary_sign():
    """Ошибка при отсутствии операнда перед бинарным знаком"""
    with pytest.raises(CalculatorError):
        calculator("*3")

def test_wrong_brackets():
    """Ошибка при вводе неправильно расставленных скобок"""
    with pytest.raises(CalculatorError):
        calculator("(3+5")
def test_empty_brackets():
    """Ошибка при вводе пустых скобках"""
    with pytest.raises(CalculatorError):
        calculator("3+()*5")
def test_whitespace_number():
    """Ошибка при вводе пробела в числе"""
    with pytest.raises(CalculatorError):
        calculator("3+5 4")

def test_two_dots_nearby_in_decimal():
    """Ошибка при вводе нескольких точек рядом"""
    with pytest.raises(CalculatorError):
        calculator("5..6")

def test_two_dots_in_decimal():
    """Ошибка при вводе нескольких точек в одном числе"""
    with pytest.raises(CalculatorError):
        calculator("5.2.1")

def test_several_unary_signs():
    """Ошибка при вводе нескольких унарных знаков"""
    with pytest.raises(CalculatorError):
        calculator("5+++1")

def test_only_signs():
    """Ошибка при вводе строки только из знаков"""
    with pytest.raises(CalculatorError):
        calculator("+++")



