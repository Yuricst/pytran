# pytran
Python helpers for fortran


### Generating template fortran module

For generating a template fortran module, run

```bash
python template.py
```

or specify module name as 

```bash
python template.py mymod
```

For more options, call the function from python repl:

```python
from template import template_module
template_module(module="template", extension="f90", temp_function=True, temp_subroutine=True)
```
