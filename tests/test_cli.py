from typer.testing import CliRunner
from toolkit.__main__ import app

runner = CliRunner()

def test_cli_calculator():
    res = runner.invoke(app, ['calc', '2+3'])
    assert res.exit_code == 0
    assert res.stdout.strip() == '5.0'

def test_cli_calculator_error():
    res = runner.invoke(app, ['calc', '5/0'])
    assert res.exit_code == 2
    assert "Деление на 0" in res.stderr

def test_cli_converter():
    res = runner.invoke(app, ['convert', '100', '--from', 'mm', '--to', 'cm'])
    assert res.exit_code == 0
    assert res.stdout.strip() == '10.0'

def test_cli_converter_error():
    res = runner.invoke(app, ['convert', '100','--from', 'abc', '--to', 'cm'])
    assert res.exit_code == 2
    assert "Невозможно конвертировать из abc в cm" in res.stderr

