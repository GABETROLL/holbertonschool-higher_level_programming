import unittest
from models.base import Base


class TestBaseConstructor(unittest.TestCase):
    def test_no_parameters(self):
        b = Base()
        self.assertEqual(b.id, 1)

        b = Base()
        self.assertEqual(b.id, 2)

    def test_id(self):
        for test_id in range(-5, 6):
            b = Base(test_id)
            self.assertEqual(b.id, test_id)

    def test_more_parameters(self):
        with self.assertRaises(TypeError):
            # too many arguments
            b = Base(1, 2)


class TestToDictionary(unittest.TestCase):
    def correct_arguments(self):
        b = Base()

        with self.assertRaises(NotImplementedError):
            b.to_dictionary()

    def incorrect_arguments(self):
        b = Base()

        with self.assertRaises(TypeError):
            b.to_dictionary("hi")


class TestUpdate(unittest.TestCase):
    def test_always_raises_not_implemented(self):
        b = Base()

        with self.assertRaises(NotImplementedError):
            b.update()
            b.update("GOD")
            b.update("IS")
            b.update("NEVER")
            b.update("GONNA")
            b.update("GIVE YOU UP")
            b.update("never", "gonna", let="you down")
            b.update(range(0, 10), int_=int)


class TestToJSONString(unittest.TestCase):
    def test_wrong_amount_of_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string(9, 8)

    def test_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_correct_type(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        result = Base.to_json_string([{}])
        self.assertEqual(result, "[{}]")

        result = Base.to_json_string([{}, {}])
        self.assertEqual(result, "[{}, {}]")

        result = Base.to_json_string([{}, {}, {}])
        self.assertEqual(result, "[{}, {}, {}]")

        result = Base.to_json_string([{"Hello, World!"}])
        self.assertEqual(result, "[{'Hello, World!'}]")

        result = Base.to_json_string([{"Holber": "ton"}])
        self.assertEqual(result, "[{'Holber': 'ton'}]")

        result = Base.to_json_string([{5: "50", "hi": {{}: float()}}])
        self.assertEqual(result, "[{5: '50', 'hi': {{}: 0.0}}]")

        result = Base.to_json_string([{5: 5.5, True: False}, {[]: "hi"}])
        self.assertEqual(result, "[{5: 5.5, True: False}, {[]: 'hi'}]")


class TestSaveToFile(unittest.TestCase):
    def test_wrong_amount_of_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

        with self.assertRaises(TypeError):
            Base.save_to_file("hello", "world")

    def test_none(self):
        Base.save_to_file(None)

        with open("Base.json", "r") as output_file_test:
            # if the file doesn't exist, the function failed,
            # and therefore, the test will fail with
            # FileNotFoundError
            self.assertEqual(output_file_test.read(), "[]")

    def test_correct_type(self):
        Base.save_to_file([])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(), "[]")

        Base.save_to_file([{}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(), "[{}]")

        Base.save_to_file([{}, {}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(), "[{}, {}]")

        Base.save_to_file([{}, {}, {}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(), "[{}, {}, {}]")

        Base.save_to_file([{"Hello, World!"}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(), "[{'Hello, World!'}]")

        Base.save_to_file([{"Holber": "ton"}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(), "[{'Holber': 'ton'}]")

        Base.save_to_file([{5: "50", "hi": {{}: float()}}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(),
                             "[{5: '50', 'hi': {{}: 0.0}}]")

        Base.save_to_file([{5: 5.5, True: False}, {[]: "hi"}])
        with open("Base.json", "r") as output_file_test:
            self.assertEqual(output_file_test.read(),
                             "[{5: 5.5, True: False}, {[]: 'hi'}]")


class TestFromJsonString(unittest.TestCase):
    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

        with self.assertRaises(TypeError):
            Base.from_json_string("h", "i")
