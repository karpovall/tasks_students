"""
Simplified VM code which works for some cases.
You need extend/rewrite code to pass all cases.
"""

import builtins
import dis
import types
import typing as tp


class Frame:
    """
    Frame header in cpython with description
        https://github.com/python/cpython/blob/3.9/Include/frameobject.h#L17

    Text description of frame parameters
        https://docs.python.org/3/library/inspect.html?highlight=frame#types-and-members
    """

    def __init__(self,
                 frame_code: types.CodeType,
                 frame_builtins: dict[str, tp.Any],
                 frame_globals: dict[str, tp.Any],
                 frame_locals: dict[str, tp.Any]) -> None:
        self.code = frame_code
        self.builtins = frame_builtins
        self.globals = frame_globals
        self.locals = frame_locals
        self.data_stack: tp.Any = []
        self.bytecode_counter = 0
        self.last_exception = None
        self.return_value = None

    def top(self) -> tp.Any:
        return self.data_stack[-1]

    def peek(self, n):
        return self.data_stack[-n]

    def pop(self) -> tp.Any:
        return self.data_stack.pop()

    def push(self, *values: tp.Any) -> None:
        self.data_stack.extend(values)

    def popn(self, n: int) -> tp.Any:
        """
        Pop a number of values from the value stack.
        A list of n values is returned, the deepest value first.
        """
        if n > 0:
            returned = self.data_stack[-n:]
            self.data_stack[-n:] = []
            return returned
        else:
            return []

    def pop_top_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-POP_TOP

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1361
        """
        self.pop()

    def run(self) -> tp.Any:
        list_ = [instruction for instruction in dis.get_instructions(self.code)]
        while self.bytecode_counter < len(list_):
            getattr(self, list_[self.bytecode_counter].opname.lower() + "_op")(list_[self.bytecode_counter].argval)
            self.bytecode_counter += 1
        return self.return_value

    def call_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-CALL_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3496
        """
        arguments = self.popn(arg)
        f = self.pop()
        self.push(f(*arguments))

    def load_name_op(self, arg: str) -> None:
        """
        Partial realization

        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2416
        """

        if arg in self.locals:
            self.push(self.locals[arg])
        elif arg in self.globals:
            self.push(self.globals[arg])
        else:
            self.push(self.builtins[arg])

    def load_global_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_GLOBAL

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2480
        """
        if arg in self.builtins:
            self.push(self.builtins[arg])
        else:
            self.push(self.globals[arg])

    def load_const_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_CONST

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1346
        """
        self.push(arg)

    def load_fast_op(self, arg: tp.Any) -> None:
        try:
            a = self.locals[arg]
            self.push(a)
        except KeyError:
            self.return_value(self)

    def store_name_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-STORE_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2280
        """
        self.locals[arg] = self.pop()

    def store_fast_op(self, arg: str) -> None:
        self.locals[arg] = self.pop()

    def store_global_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-STORE_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2280
        """
        self.globals[arg] = self.pop()

    def delete_fast_op(self, arg: str) -> None:
        try:
            del self.locals[arg]
        except KeyError:
            self.bytecode_counter = 1000

    def delete_name_op(self, arg: str) -> None:
        del self.locals[arg]

    def delete_global_op(self, arg: str) -> None:
        del self.globals[arg]

    def return_value_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-RETURN_VALUE

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1911
        """
        self.return_value = self.pop()

    def make_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-MAKE_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3571

        Parse stack:
            https://github.com/python/cpython/blob/3.9/Objects/call.c#L671

        Call function in cpython:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L4950
        """
        name = self.pop()  # the qualified name of the function (at TOS)  # noqa
        code = self.pop()  # the code associated with the function (at TOS1)

        # TODO: use arg to parse function defaults

        def f(*args: tp.Any, **kwargs: tp.Any) -> tp.Any:
            # TODO: parse input arguments using code attributes such as co_argcount

            parsed_args: dict[str, tp.Any] = {}
            f_locals = dict(self.locals)
            f_locals.update(parsed_args)

            frame = Frame(code, self.builtins, self.globals, f_locals)  # Run code in prepared environment
            return frame.run()

        self.push(f)

    def for_iter_op(self, arg: int) -> None:
        tos = self.pop()
        try:
            const = tos.__next__()
            self.push(tos)
            self.push(const)
        except StopIteration:
            self.bytecode_counter = arg // 2 - 1

    def jump_absolute_op(self, arg: int) -> None:
        self.bytecode_counter = (arg // 2) - 1

    def jump_forward_op(self, arg: int) -> None:
        self.bytecode_counter += arg

    def pop_jump_if_true_op(self, arg: int) -> None:
        tos = self.pop()
        if tos:
            self.bytecode_counter = (arg // 2) - 1

    def pop_jump_if_false_op(self, arg: int) -> None:
        tos = self.pop()
        if not tos:
            self.bytecode_counter = (arg // 2) - 1

    def jump_if_true_or_pop_op(self, arg: int) -> None:
        tos = self.top()
        if not tos:
            self.pop()
        else:
            self.bytecode_counter = (arg // 2) - 1

    def jump_if_false_or_pop_op(self, arg: int) -> None:
        tos = self.top()
        if not tos:
            self.bytecode_counter = (arg // 2) - 1
        else:
            self.pop()

    def compare_op_op(self, arg: str) -> None:
        y = self.pop()
        x = self.pop()
        if arg == '<':
            self.push(x < y)
        elif arg == '<=':
            self.push(x <= y)
        elif arg == '==':
            self.push(x == y)
        elif arg == '!=':
            self.push(x != y)
        elif arg == '>':
            self.push(x > y)
        elif arg == '>=':
            self.push(x >= y)

    def inplace_add_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const += const1
        self.push(const)

    def inplace_subtract_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 - const
        self.push(const)

    def inplace_power_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 ** const
        self.push(const)

    def inplace_multiply_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const *= const1
        self.push(const)

    def inplace_floor_divide_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 // const
        self.push(const)

    def inplace_true_divide_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 / const
        self.push(const)

    def inplace_modulo_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 % const
        self.push(const)

    def inplace_and_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const &= const1
        self.push(const)

    def inplace_lshift_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 << const
        self.push(const)

    def inplace_rshift_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 >> const
        self.push(const)

    def inplace_xor_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const ^= const1
        self.push(const)

    def inplace_or_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const |= const1
        self.push(const)

    def unary_positive_op(self, arg: str) -> None:
        const = self.pop()
        self.push(+const)

    def unary_negative_op(self, arg: str) -> None:
        const = self.pop()
        self.push(-const)

    def unary_not_op(self, arg: str) -> None:
        const = self.pop()
        self.push(not const)

    def unary_invert_op(self, arg: str) -> None:
        const = self.pop()
        self.push(~ const)

    def get_iter_op(self, arg: str) -> None:
        const = self.pop()
        self.push(iter(const))

    def binary_add_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 + const
        self.push(const)

    def binary_subtract_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 - const
        self.push(const)

    def binary_power_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 ** const
        self.push(const)

    def binary_multiply_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 * const
        self.push(const)

    def binary_floor_divide_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 // const
        self.push(const)

    def binary_true_divide_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 / const
        self.push(const)

    def binary_modulo_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 % const
        self.push(const)

    def binary_and_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 & const
        self.push(const)

    def binary_lshift_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 << const
        self.push(const)

    def binary_rshift_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 >> const
        self.push(const)

    def binary_xor_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 ^ const
        self.push(const)

    def binary_or_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const = const1 | const
        self.push(const)

    def binary_subscr_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        self.push(const1[const])

    def store_subscr_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        const2 = self.pop()
        const1[const] = const2

    def delete_subscr_op(self, arg: str) -> None:
        const = self.pop()
        const1 = self.pop()
        del const1[const]

    def contains_op_op(self, args: str) -> None:
        tos = self.pop()
        tos1 = self.pop()
        a = tos1 in tos
        self.push(a)

    def is_op_op(self, args: str) -> None:
        tos = self.pop()
        tos1 = self.pop()
        a = tos is tos1
        self.push(a)

    def load_assertion_error_op(self, arg: str) -> None:
        self.push(AssertionError)

    def raise_varargs_op(self, arg: int) -> None:
        ex = val = tb = None
        if arg == 0:
            ex, val, tb = self.last_exception
        elif arg == 1:
            ex = self.pop()
        elif arg == 2:
            val = self.pop()
            ex = self.pop()
        elif arg == 3:
            tb = self.pop()
            val = self.pop()
            ex = self.pop()

    def build_tuple_op(self, arg: int) -> None:
        el = self.popn(arg)
        self.push(tuple(el))

    def build_list_op(self, arg: int) -> None:
        el = self.popn(arg)
        self.push(el)

    def build_set_op(self, arg: int) -> None:
        el = self.popn(arg)
        self.push(set(el))

    def build_map_op(self, arg: int) -> None:
        self.push({})

    def list_to_tuple_op(self, arg: str) -> None:
        tos = self.pop()
        self.push(tuple(tos))

    def store_map_op(self):
        the_map, val, key = self.popn(3)
        the_map[key] = val
        self.push(the_map)

    def build_const_key_map_op(self, arg: int) -> None:
        tos = self.pop()
        el = self.popn(arg)
        dict_ = {}
        for i in range(len(tos)):
            dict_[tos[i]] = el[i]
        self.push(dict_)

    def unpack_sequence_op(self, arg: int) -> None:
        seq = self.pop()
        for x in reversed(seq):
            self.push(x)

    def build_slice_op(self, arg: int) -> None:
        if arg == 2:
            x, y = self.popn(2)
            self.push(slice(x, y))
        elif arg == 3:
            x, y, z = self.popn(3)
            self.push(slice(x, y, z))

    def list_append_op(self, arg: int) -> None:
        val = self.pop()
        the_list = self.peek(arg)
        the_list.append(val)

    def list_extend_op(self, arg: int) -> None:
        val = self.pop()
        the_list = self.peek(arg)
        the_list.extend(val)

    def set_add_op(self, arg: int) -> None:
        val = self.pop()
        the_set = self.peek(arg)
        the_set.add(val)

    def set_update_op(self, arg: int) -> None:
        val = self.pop()
        the_set = self.peek(arg)
        the_set.update(val)

    def map_add_op(self, arg: int) -> None:
        val, key = self.popn(2)
        the_map = self.peek(arg)
        the_map[key] = val

    def import_name_op(self, name) -> None:
        level, fromlist = self.popn(2)
        self.push(
            __import__(name, self.globals, self.locals, fromlist, level)
        )

    def import_from_op(self, name) -> None:
        mod = self.top()
        self.push(getattr(mod, name))

    def import_star_op(self, name) -> None:
        mod = self.pop()
        for attr in dir(mod):
            if attr[0] != '_':
                self.locals[attr] = getattr(mod, attr)

    def load_build_class_op(self, arg: str) -> None:
        self.push(builtins.__build_class__)

    def store_locals_op(self) -> None:
        self.locals = self.pop()

    def load_attr_op(self, arg: str) -> None:
        obj = self.pop()
        val = getattr(obj, arg)
        self.push(val)

    def store_attr_op(self, arg: str) -> None:
        val, obj = self.popn(2)
        setattr(obj, arg, val)

    def delete_attr_op(self, arg) -> None:
        obj = self.pop()
        delattr(obj, arg)


class VirtualMachine:
    def run(self, code_obj: types.CodeType) -> None:
        """
        :param code_obj: code for interpreting
        """
        globals_context: dict[str, tp.Any] = {}
        frame = Frame(code_obj, builtins.globals()['__builtins__'], globals_context, globals_context)
        return frame.run()
