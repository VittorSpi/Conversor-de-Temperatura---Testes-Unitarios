# Conversor de Temperaturas

Pequena aplicação em Python para conversão entre Celsius, Fahrenheit e Kelvin, com validação de limites físicos (zero absoluto) e testes unitários usando Pytest.

---

## Funcionalidades

- Conversão de Celsius para Fahrenheit e Kelvin  
- Conversão de Fahrenheit para Celsius e Kelvin  
- Conversão de Kelvin para Celsius e Fahrenheit  
- Validação de temperaturas abaixo do zero absoluto, lançando exceção caso ocorra

---


## Regras de Negócio Testadas

1. **Limites físicos da temperatura:**  
   - Celsius ≥ -273.15  
   - Fahrenheit ≥ -459.67  
   - Kelvin ≥ 0  

2. **Conversão correta entre unidades:**  
   - Celsius → Fahrenheit e Kelvin  
   - Fahrenheit → Celsius e Kelvin  
   - Kelvin → Celsius e Fahrenheit  

3. **Exceções:**  
   - Lançamento de `ValueError` caso algum valor informado esteja abaixo do zero absoluto.
