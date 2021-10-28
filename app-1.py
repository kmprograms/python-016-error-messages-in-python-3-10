# Jak Python od wersji 3.10 informuje nas o błędach?

# Jedną z nowości Python 3.10 jest jeszcze lepsza czytelność komunikatów o błędach,
# które spotykają nas podczas rozwijania aplikacji.

# Bardzo duzy postęp w poprawie czytelności wystąpił w przypadku błędów typu
# SyntaxError czyli takich, które występują, kiedy kod jest parsowany jeszcze
# zanim zostanie uruchomiony.
# Starsze wersje języka często dostarczały komunikaty, z których nie wynikało
# jednoznacznie, co jest powodem błędu. Python w wersji 3.10 poprawia ten mechanizm.

# ---------------------------------------------------------------------------------
# Przykład 1
# ---------------------------------------------------------------------------------
# Uruchom skrypt z poniższym kodem:
# >> python app-1.py

# print('Message)

# W Python 3.10 dostaniesz komunikat:
# --> SyntaxError: unterminated string literal
# We wcześniejszych wersjach Python w takiej sytuacji otrzymamy komunikat:
# --> SyntaxError: EOL while scanning string literal

# ---------------------------------------------------------------------------------
# Przykład 2
# ---------------------------------------------------------------------------------
# Uruchom skrypt z poniższym kodem:
# >> python app-1.py

# hobbies = {
#     'Adam': 'Sport',
#     'Ewa': 'Books',
#     'Jan': 'Music'
#
#
# print(f'{hobbies["Adam"]}')

# W Python 3.10 dostaniesz komunikat:
# --> SyntaxError: '{' was never closed
# We wcześniejszych wersjach Python w takiej sytuacji otrzymamy komunikat:
# --> SyntaxError: invalid syntax


# ---------------------------------------------------------------------------------
# Przykład 3
# ---------------------------------------------------------------------------------
# Uruchom skrypt z poniższym kodem:
# >> python app-1.py

# hobbies = {
#     'Adam': 'Sport',
#     'Ewa': 'Books',
#     'Jan': 'Music'
# }
#
# if hobbies['Adam'] = 'Sport':
#     pass

# W Python 3.10 dostaniesz komunikat:
# --> SyntaxError: cannot assign to subscript here. Maybe you meant '==' instead of '='?
# W dodatku za pomocą ^ dostajesz kompleksowo podkreslenie miejsca,
# w którym jest błąd.
# We wcześniejszych wersjach Python w takiej sytuacji otrzymamy komunikat:
# --> SyntaxError: invalid syntax


# Czytelność zwiększono również w przypadku odwołań do nieprawidłowych
# atrybutów i nazw
# ---------------------------------------------------------------------------------
# Przykład 4
# ---------------------------------------------------------------------------------
# Uruchom skrypt z poniższym kodem:
# >> python app-1.py

# Zasugeruje prawidlowe nazwy atrybutow i nazw
# Mechanizm podpowiadania działa zarówno dla nazw wbudowanych jak i tych,
# które samodzielnie dostarczymy.

# import sys
# print(sys.arg)  # AttributeError: module 'sys' has no attribute 'arg'. Did you mean: 'argv'?

user_age = 19
print(userage)  # NameError: name 'userage' is not defined. Did you mean: 'user_age'?