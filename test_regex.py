import re
s = "🇲🇽 TODO LISTO: @FILGuadalajara La feria de ferias del libro en 🇲🇽 y el VISITA el stand"

expression = re.compile(u'[\U0001F1E6-\U0001F1FF]')
print(re.sub(expression, "", s))
