def validate_if_else(s):
  return "if" in s and "else" in s

def check(input, validate):
  print(f"Input: {input}")

  if validate(input):
    print("Entrada válida.\n")
  else:
    print("Entrada inválida.\n")

valid_input = "if x > 0: pass else: pass"
invalid_input = "if x > 0: pass"

check(valid_input, validate_if_else)
check(invalid_input, validate_if_else)