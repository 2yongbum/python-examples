import sys

def num(a):
  return float(a.replace(',', ''))

equation = ' '.join(sys.argv[1:])
equation2 = equation.replace(',', '')
unit = ''
try:
  if '%' in equation2:
    num1, num2 = map(float, equation2.split('%'))
    result = num1 * num2 / 100
    unit = '(%)'
  elif '~' in equation2:
    num1, num2 = map(float, equation2.split('~'))
    result = (num1 - num2) * 100 / num1
    unit = '(%)'
  elif '$' in equation2:
    num1, num2 = map(float, equation2.split('$'))
    result = num1+num1*num2/100
  else:
    result = eval(equation2)
  
except Exception as e:
  print("Error: Invalid equation. Please try again.")

rs = f'{result:,}'
if 'e-' in rs:
  rs = f'{result:.10f} ({result})'
print(equation, '=', rs, unit)
