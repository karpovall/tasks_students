import dis
import types


def code_(code: types.CodeType, list_: list[str]) -> list[str]:
    instructions = dis.get_instructions(code)
    for instruction in instructions:
        list_.append(instruction.opname)
        if instruction.opname == 'LOAD_CONST':
            const_value = instruction.argval
            if isinstance(const_value, types.CodeType):
                code_(const_value, list_)
    return list_


def count_operations(source_code: types.CodeType) -> dict[str, int]:
    """Count byte code operations in given source code.

    :param source_code: the bytecode operation names to be extracted from
    :return: operation counts
    """
    dict_ = {}
    list_: list[str] = []
    a = code_(source_code, list_)
    for i in range(len(a)):
        dict_[a[i]] = a.count(a[i])
    return dict_
