from toolkit.calculator import calculator
from toolkit.converter import converter
from toolkit.errors import CalculatorError, ConverterError

import typer
app = typer.Typer()

@app.command(context_settings={"ignore_unknown_options": True})
def calc(expression: str = typer.Argument(default="",help = "Арифметическое выражение")) -> None:
    """Запуск калькулятора через CLI"""
    try:
        print(calculator(expression))
    except CalculatorError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)

@app.command(context_settings={"ignore_unknown_options": True})
def convert(value: float = typer.Argument(default=None,help = "Значение конвертируемой единицы измерения"),
            from_unit: str = typer.Option(None, "--from", help="Единица измерения,из которой конвертируем"),
            to_unit: str = typer.Option(None,"--to", help="Единица измерения, в которую конвертируем"),) -> None:
    """Запуск конвертера через CLI"""
    try:
        print(converter(value,from_unit,to_unit))
    except ConverterError as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(code=2)



if __name__ == "__main__":
    app()



