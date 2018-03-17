"""tres formas de fazer..."""

pessoa1 = ["Ana", "60.5", "1.7"]
pessoa2 = ["Maria", "105.8", "1.5"]
pessoa3 = ["Braga", "80", "1.8"]

print(pessoa1)
print(pessoa2)
print(pessoa3)

print("a" , pessoa1[0] , "tem" , pessoa1[1] , "kg e" , pessoa1[2] , "de altura")
print("a" , pessoa2[0] , "tem" , pessoa2[1] , "kg e" , pessoa2[2] , "de altura")
print("a" , pessoa3[0] , "tem" , pessoa3[1] , "kg e" , pessoa3[2] , "de altura")

pessoas = [
["Ana", "60.5", "1.7"],
["Maria", "105.8", "1.5"],
["Braga", "80", "1.8"]
]

for percorre in pessoas:
    print("a" , percorre[0] , "tem" , percorre[1] , "kg, e" , percorre[2] , "de altura")
