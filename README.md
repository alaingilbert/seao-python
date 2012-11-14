# Installation

`pip install seao`

# Example

```py
from seao.Seao import Seao

seao = Seao(USERNAME, PASSWORD)
pdf = seao.get_file(PDF_ID)
with open('tmp.pdf', 'w+') as f:
    f.write(pdf)
seao.logout()
```
