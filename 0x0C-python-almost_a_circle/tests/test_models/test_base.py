#!/usr/bin/python3

# 0. If it's not tested it doesn't work
# Run: python3 -m unittest discover tests

"""
CLass #0: ModelInstances
Class #1: MOdelToJSON
Class #2: MOdelFromJSON
Class #3: SaveModelToFile
Class #4: CreateMOdel
Class #5: LoadFromFile
Class #6: SaveModelToCSV
Class #7: LoadFRomCSV
"""

import os
import unittest
from models.base import Base as B
from models.square import Square as S
from models.rectangle import Rectangle as R


# Class #0
class ModelInstances(unittest.TestCase):
    """A class to test instances of Base arguments"""

    def PassNoArgs(self):
        """A function that passes no arguments"""

        b1 = B()
        b2 = B()
        self.assertEqual(b1.id, b2.id - 1)

    def Pass3Bases(self):
        """A function that passes three bases arguments"""

        b1 = B()
        b2 = B()
        b3 = B()
        self.assertEqual(b1.id, b3.id - 2)

    def PassNone(self):
        "A function that passes NONE as arguments"

        b1 = B(None)
        b2 = B(None)
        self.assertEqual(b1.id, b2.id - 1)

    def PassUID(self):
        """A function that passes unique ID"""

        self.assertEqual(12, B(12).id)

    def PassNoargsAndUID(self):
        """A function that passes no arguments a unique ID"""

        b1 = B()
        b2 = B(13)
        b3 = B()
        self.assertEqual(b1.id, b3.id - 1)

    def PassPID(self):
        """A function that passes a public ID as arguments"""

        b = B(10)
        b.id = 13
        self.assertEqual(13, b.id)

    def PassPrivateInsatnces(self):
        """A function that passes Private instances as arguments"""

        with self.assertRaises(AttributeError):
            print(B(13).__nb_instances)

    def PassSting(self):
        """A function that passes strings as arguments"""

        self.assertEqual("Hannibal", B("Hannibal").id)

    def PassFloatingPount(self):
        """A function that passes floating point values as arguments"""

        self.assertEqual(4.04, B(4.04).id)

    def PassComplexNUm(self):
        """A function that passes complex numbers as arguments"""

        self.assertEqual(complex(13), B(complex(13)).id)

    def PassDict(self):
        """A function that passes dictionary arguments"""

        self.assertEqual({"a": 13, "b": 31}, B({"a": 13, "b": 31}).id)

    def PassBoolean(self):
        """A function that passes Boolean arguments"""

        self.assertEqual(False, B(False).id)

    def PassList(self):
        """A function that passes a list as arguments"""

        self.assertEqual([13, 13, 31], B([3, 13, 31]).id)

    def PassTuple(self):
        """A function that passes a tuple as arguments"""

        self.assertEqual((13, 31), B((13, 31)).id)

    def PassSet(self):
        """A function that passes a set as arguments"""

        self.assertEqual({3, 13, 31}, B({3, 13, 31}).id)

    def PassFrozenset(self):
        """A function that passes a frozenset as arguments"""

        self.assertEqual(frozenset({3, 1, 3}), B(frozenset({3, 1, 3})).id)

    def PassNumRange(self):
        """A function that passes a range of numbers as arguments"""

        self.assertEqual(range(5), B(range(5)).id)

    def PassByte(self):
        """A function that passes byte attributes as arguments"""

        self.assertEqual(b'Flowers', B(b'Flowers').id)

    def PassByteArray(self):
        """A function that passes bytearray arguments"""

        self.assertEqual(bytearray(b'mejbri'), B(bytearray(b'mejbri')).id)

    def PassMemoryview(self):
        """A function that passes memoryview arguments"""

        self.assertEqual(memoryview(b'cisfun'), B(memoryview(b'cisfun')).id)

    def PassInfFloat(self):
        """Pass inf floating point values as arguments"""

        self.assertEqual(float('inf'), B(float('inf')).id)

    def PassNAN(self):
        """A function that passes nan as a floating point argument"""

        self.assertNotEqual(float('nan'), B(float('nan')).id)

    def Pass2Args(self):
        """A function that passes 2 regular integers as arguments"""

        with self.assertRaises(TypeError):
            B(1, 2)


