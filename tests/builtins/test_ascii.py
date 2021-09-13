from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class AsciiTests(TranspileTestCase):
    def test_ascii_tuple(self):
        self.assertCodeExecution("""
            print(ascii(()))
            print(ascii((1,)))
            print(ascii((1,2,3)))
            print(ascii(("abc123")))
            print(ascii(("åäö\\n\\t")))
            print(ascii(("'")))
            print(ascii(("\\\\")))
            print(ascii(("\\"")))
            print(ascii(("'\\"")))
            print(ascii(("\\x04")))
            print(ascii(("\\x80")))
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
            print(ascii(slice("abc","åäö","\\x04\\x80")))
            print(ascii(slice("abc", "\\n\\r\\t", "\\u1337/ascii")))
            print(ascii(slice("' \\\\","\\"","'\\"")))
            """)

    def test_ascii_list(self):
        self.assertCodeExecution("""
            print(ascii([]))
            print(ascii([1]))
            print(ascii([1, "abc123", 2]))
            print(ascii([1, "\\n\\t\\r åäö", 2]))
            print(ascii(["\\x04"]))
            print(ascii(["'", "\\\\", "\\"", "'\\""]))
            """)

    # Still figuring out these
    # def test_ascii_set(self):
    #     self.assertCodeExecution("""
    #         print(ascii(set([])))
    #         print(ascii(set([1])))
    #         print(ascii(set([1, "abc123", 2])))
    #         print(ascii(set([1, "\\n\\t\\r åäö", 2])))
    #         print(ascii(set(["\\x04"])))
    #         print(ascii(set(["'", "\\\\", "\\"", "'\\""])))
    #         """)

    # def test_ascii_frozenset(self):
    #     self.assertCodeExecution("""
    #         print(ascii(frozenset([])))
    #         print(ascii(frozenset([1])))
    #         print(ascii(frozenset([1, "abc123", 2])))
    #         print(ascii(frozenset([1, "\\n\\t\\r åäö", 2])))
    #         print(ascii(frozenset(["\\x04"])))
    #         print(ascii(frozenset(["'", "\\\\", "\\"", "'\\""])))
    #         """)

    # def test_ascii_dict(self):
    #     self.assertCodeExecution("""
    #         print(ascii({}))
    #         print(ascii({"abc":123}))
    #         print(ascii({"åäö":"\\n\\t\\r"}))
    #         print(ascii({"\\x04":"\\x80"}))
    #         print(ascii({"'":"\\\\", "\\"":"'\\""}))
    #         """)

class BuiltinAsciiFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["ascii"]

    not_implemented = [
        'test_class',
        'test_complex',
    ]
