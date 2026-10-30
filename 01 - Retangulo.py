import math

area = float
perimetro = float
diagonal = float

Base = float(input("Base do Retangulo: "))
Altura = float(input("Altura do Retangulo: "))

area = Base * Altura
perimetro = 2 * (Base + Altura)
diagonal = math.sqrt(Base * Base + Altura * Altura)

print()
print(f"Area {area:.4f}")
print(f"Perimetro {perimetro:.4f}")
print(f"Diagonal {diagonal:.4f}")