# Class #1
class ModelToJSON(unittest.TestCase):
    """A class that tests modules from other types to JSON strings"""

    def PassRStringToJSON(self):
        """A function that passes strings to JSON"""

        r = R(10, 7, 2, 8, 6)
        self.assertEqual(str, type(B.to_json_string([r.to_dictionary()])))

    def PassRDictToJSON(self):
        """A function that passes a dictionary to JSON"""

        r = R(10, 7, 2, 8, 6)
        self.assertTrue(len(B.to_json_string([r.to_dictionary()])) == 53)

    def Pass2RDictsToJSON(self):
        """A function that passes 2 list dictionaries to JSON"""

        r1 = R(2, 3, 5, 19, 2)
        r2 = R(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(B.to_json_string(list_dicts)) == 106)

    def PassSSringToJSON(self):
        """A function that passes strings to JSON"""

        s = S(13, 14, 15, 16)
        self.assertEqual(str, type(B.to_json_string([s.to_dictionary()])))

    def PassSDictToJSON(self):
        """A function that passes a dictionary to JSON"""

        s = S(10, 2, 3, 4)
        self.assertTrue(len(B.to_json_string([s.to_dictionary()])) == 39)

    def Pass2SDictsToJSON(self):
        """A function thatpasses 2 list dictionaries to JSON"""

        s1 = S(10, 2, 3, 4)
        s2 = S(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(B.to_json_string(list_dicts)) == 78)

    def PassEmptyListToJSON(self):
        """A function that passes empty list to JSON"""

        self.assertEqual("[]", B.to_json_string([]))

    def PassNoneToJSON(self):
        """A function that passes None to JSON"""

        self.assertEqual("[]", B.to_json_string(None))

    def PassNoArgsToJSON(self):
        """A function that passes no arguments to JSON"""

        with self.assertRaises(TypeError):
            B.to_json_string()

    def Pass2ArgsToJSON(self):
        """A function that passes more than 1 argument to JSON"""

        with self.assertRaises(TypeError):
            B.to_json_string([], 13)


# Class #2
class ModelFromJSON(unittest.TestCase):
    """A class that tests modules from JSON strings to other types"""

    def PassToRList1(self):
        """A function that passes from JSON to list output"""

        list_input = [{"id": 13, "width": 13, "height": 3}]
        json_list_input = R.to_json_string(list_input)
        list_output = R.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def PassToRList2(self):
        """A function that passes from JSON to list output"""

        list_input = [{"id": 14, "width": 14, "height": 4, "x": 4}]
        json_list_input = R.to_json_string(list_input)
        list_output = R.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def PassTo2RList(self):
        """A function that passes from JSON to 2 list outputs"""

        list_input = [
            {"id": 1, "width": 20, "height": 10, "x": 4, "y": 2},
            {"id": 2, "width": 40, "height": 20, "x": 8, "y": 4},
        ]
        json_list_input = R.to_json_string(list_input)
        list_output = R.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def PassToSList1(self):
        """A function that passes from JSON to list output"""

        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = S.to_json_string(list_input)
        list_output = S.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def PassTo2SList(self):
        """A function that passes from JSON to 2 list outputs"""

        list_input = [
            {"id": 1, "size": 10, "height": 5},
            {"id": 2, "size": 20, "height": 10}
        ]
        json_list_input = S.to_json_string(list_input)
        list_output = S.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def PassToNone(self):
        """A function that passes from JSON to NOne"""

        self.assertEqual([], B.from_json_string(None))

    def PassToEmpty(self):
        """A function that passes from JSON to empty list"""

        self.assertEqual([], B.from_json_string("[]"))

    def PassToNoArgs(self):
        """A function that passes from JSON to no arguments"""

        with self.assertRaises(TypeError):
            B.from_json_string()

    def PassTo2Args(self):
        """A function that passes more than one arguments"""

        with self.assertRaises(TypeError):
            B.from_json_string([], 13)


