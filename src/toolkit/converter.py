from .errors import ConverterError
from.history import add_history
from decimal import Decimal, ROUND_HALF_UP
from .config import load_config
MASS = load_config()["MASS"]
LENGTH  = load_config()["LENGTH"]

def converter(value: float, from_unit: str, to_unit: str) -> float:
    """Конвертация"""
    if value is None or from_unit is None or to_unit is None:
        raise ConverterError("Пустое выражение")
    value = Decimal(value)
    to_unit = to_unit.lower()
    from_unit = from_unit.lower()
    if to_unit in LENGTH and from_unit in LENGTH:
        result = value*Decimal(LENGTH[from_unit])/Decimal(LENGTH[to_unit])
        result = result.quantize(Decimal("0.000000000000001"), rounding=ROUND_HALF_UP)
        add_history("converter", expression = f"{value} -- from {from_unit} -- to {to_unit}", result = float(result))
        return float(result)
    elif to_unit in MASS and from_unit in MASS:
        result = value*Decimal(MASS[from_unit])/Decimal(MASS[to_unit])
        result = result.quantize(Decimal("0.000000000000001"), rounding=ROUND_HALF_UP)
        add_history("converter", expression=f"{value} -- from {from_unit} -- to {to_unit}", result=float(result))
        return float(result)
    elif to_unit in ['c','f','k'] and from_unit in ['c','f','k']:
        result = temperature(value,from_unit,to_unit)
        result = result.quantize(Decimal("0.000000000000001"), rounding=ROUND_HALF_UP)
        add_history("converter", expression=f"{value} -- from {from_unit} -- to {to_unit}", result=float(result))
        return float(result)
    raise ConverterError(f"Невозможно конвертировать из {from_unit} в {to_unit}")



def temperature(value:Decimal,from_unit: str,to_unit: str) -> Decimal:
    """Конвертация температуры"""
    if from_unit == 'c':
        c = value
    elif from_unit == 'f':
        c = (value - 32)*5/9
    elif from_unit == 'k':
        c = value - Decimal(273.15)
    else:
        raise ConverterError("Запрос введен некорректно")
    if c>=-273.15:
        if to_unit == 'c':
            return c
        elif to_unit == 'f':
            return c*9/5 + 32
        elif to_unit == 'k':
            return c + Decimal(273.15)
        else:
            raise ConverterError("Запрос введен некорректно")
    else:
        raise ConverterError("Температура ниже абсолютного нуля")
