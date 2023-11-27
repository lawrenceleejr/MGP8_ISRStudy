import re

str = "asdf/string1000GeV.root"
match = re.search(r'(\d+)GeV', str).group(1)
print(match)