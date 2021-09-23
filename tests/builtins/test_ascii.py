from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AsciiTests(TranspileTestCase):
    def test_ascii_tuple(self):
        self.assertCodeExecution("""
            print(ascii(()))
            print(ascii((1,)))
            print(ascii((1,2,3)))
            print(ascii("abcåäö\\n\\t"))
            print(ascii(("\\x04")))
            """)

    def test_ascii_str(self):
        self.assertCodeExecution("""
            print(ascii(""))
            print(ascii("abc123"))
            print(ascii("\\n\\t\\r åäö"))
            print(ascii("'"))
            print(ascii("\\\\"))
            print(ascii("\\""))
            print(ascii("'\\""))
            print(ascii("\\x04"))
            print(ascii("\\x80"))
            print(ascii("\\u1337"))
            """)

    def test_ascii_bytes(self):
        self.assertCodeExecution("""
            print(ascii(b""))
            print(ascii(b"abc123"))
            print(ascii(b"\\n\\t\\r"))
            print(ascii(b"'"))
            print(ascii(b"\\\\"))
            print(ascii(b"\\""))
            print(ascii(b"'\\""))
            print(ascii(b"\\x04"))
            print(ascii(b"\\x80"))
            """)

    def test_ascii_slice(self):
        self.assertCodeExecution("""
            print(ascii(slice(1,2,1)))
            print(ascii(slice("\\x01", "\\n\\r\\t", "\\u1337/ascii")))
            """)

    def test_ascii_list(self):
        self.assertCodeExecution("""
            print(ascii([]))
            print(ascii([1]))
            print(ascii([1, "abc123", 2]))
            print(ascii([1, "\\n\\t\\r åäö", 2]))
            print(ascii(["\\x04"]))
            """)


class BuiltinAsciiFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["ascii"]

    not_implemented = [
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_set',
        'test_obj',
    ]
