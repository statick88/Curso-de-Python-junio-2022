from camelcase import CamelCase

camel = CamelCase()
string = "Hola esto es un texto para CamelCase"
camelCase = camel.hump(string)
print(camelCase)