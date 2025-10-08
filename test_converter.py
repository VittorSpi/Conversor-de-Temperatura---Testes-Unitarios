import pytest
from converter_temperate import ConverterTemperatura

converter_temp = ConverterTemperatura()

def test_celsius_para_fahrenheit():
    assert converter_temp.celsius_para_fahrenheit(0) == 32
    assert converter_temp.celsius_para_fahrenheit(100) == 212
    assert converter_temp.celsius_para_fahrenheit(-40) == -40

def test_celsius_para_kelvin():
    assert converter_temp.celsius_para_kelvin(0) == 273.15
    assert converter_temp.celsius_para_kelvin(100) == 373.15
    assert converter_temp.celsius_para_kelvin(-273.15) == 0 

def test_fahrenheit_para_celsius():
    assert converter_temp.fahrenheit_para_celsius(32) == 0
    assert converter_temp.fahrenheit_para_celsius(212) == 100
    assert converter_temp.fahrenheit_para_celsius(-40) == -40 

def test_fahrenheit_para_kelvin():
    assert converter_temp.fahrenheit_para_kelvin(32) == 273.15
    assert converter_temp.fahrenheit_para_kelvin(212) == 373.15
    assert converter_temp.fahrenheit_para_kelvin(-459.67) == 0

def test_kelvin_para_celsius():
    assert converter_temp.kelvin_para_celsius(273.15) == 0
    assert converter_temp.kelvin_para_celsius(373.15) == 100
    assert converter_temp.kelvin_para_celsius(0) == -273.15     

def test_kelvin_para_fahrenheit():
    assert converter_temp.kelvin_para_fahrenheit(273.15) == 32
    assert converter_temp.kelvin_para_fahrenheit(373.15) == 212
    assert converter_temp.kelvin_para_fahrenheit(0) == -459.67
    #O teste test_kelvin_para_fahrenheit falha ao comparar -459.66999999999996 com -459.67 
    # devido a imprecisões inerentes de números de ponto flutuante no Python.
    #  O cálculo está correto, mas a representação do float não é exata.
