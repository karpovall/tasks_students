import math
import sys

from typing import Any, Optional

PROMPT = '>>> '


def run_calc(context: Optional[dict[str, Any]] = None) -> None:
    """Run interactive calculator session in specified namespace"""

    sys.stdout.write(PROMPT)
    sys.stdout.flush()
    st = sys.stdin.readline()
    new_context = {}
    if context is not None:
        new_context = context.copy()
    if '__builtins__' not in new_context:
        new_context['__builtins__'] = {}
    if st != "":
        while st != "":
            sys.stdout.write(str(eval(st, new_context)) + '\n')
            sys.stdout.flush()
            sys.stdout.write(PROMPT)
            sys.stdout.flush()
            st = sys.stdin.readline()
        sys.stdout.write('\n')
        sys.stdout.flush()



if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)






