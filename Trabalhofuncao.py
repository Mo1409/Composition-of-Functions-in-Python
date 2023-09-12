def f(x):
  return x**2 + 5


def g(x):
  return 2 * x + 8


def compor(f, g, x):
  return f(g(x))


x = int(input("Escolha o valor de x: "))

funcao_GoF = compor(f, g, x)

funcao_GoG = compor(g, g, x)

funcao_FoF = compor(f, f, x)

funcao_FoG = compor(f, g, x)

print("(g * f)(x) =", funcao_GoF)
print("(g * gx) =", funcao_GoG)

print("(f * f)(x)", funcao_FoF)

print("(f º g)(x) =", funcao_FoG)
