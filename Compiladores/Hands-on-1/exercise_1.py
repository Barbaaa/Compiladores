def validate_alpha(s):
  return s.isalpha()

def check(input, validate):
  print(f"Input: {input}")

  if validate(input):
    print("Entrada válida.\n")
  else:
    print("Entrada inválida.\n")

valid_input = "HelloWorld"
invalid_input = "H3ll0W0r1d"

check(valid_input, validate_alpha)
check(invalid_input, validate_alpha)