# Class #3
class SaveModelToFile(unittest.TestCase):
    """A class to save Base models to a file"""

    @classmethod
    def tearDown(self):
        """A function that removes existing models"""

        try:
            os.remove("Rectangle.json")

        except IOError:
            pass

        try:
            os.remove("Square.json")

        except IOError:
            pass

        try:
            os.remove("Base.json")

        except IOError:
            pass

    def Save1RToFile(self):
        """A function to save 1 rectangle to a file"""

        r = R(10, 7, 2, 8, 5)
        R.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def Save2RToFile(self):
        """A function to save 2 rectangles to a file"""

        r1 = R(10, 7, 2, 8, 5)
        r2 = R(2, 4, 1, 2, 3)
        R.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def Save1SToFile(self):
        """A function to save 1 square to a file"""

        s = S(10, 7, 2, 8)
        S.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def Save2SToFile(self):
        """A function to save 2 squares to a file"""

        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def SaveBaseToFile(self):
        """A function to save base model to a file"""

        s = S(10, 7, 2, 8)
        B.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def SaveOverwrite(self):
        """A function to save to existing file and overwite content"""

        s = S(9, 2, 39, 2)
        S.save_to_file([s])
        s = S(10, 7, 2, 8)
        S.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def SaveNoneToFile(self):
        """A function that save None to file"""

        S.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def SaveEmptyToFile(self):
        """A function that saves an empty list to a file"""

        S.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def SaveNoArgsToFile(self):
        """A function that saves no arguments to a file"""

        with self.assertRaises(TypeError):
            R.save_to_file()

    def SaveMoreArgsToFile(self):
        """A function that saves more than 1 arguments to a file"""

        with self.assertRaises(TypeError):
            S.save_to_file([], 13)


