from tweet import Tweet


t1 = Tweet("Miren España ' Controlaremos la Sala Segunda desde detrás ' : el ' whatsapp ' de Cosidó justificando el pacto con el PSOE en el CGPJ")
t2 = Tweet("Això és el 155 judicial : ' Controlaremos la Sala Segunda desde detrás ' : el ' whatsapp ' de Cosidó justificando el pacto con el PSOE en el CGPJ via")

print("sentence 1")
print(t1.oov_words())

print("sentence 2")
print(t2.oov_words())
