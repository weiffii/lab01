import pytest
from toolkit.converter import converter
from toolkit.errors import ConverterError

def test_length_small_to_big():
    """Тест на перевод из маньшей длины в большую"""
    res = converter(100,"mm","cm")
    assert res == 10

def test_length_big_to_small():
    """Тест на перевод из большей длины в меньшую"""
    res = converter(1, "km", "mm")
    assert res == 1000000

def test_length_same():
    """Тест на перевод из одной метрики в ту же"""
    res = converter(1, "km", "km")
    assert res == 1

def test_mass_small_to_big():
    """Тест на перевод из меньшей массы в большую"""
    res = converter(1000, "g", "kg")
    assert res == 1

def test_mass_big_to_small():
    """Тест на перевод из большей массы в меньшую"""
    res = converter(2, "kg", "g")
    assert res == 2000

def test_mass_same():
    """Тест на перевод из одной метрики в ту же"""
    res = converter(1, "kg", "kg")
    assert res == 1

def test_temperature_f_to_c():
    """Тест на перевод из форенгейт в цельсии"""
    res = converter(32, "f", "c")
    assert res == 0

def test_temperature_k_to_c():
    """Тест на перевод из кельвин в цельсии"""
    res = converter(273.15, "k", "c")
    assert res == 0

def test_temperature_c_to_c():
    """Тест на перевод из одной метрики в ту же"""
    res = converter(32, "c", "c")
    assert res == 32

def test_temperature_c_to_k():
    """Тест на перевод из одной метрики в ту же"""
    res = converter(0, "c", "k")
    assert res == 273.15

def test_decimal():
    """Тест на ввод дробного числа"""
    res = converter(1.5, "m", "cm")
    assert res == 150

def test_register():
    """Тест на о, что регистр единиц измерения не учитывается"""
    res = converter(1.5, "m", "CM")
    assert res == 150

def test_unknown_unit():
    with pytest.raises(ConverterError):
        converter(10,"ab","m")

def test_incommpatible_units():
    with pytest.raises(ConverterError):
        converter(10,"kg","m")

def test_temperature_below_absolute_zero():
    with pytest.raises(ConverterError):
        converter(-300,"c","k")