# Class #4
class CreateModel(unittest.TestCase):
    """A class that defines creation of base models"""

    def CreateNormalRectangle(self):
        """A function to create a rectangle"""

        r1 = R(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = R.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def CreateNewRectangle(self):
        """A function to create a rectangle"""

        r1 = R(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = R.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def CreateNormalRectangle2(self):
        """A function to create a rectangle"""

        r1 = R(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = R.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def CreateNewRectangle2(self):
        """A function that creates a rectangle"""

        r1 = R(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = R.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def CreateNormalSquare(self):
        """A function that creates a square"""

        s1 = S(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = S.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def CreateNewSquare(self):
        """A function that creates a square"""

        s1 = S(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = S.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def CreateNormalSquare2(self):
        """A function that creates a square"""

        s1 = S(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = S.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def CreateNewSquare2(self):
        """A function that creates a square"""

        s1 = S(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = S.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


# Class #5
class LoadFromFile(unittest.TestCase):
    """A class that loads methods of Base models from a file"""

    @classmethod
    def tearDown(self):
        """A function that deletes previously loaded files"""

        try:
            os.remove("Rectangle.json")

        except IOError:
            pass

        try:
            os.remove("Square.json")

        except IOError:
            pass

    def LoadFirstRectangle(self):
        """A function that loads the first rectangle in a file"""

        r1 = R(10, 7, 2, 8, 1)
        r2 = R(2, 4, 5, 6, 2)
        R.save_to_file([r1, r2])
        list_rectangles_output = R.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def LoadSecondRectangle(self):
        """A function that loads the second rectangle in a file"""

        r1 = R(10, 7, 2, 8, 1)
        r2 = R(2, 4, 5, 6, 2)
        R.save_to_file([r1, r2])
        list_rectangles_output = R.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def LoadRectangleType(self):
        """A function that loads a rectangle from a file based on type"""

        r1 = R(10, 7, 2, 8, 1)
        r2 = R(2, 4, 5, 6, 2)
        R.save_to_file([r1, r2])
        output = R.load_from_file()
        self.assertTrue(all(type(obj) == R for obj in output))

    def LoadFirstSquare(self):
        """A function that loads the first square in a file"""

        s1 = S(5, 1, 3, 3)
        s2 = S(9, 5, 2, 3)
        S.save_to_file([s1, s2])
        list_squares_output = S.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def LoadSecondSquare(self):
        """A function that loads the secomd square in a file"""

        s1 = S(5, 1, 3, 3)
        s2 = S(9, 5, 2, 3)
        S.save_to_file([s1, s2])
        list_squares_output = S.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def LoadSquareType(self):
        """A function that loads a square from a file based on type"""

        s1 = S(5, 1, 3, 3)
        s2 = S(9, 5, 2, 3)
        S.save_to_file([s1, s2])
        output = S.load_from_file()
        self.assertTrue(all(type(obj) == S for obj in output))

    def LoadSFromNoFile(self):
        """A function that loads a square model from no file"""

        output = S.load_from_file()
        self.assertEqual([], output)

    def LoadRFromNoFile(self):
        """A function that loads a rectangle model from no file"""

        output = R.load_from_file()
        self.assertEqual([], output)

    def LoadMoreThan1Files(self):
        """A function that loads from more that one file"""

        with self.assertRaises(TypeError):
            B.load_from_file([], 1)


# Class #6
class SaveModelToCSV(unittest.TestCase):
    """A class that saves Base models to CSV files"""

    @classmethod
    def tearDown(self):
        """A function that deletes already saved csv files"""

        try:
            os.remove("Rectangle.csv")

        except IOError:
            pass

        try:
            os.remove("Square.csv")

        except IOError:
            pass

        try:
            os.remove("Base.csv")

        except IOError:
            pass

    def Save1RToCSV(self):
        """A function that saves a rectangle to a file in CSV format"""

        r = R(10, 7, 2, 8, 5)
        R.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def Save2RToCSV(self):
        """A function that saves 2 rectangles to a file in CSV format"""

        r1 = R(10, 7, 2, 8, 5)
        r2 = R(2, 4, 1, 2, 3)
        R.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def Save1SToCSV(self):
        """A function that saves a square to a file in CSV format"""

        s = S(10, 7, 2, 8)
        S.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def Save2SToCSV(self):
        """A function that saves 2 squares to a file in CSV format"""

        s1 = S(10, 7, 2, 8)
        s2 = S(8, 1, 2, 3)
        S.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def SaveBaseToCSV(self):
        """A function that saves Base models to files in CSV format"""

        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def SaveOverwriteToCSV(self):
        """A function that overwrites and saves model to file in CSV format"""

        s = S(9, 2, 39, 2)
        S.save_to_file_csv([s])
        s = S(10, 7, 2, 8)
        S.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def SaveNOneToCSV(self):
        """A function that saves None to a file in CSV format"""

        S.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def SaveEmptyToCSV(self):
        """A function that saves an empty list to a file in CSV format"""

        S.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def SaveNoArgsToCSV(self):
        """A function that passes no args to save in CSV format"""

        with self.assertRaises(TypeError):
            R.save_to_file_csv()

    def SaveMoreArgsToCSV(self):
        """A function to save more than 1 args to file in csv format"""

        with self.assertRaises(TypeError):
            S.save_to_file_csv([], 1)


# Class #7
class LoadFromCSV(unittest.TestCase):
    """A class that loads methods of Base models from a CSV file"""

    @classmethod
    def tearDown(self):
        """A function that deletes previously loaded CSV files"""

        try:
            os.remove("Rectangle.json")

        except IOError:
            pass

        try:
            os.remove("Square.json")

        except IOError:
            pass

    def LoadFirstRectangleCSV(self):
        """A function that loads the first rectangle in a CSV file"""

        r1 = R(10, 7, 2, 8, 1)
        r2 = R(2, 4, 5, 6, 2)
        R.save_to_file_csv([r1, r2])
        list_rectangles_output = R.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def LoadSecondRectangleCSV(self):
        """A function that loads the second rectangle in a CSV file"""

        r1 = R(10, 7, 2, 8, 1)
        r2 = R(2, 4, 5, 6, 2)
        R.save_to_file_csv([r1, r2])
        list_rectangles_output = R.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def LoadRectangleTypeCSV(self):
        """A function that loads a rectangle from a CSV file based on type"""

        r1 = R(10, 7, 2, 8, 1)
        r2 = R(2, 4, 5, 6, 2)
        R.save_to_file_csv([r1, r2])
        output = R.load_from_file_csv()
        self.assertTrue(all(type(obj) == R for obj in output))

    def LoadFirstSquareCSV(self):
        """A function that loads the first square in a file"""

        s1 = S(5, 1, 3, 3)
        s2 = S(9, 5, 2, 3)
        S.save_to_file_csv([s1, s2])
        list_squares_output = S.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def LoadSecondSquareCSV(self):
        """A function that loads the secomd square in a file"""

        s1 = S(5, 1, 3, 3)
        s2 = S(9, 5, 2, 3)
        S.save_to_file_csv([s1, s2])
        list_squares_output = S.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def LoadSquareTypeCSV(self):
        """A function that loads a square from a file based on type"""

        s1 = S(5, 1, 3, 3)
        s2 = S(9, 5, 2, 3)
        S.save_to_file_csv([s1, s2])
        output = S.load_from_file_csv()
        self.assertTrue(all(type(obj) == S for obj in output))

    def LoadSFromNoFileCSV(self):
        """A function that loads a square model from no file"""

        output = S.load_from_file_csv()
        self.assertEqual([], output)

    def LoadRFromNoFileCSV(self):
        """A function that loads a rectangle model from no file"""

        output = R.load_from_file_csv()
        self.assertEqual([], output)

    def LoadMoreThan1FilesCSV(self):
        """A function that loads from more that one file"""

        with self.assertRaises(TypeError):
            B.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
