#!/usr/bin/python3

# 0. If it's not tested it doesn't work
# Run: python3 -m unittest discover tests

"""
CLass #0: SquareInstances
Class #1: WidthInstancesS
Class #2: HeightIstancesS
Class #3: XInstancesS
Class #4: YInstancesS
Class #5: SquareInitOrder
Class #6: SquareArea
Class #7: DisplayMethodsS
Class #8: SquareArgs
Class #9: SquareKwargs
Class #10: SquareTodict
"""

import io
import sys
import unittest
from models.base import Base as B
from models.square import Square as S


# Class #0
class SquareInstances(unittest.TestCase):
    """A class that defines instances of the Square model"""

    def PassBaseSquare(self):
        """A function that checks if square if of a base model"""

        self.assertIsInstance(S(10, 2), B)

    def PassNoArgsS(self):
        """A function that passes no arguments to rectangle class"""

        with self.assertSaises(TypeError):
            S()

    def PassOneArgS(self):
        """A function that passes only one argument"""

        with self.assertSaises(TypeError):
            S(13)

    def PassTwoArgsS(self):
        """A function that passes 2 arguments"""

        s1 = S(10, 2)
        s2 = S(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def PassrThreeArgsS(self):
        """A function that passes 3 arguments"""

        s1 = S(2, 2, 4)
        s2 = S(4, 4, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def PassFourArgsS(self):
        """A function that passes 4 arguments"""

        s1 = S(1, 2, 3, 4)
        s2 = S(4, 3, 2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def PassFiveArgsS(self):
        """A function that passes 5 arguments"""

        self.assertEqual(7, S(10, 2, 0, 0, 7).id)

    def PassOverFiveArgsS(self):
        """A function that passes more than 5 arguments"""

        with self.assertSaises(TypeError):
            S(1, 2, 3, 4, 5, 6)

    def PassPrivateWidthS(self):
        """A function that passes private width instances"""

        with self.assertSaises(AttributeError):
            print(S(5, 5, 0, 0, 1).__width)

    def PassPrivateHeightS(self):
        """ A function that passes private height instances"""

        with self.assertSaises(AttributeError):
            print(S(5, 5, 0, 0, 1).__height)

    def PassPrivateXS(self):
        """A function that passes private x instances"""

        with self.assertSaises(AttributeError):
            print(S(5, 5, 0, 0, 1).__x)

    def PassPrivateYS(self):
        """A function that passes private width instances"""

        with self.assertSaises(AttributeError):
            print(S(5, 5, 0, 0, 1).__y)

    def PassWidthGetterS(self):
        """A function that passes width with @getter"""

        s = S(5, 7, 7, 5, 1)
        self.assertEqual(5, s.width)

    def PassWidthSetterS(self):
        """A function that passes width with @setter"""

        s = S(5, 7, 7, 5, 1)
        s.width = 10
        self.assertEqual(10, s.width)

    def PassHeightGetterS(self):
        """A function that passes height with @getter"""

        s = S(5, 7, 7, 5, 1)
        self.assertEqual(7, s.height)

    def PassHeightSetterS(self):
        """A function that passes height with @setter"""

        s = S(5, 7, 7, 5, 1)
        s.height = 10
        self.assertEqual(10, s.height)

    def PassXGetterS(self):
        """A function that passes x with @getter"""

        s = S(5, 7, 7, 5, 1)
        self.assertEqual(7, s.x)

    def PassXSetterS(self):
        """A function that passes x with @setter"""

        s = S(5, 7, 7, 5, 1)
        s.x = 10
        self.assertEqual(10, s.x)

    def PassYGetterS(self):
        """A function that passes y with @getter"""

        s = S(5, 7, 7, 5, 1)
        self.assertEqual(5, s.y)

    def PassYSetterS(self):
        """A function that passes y with @setter"""

        s = S(5, 7, 7, 5, 1)
        s.y = 10
        self.assertEqual(10, s.y)


# Class #1
class WidthInstancesS(unittest.TestCase):
    """A class that defines instances for width attribute"""

    def PassNoneWS(self):
        """A function that passes None as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(None, 13)

    def PassStringWS(self):
        """A function that passes a string as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S("hannibal", 13)

    def PassFloatWS(self):
        """A function that passes a floating point as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(1.3, 3)

    def PassComplexWS(self):
        """A function that passes a complex number as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(complex(5), 2)

    def PassDictWS(self):
        """A function that passes a dictionary as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S({"a": 1, "b": 2}, 2)

    def PassBooleanWS(self):
        """A function that passes a boolean value as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(True, 2)

    def PassListWS(self):
        """A function that passes a list as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S([1, 2, 3], 2)

    def PassSetWS(self):
        """A function that passes a set as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S({1, 2, 3}, 2)

    def PassTupleWS(self):
        """A function that passes a tuple as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S((1, 2, 3), 2)

    def PassFrozenSetWS(self):
        """A function that passes a frozenset as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(frozenset({1, 2, 3, 1}), 2)

    def PassSangeWS(self):
        """A function that passes a range of numbers as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(range(5), 2)

    def PassByteWS(self):
        """A function that passes bytes as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(b'Python', 2)

    def PassByteArrayWS(self):
        """A function that passes a butearray as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(bytearray(b'abcdefg'), 2)

    def PassMemoryViewWS(self):
        """A function that passes a mempryview as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(memoryview(b'abcedfg'), 2)

    def PassInfWS(self):
        """A function that passes inf as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(float('inf'), 2)

    def PassNanWS(self):
        """A function that passes nan as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S(float('nan'), 2)

    def PassNegWS(self):
        """A function that passes a negative number as width argument"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            S(-1, 2)

    def PassZeroWS(self):
        """A function that passes 0 as width argument"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            S(0, 2)


# Class #2
class HeightInstancesS(unittest.TestCase):
    """A class that defines instances for height attribute"""

    def PassNoneHS(self):
        """A function that passes None as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(None, 13)

    def PassStringHS(self):
        """A function that passes a string as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S("hannibal", 13)

    def PassFloatHS(self):
        """A function that passes a floating point as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(1.3, 3)

    def PassComplexHS(self):
        """A function that passes a complex number as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(complex(5), 2)

    def PassDictHS(self):
        """A function that passes a dictionary as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S({"a": 1, "b": 2}, 2)

    def PassBooleanHS(self):
        """A function that passes a boolean value as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(True, 2)

    def PassListHS(self):
        """A function that passes a list as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S([1, 2, 3], 2)

    def PassSetHS(self):
        """A function that passes a set as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S({1, 2, 3}, 2)

    def PassTupleHS(self):
        """A function that passes a tuple as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S((1, 2, 3), 2)

    def PassFrozenSetHS(self):
        """A function that passes a frozenset as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(frozenset({1, 2, 3, 1}), 2)

    def PassSangeHS(self):
        """A function that passes a range of numbers as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(range(5), 2)

    def PassByteHS(self):
        """A function that passes bytes as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(b'Python', 2)

    def PassByteArrayHS(self):
        """A function that passes a butearray as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(bytearray(b'abcdefg'), 2)

    def PassMemoryViewHS(self):
        """A function that passes a mempryview as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(memoryview(b'abcedfg'), 2)

    def PassInfHS(self):
        """A function that passes inf as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(float('inf'), 2)

    def PassNanHS(self):
        """A function that passes nan as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(float('nan'), 2)

    def PassNegHS(self):
        """A function that passes a negative number as height argument"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            S(-1, 2)

    def PassZeroHS(self):
        """A function that passes 0 as height argument"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            S(0, 2)


# Class #3
class XInstancesS(unittest.TestCase):
    """A class that defines instances for x attribute"""

    def PassNoneXS(self):
        """A function that passes None as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(None, 13)

    def PassStringXS(self):
        """A function that passes a string as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S("hannibal", 13)

    def PassFloatXS(self):
        """A function that passes a floating point as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(1.3, 3)

    def PassComplexXS(self):
        """A function that passes a complex number as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(complex(5), 2)

    def PassDictXS(self):
        """A function that passes a dictionary as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S({"a": 1, "b": 2}, 2)

    def PassBooleanXS(self):
        """A function that passes a boolean value as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(True, 2)

    def PassListXS(self):
        """A function that passes a list as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S([1, 2, 3], 2)

    def PassSetXS(self):
        """A function that passes a set as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S({1, 2, 3}, 2)

    def PassTupleXS(self):
        """A function that passes a tuple as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S((1, 2, 3), 2)

    def PassFrozenSetXS(self):
        """A function that passes a frozenset as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(frozenset({1, 2, 3, 1}), 2)

    def PassSangeXS(self):
        """A function that passes a range of numbers as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(range(5), 2)

    def PassByteXS(self):
        """A function that passes bytes as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(b'Python', 2)

    def PassByteArrayXS(self):
        """A function that passes a butearray as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(bytearray(b'abcdefg'), 2)

    def PassMemoryViewXS(self):
        """A function that passes a mempryview as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(memoryview(b'abcedfg'), 2)

    def PassInfXS(self):
        """A function that passes inf as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(float('inf'), 2)

    def PassNanXS(self):
        """A function that passes nan as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(float('nan'), 2)

    def PassNegXS(self):
        """A function that passes a negative number as x argument"""

        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            S(-1, 2)

    def PassZeroXS(self):
        """A function that passes 0 as x argument"""

        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            S(0, 2)


# Class #4
class YInstancesS(unittest.TestCase):
    """A class that defines instances for y attribute"""

    def PassNoneYS(self):
        """A function that passes None as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(None, 13)

    def PassStringYS(self):
        """A function that passes a string as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S("hannibal", 13)

    def PassFloatYS(self):
        """A function that passes a floating point as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(1.3, 3)

    def PassComplexYS(self):
        """A function that passes a complex number as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(complex(5), 2)

    def PassDictYS(self):
        """A function that passes a dictionary as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S({"a": 1, "b": 2}, 2)

    def PassBooleanYS(self):
        """A function that passes a boolean value as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(True, 2)

    def PassListYS(self):
        """A function that passes a list as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S([1, 2, 3], 2)

    def PassSetYS(self):
        """A function that passes a set as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S({1, 2, 3}, 2)

    def PassTupleYS(self):
        """A function that passes a tuple as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S((1, 2, 3), 2)

    def PassFrozenSetYS(self):
        """A function that passes a frozenset as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(frozenset({1, 2, 3, 1}), 2)

    def PassSangeYS(self):
        """A function that passes a range of numbers as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(range(5), 2)

    def PassByteYS(self):
        """A function that passes bytes as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(b'Python', 2)

    def PassByteArrayYS(self):
        """A function that passes a butearray as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(bytearray(b'abcdefg'), 2)

    def PassMemoryViewYS(self):
        """A function that passes a mempryview as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(memoryview(b'abcedfg'), 2)

    def PassInfYS(self):
        """A function that passes inf as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(float('inf'), 2)

    def PassNanYS(self):
        """A function that passes nan as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            S(float('nan'), 2)

    def PassNegYS(self):
        """A function that passes a negative number as y argument"""

        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            S(-1, 2)

    def PassZeroYS(self):
        """A function that passes 0 as y argument"""

        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            S(0, 2)


# Class #5
class SquareInitOrder(unittest.TestCase):
    """A class that defines the order of initializing rectabgle instances"""

    def WidthFirstSh(self):
        """A function that passes width before height"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S("invalid width", "invalid height")

    def WidthFirstSx(self):
        """A function that passes width before x"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S("invalid width", 2, "invalid x")

    def WidthFirstSy(self):
        """A function that passes width before y"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S("invalid width", 2, 3, "invalid y")

    def HeightFirstSx(self):
        """A function that passes height before x"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(1, "invalid height", "invalid x")

    def HeightFirstSy(self):
        """A function that passes height before y"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            S(1, "invalid height", 2, "invalid y")

    def XFirstSy(self):
        """A function that passes x before y"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(1, 2, "invalid x", "invalid y")


# Class #6
class SquareArea(unittest.TestCase):
    """A class that defines area of a rectangle"""

    def SmallAreaS(self):
        """A function that passes a small area"""

        s = S(10, 2, 0, 0, 0)
        self.assertEqual(20, s.area())

    def LargeAreaS(self):
        """A function that passes a large area"""

        s = S(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, s.area())

    def ChangedAreaS(self):
        """A function that pass changed attributes as area"""

        s = S(2, 10, 1, 1, 1)
        s.width = 7
        s.height = 14
        self.assertEqual(98, s.area())

    def OneAreaS(self):
        """A function that passes only 1 area"""

        s = S(2, 10, 1, 1, 1)
        with self.assertSaises(TypeError):
            s.area(1)


# Class #7
class DisplayMethodsS(unittest.TestCase):
    """A class that defines the print & display methons of a rectangle"""

    @staticmethod
    def CaptureStdout(rect, method):
        """A function that defines attributes to capture rectangle display"""

        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)

        else:
            rect.display()

        sys.stdout = sys.__stdout__
        return (capture)

    #  __str__ method
    def PrintWidthHeightS(self):
        """A function that prints a rectangle given w & h to stdout"""

        s = S(4, 6)
        capture = DisplayMethodsS.CaptureStdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4/6\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def PrintWidthHeightXS(self):
        """A function that prints a rectangle given w, h & x to stdout"""

        s = S(5, 5, 1)
        correct = "[Square] ({}) 1/0 - 5/5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def PrintWidthHeightXYS(self):
        """A function that prints a rectangle given w, h, x & y to stdout"""

        s = S(1, 8, 2, 4)
        correct = "[Square] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(s))

    def PrintWidthHeightXYIDS(self):
        """A function that prints a rectangle given w,h,x,y,id to stdout"""

        s = S(13, 21, 2, 4, 7)
        self.assertEqual("[Square] (7) 2/4 - 13/21", str(s))

    def PrintStrChangedAttS(self):
        """A function that prints rectangle with str method changed values"""

        s = S(7, 7, 0, 0, [4])
        s.width = 15
        s.height = 1
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15/1", str(s))

    def PrintStrOneArgS(self):
        """A function that prints rectangle with only one argument given"""

        s = S(1, 2, 3, 4, 5)
        with self.assertSaises(TypeError):
            s.__str__(1)

    # display method
    def DisplayWidthHeightS(self):
        """A function taht displays a rectangle given w & h to stdout"""

        s = S(2, 3, 0, 0, 0)
        capture = DisplayMethodsS.CaptureStdout(s, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def DisplayWidthHeightXS(self):
        """A function taht displays a rectangle given w,h, x to stdout"""

        s = S(3, 2, 1, 0, 1)
        capture = DisplayMethodsS.CaptureStdout(s, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def DisplayWidthHeightYS(self):
        """A function taht displays a rectangle given w,h,y to stdout"""

        s = S(4, 5, 0, 1, 0)
        capture = DisplayMethodsS.CaptureStdout(s, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def DisplayWidthHeightXYS(self):
        """A function taht displays a rectangle given w,h,x,y to stdout"""

        s = S(2, 4, 3, 2, 0)
        capture = DisplayMethodsS.CaptureStdout(s, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def DisplayOneArgS(self):
        """A function that displays a rectangle given only 1 argument"""

        s = S(5, 1, 2, 4, 7)
        with self.assertSaises(TypeError):
            s.display(1)


# Class #8
class SquareArgs(unittest.TestCase):
    """A class that defines updating *args method for rectangle model"""

    def Pass0SArg(self):
        """A function that passes 0 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10/10", str(s))

    def Pass1SArg(self):
        """A function that passes 0 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10/10", str(s))

    def Pass2SArg(self):
        """A function that passes 2 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2/10", str(s))

    def Pass3SArg(self):
        """A function that passes 3 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 10/10 - 2/3", str(s))

    def Pass4SArg(self):
        """A function that passes 4 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 4/10 - 2/3", str(s))

    def Pass5SArg(self):
        """A function that passes 5 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 4/5 - 2/3", str(s))

    def PassOver5SArg(self):
        """A function that passes over 5 attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Square] (89) 4/5 - 2/3", str(s))

    def PassNoneSArg(self):
        """A function that passes None as attribute to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10/10".format(s.id)
        self.assertEqual(correct, str(s))

    def PassNoneIDSArg(self):
        """A function that passes NOne and ID attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(None, 4, 5, 2)
        correct = "[Square] ({}) 2/10 - 4/5".format(s.id)
        self.assertEqual(correct, str(s))

    def PassUpdated2SArg(self):
        """A function that passes twice updated attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5, 6)
        s.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Square] (6) 3/2 - 5/4", str(s))

    def PassInvalidWidthSArg(self):
        """A function that passes invalid width type attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def PassZeroWidthSArg(self):
        """A function that passes zero width type attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def PassNegWidthSArg(self):
        """A function that passes negative width type attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -5)

    def PassInvalidHeightSArg(self):
        """A function that passes invalid height type attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s.update(89, 2, "invalid")

    def PassZeroHeightSArg(self):
        """A function that passes zero height attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s.update(89, 1, 0)

    def PassNegHeightSArg(self):
        """A function that passes negative height attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s.update(89, 1, -5)

    def PassInvalidXSArg(self):
        """A function that passes invalid x type attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 2, 3, "invalid")

    def PassNegXSArg(self):
        """A function that passes negative x attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(89, 1, 2, -6)

    def PassInvalidYSArg(self):
        """A function that passes invalid y type attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 2, 3, 4, "invalid")

    def PassNegYSArg(self):
        """A function that passes negative y attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(89, 1, 2, 3, -6)

    def PassWidthHeightSArg(self):
        """A function that passes width before height attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def PassWidthXSArg(self):
        """A function that passes width before x attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 1, "invalid")

    def PassWidthYSArg(self):
        """A function that passes width before y attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 1, 2, "invalid")

    def PassHeightXSArg(self):
        """A function that passes height before x attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s.update(89, 1, "invalid", "invalid")

    def PassHeightYSArg(self):
        """A function that passes height before y attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s.update(89, 1, "invalid", 1, "invalid")

    def PassXYSArg(self):
        """A function that passes x before y attributes to *args"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, 2, "invalid", "invalid")


# Class #9
class SquareKwargs(unittest.TestCase):
    """A class that defines updating **kwargs method for rectangle model"""

    def Pass1SKwarg(self):
        """A function that passes 1 attribute to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10/10", str(s))

    def Pass2SKwarg(self):
        """A function that passes 2 attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(width=2, id=1)
        self.assertEqual("[Square] (1) 10/10 - 2/10", str(s))

    def Pass3SKwarg(self):
        """A function that passes 3 attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(width=2, height=3, id=89)
        self.assertEqual("[Square] (89) 10/10 - 2/3", str(s))

    def Pass4SKwarg(self):
        """A function that passes 4 attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(id=89, x=1, height=2, width=4)
        self.assertEqual("[Square] (89) 1/3 - 4/2", str(s))

    def Pass5SKwarg(self):
        """A function that passes 5 attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Square] (99) 8/5 - 1/2", str(s))

    def PassNoneSKwarg(self):
        """A function that passes None as attribute to **kwars"""

        s = S(10, 10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10/10".format(s.id)
        self.assertEqual(correct, str(s))

    def PassNoneIDSKwarg(self):
        """A function that passes None and id as attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(id=None, height=7, y=9)
        correct = "[Square] ({}) 10/9 - 10/7".format(s.id)
        self.assertEqual(correct, str(s))

    def PassUpdated2SKwarg(self):
        """A function that passes twice updated attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(id=89, x=1, height=2)
        s.update(y=3, height=15, width=2)
        self.assertEqual("[Square] (89) 1/3 - 2/15", str(s))

    def PassInvalidWidthSKwarg(self):
        """A function that passes invalid width type attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(width="invalid")

    def PassZeroWidthSKwarg(self):
        """A function that passes zero width attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(width=0)

    def PassNegWidthSKwarg(self):
        """A function that passes negative width attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(width=-5)

    def PassInvalidHeightSKwarg(self):
        """A function that passes invalid height type attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            s.update(height="invalid")

    def PassZeroHeightSKwarg(self):
        """A function that passes zero height attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s.update(height=0)

    def PassNegHeightSKwarg(self):
        """A function that passes negative height attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            s.update(height=-5)

    def PassInvalidXSKwarg(self):
        """A function that passes invalid x type attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def PassNegXSKwarg(self):
        """A function that passes negative x attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def PassInvalidYSKwarg(self):
        """A function that passes invalid y type attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def PassNegYSKwarg(self):
        """A function that passes negative y attributes to **kwargs"""

        s = S(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def PassArgsAndKwargsS(self):
        """A function that passes to *args and **kwargs"""

        s = S(10, 10, 10, 10, 10)
        s.update(89, 2, height=4, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2/10", str(s))

    def PassWrongKeysSKwargs(self):
        """A function that passes wrong keys as attributes"""

        s = S(10, 10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10/10", str(s))

    def PassMoreWrongKeysSKwargs(self):
        """A function that passes wrong keys as attributes"""

        s = S(10, 10, 10, 10, 10)
        s.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 10/5", str(s))


# Class #10
class SquareTodict(unittest.TestCase):
    """A class that defines dictionary representation of rectangles"""

    def SToDictOutput(self):
        """A function that passes dictionary output"""

        s = S(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, s.to_dictionary())

    def SToDoictNoObj(self):
        """A function that passes dictionary with no object changes"""

        s1 = S(10, 2, 1, 9, 5)
        s2 = S(5, 9, 1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def SToDictArgs(self):
        """A function that passes dictionary arguments"""

        s = S(10, 2, 4, 1, 2)
        with self.assertSaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
