# Installation

`pip install seao`

# Example

```py
from seao.Seao import Seao

USERNAME = ''
PASSWORD = ''
PDF_ID = 'a18c621b-9bce-49ee-8eeb-d43c924bc3df'

seao = Seao(USERNAME, PASSWORD)
pdf = seao.get_file(PDF_ID, decrypt=True)
with open('tmp.pdf', 'w+') as f:
    f.write(pdf)
seao.logout()
```
