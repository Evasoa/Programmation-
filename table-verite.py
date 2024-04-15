from itertools import product
from sympy import symbols, sympify

# Fonction pour évaluer une expression booléenne
def evaluer_expression(expression, valeurs):
    return expression.subs(valeurs)

# Affichage de la table de vérité
def table_verite(expression, variables):
    variable_names = [str(var) for var in variables]
    print("Table de vérité :")
    print(" ".join(variable_names + ["Résultat"]))
    for values in product([False, True], repeat=len(variable_names)):
        valeurs = dict(zip(variables, values))
        resultat = evaluer_expression(expression, valeurs)
        values_str = " ".join(str(int(v)) for v in values)
        resultat_str = "1" if resultat else "0"
        print(values_str, resultat_str)  # Afficher le résultat comme 0 ou 1

# Calcul des formes canoniques
def formes_canoniques(expression, variables):
    formes_true = []
    formes_false = []
    for values in product([False, True], repeat=len(variables)):
        valeurs = dict(zip(variables, values))
        resultat = evaluer_expression(expression, valeurs)
        terms = [f"{v}" if valeurs[v] else f"~{v}" for v in variables]
        forme = " AND ".join(terms)
        if resultat:
            formes_true.append(forme)
        else:
            formes_false.append(forme)
    print("\nPremière forme canonique :")
    print(" OR ".join(formes_true))
    print("\nDeuxième forme canonique :")
    print(" AND ".join(formes_false))  # Utiliser AND pour la deuxième forme canonique

# Fonction principale
def main():
    print("Entrez l'expression booléenne en utilisant les opérateurs suivants :")
    print("- '&' pour l'opérateur ET")
    print("- '|' pour l'opérateur OU")
    print("- '~' pour l'opérateur NON")
    print("- Utilisez des parenthèses pour la priorité d'opération. Ex: (x & y) | (~x & z)")
    expression_str = input("Entrez l'expression booléenne : ")
    variables = list(set(symbols(expression_str)))
    expression = sympify(expression_str, evaluate=False)
    table_verite(expression, variables)
    formes_canoniques(expression, variables)

# Appel de la fonction principale
if __name__ == "__main__":
    main()
