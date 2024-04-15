from sympy.logic.boolalg import to_dnf, truth_table
from sympy.abc import x, y, z
from sympy import sympify


# Fonction principale
def main():
    print("Entrez l'expression booléenne en utilisant les opérateurs suivants :")
    print("- '&' pour l'opérateur ET")
    print("- '|' pour l'opérateur OU")
    print("- '~' pour l'opérateur NON")
    print("- Utilisez des parenthèses pour la priorité d'opération. Ex: (x & y) | (~x & z)")
    expression_str = input("Entrez l'expression booléenne : ")
    expression = sympify(expression_str, evaluate=False)
    table = truth_table(expression, [x, y, z])
    min_expression = to_dnf(expression)
    print("Forme minimale :")
    print(min_expression)

# Appel de la fonction principale
if __name__ == "__main__":
    main()

