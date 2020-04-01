# Un nombre premier est un nombre divisible uniquement par 1 et par lui même
# Exemple 7 est premier, 7 est uniquement divisible par 1 et par 7
# Exemple 8 n'est pas premier, car il est divisible par 1, 8, 2, 4

# 7 est un nombre premier sur 3 bits cad < 2**3 = 8
# 7 est ma clé de cryptage
# Message = 5
# Algo de cryptage = *
# Mise en oeuvre du cryptage => 7 * 5 = 35 est mon message crypté
# Si vous connaissez la clé, vous connaissez l'algo de décryptage : /
# Décryptage 35 / 7 => 5
# Clé de cryptage ne peut être qu'un nombre premier
# Vous ne connaissez pas la clé => pirate
