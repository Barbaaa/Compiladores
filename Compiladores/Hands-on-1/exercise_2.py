def validate_real(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def check(input, validate):
  print(f"Input: {input}")

  if validate(input):
    print("Entrada válida.\n")
  else:
    print("Entrada inválida.\n")

valid_input = "-123.456"
invalid_input = "+123,456.0"

check(valid_input, validate_real)
check(invalid_input, validate_real)