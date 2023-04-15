#!/usr/bin/python3

# 0. If it's not tested it doesn't work
# Run: python3 -m unittest discover tests

"""
CLass #0: RectangleInstances
Class #1: WidthInstances
Class #2: HeightIstances
Class #3: XInstances
Class #4: YINstances
Class #5: RectangleInitOrder
Class #6: RectangleArea
Class #7: DisplayMethodsR
Class #8: RectangleArgs
Class #9: RectangleKwargs
Class #10: RectangleTodict
"""

import io
import sys
import unittest
from models.base import Base as B
from models.rectangle import Rectangle as R


# Class #0
class RectangleInstances(unittest.TestCase):
    """A class that defines instances of the Rectangle model"""

    def PassBaseRectangle(self):
        """A function that checks if rectangle if of a base model"""

        self.assertIsInstance(R(10, 2), B)

    def PassNoArgs(self):
        """A function that passes no arguments to rectangle class"""

        with self.assertRaises(TypeError):
            R()

    def PassOneArg(self):
        """A function that passes only one argument"""

        with self.assertRaises(TypeError):
            R(13)

    def PassTwoArgs(self):
        """A function that passes 2 arguments"""

        r1 = R(10, 2)
        r2 = R(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def PassTwoArgs(self):
        """A function that passes 3 arguments"""

        r1 = R(2, 2, 4)
        r2 = R(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def PassFourArgs(self):
        """A function that passes 4 arguments"""

        r1 = R(1, 2, 3, 4)
        r2 = R(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def PassFiveArgs(self):
        """A function that passes 5 arguments"""

        self.assertEqual(7, R(10, 2, 0, 0, 7).id)

    def PassOverFiveArgs(self):
        """A function that passes more than 5 arguments"""

        with self.assertRaises(TypeError):
            R(1, 2, 3, 4, 5, 6)

    def PassPrivateWidth(self):
        """A function that passes private width instances"""

        with self.assertRaises(AttributeError):
            print(R(5, 5, 0, 0, 1).__width)

    def PassPrivateHeight(self):
        """ A function that passes private height instances"""

        with self.assertRaises(AttributeError):
            print(R(5, 5, 0, 0, 1).__height)

    def PassPrivateX(self):
        """A function that passes private x instances"""

        with self.assertRaises(AttributeError):
            print(R(5, 5, 0, 0, 1).__x)

    def PassPrivateY(self):
        """A function that passes private width instances"""

        with self.assertRaises(AttributeError):
            print(R(5, 5, 0, 0, 1).__y)

    def PassWidthGetter(self):
        """A function that passes width with @getter"""

        r = R(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def PassWidthSetter(self):
        """A function that passes width with @setter"""

        r = R(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def PassHeightGetter(self):
        """A function that passes height with @getter"""

        r = R(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def PassHeightSetter(self):
        """A function that passes height with @setter"""

        r = R(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def PassXGetter(self):
        """A function that passes x with @getter"""

        r = R(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def PassXSetter(self):
        """A function that passes x with @setter"""

        r = R(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def PassYGetter(self):
        """A function that passes y with @getter"""

        r = R(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def PassYSetter(self):
        """A function that passes y with @setter"""

        r = R(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


# Class #1
class WidthInstances(unittest.TestCase):
    """A class that defines instances for width attribute"""

    def PassNoneW(self):
        """A function that passes None as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(None, 13)

    def PassStringW(self):
        """A function that passes a string as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R("hannibal", 13)

    def PassFloatW(self):
        """A function that passes a floating point as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(1.3, 3)

    def PassComplexW(self):
        """A function that passes a complex number as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(complex(5), 2)

    def PassDictW(self):
        """A function that passes a dictionary as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R({"a": 1, "b": 2}, 2)

    def PassBooleanW(self):
        """A function that passes a boolean value as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(True, 2)

    def PassListW(self):
        """A function that passes a list as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R([1, 2, 3], 2)

    def PassSetW(self):
        """A function that passes a set as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R({1, 2, 3}, 2)

    def PassTupleW(self):
        """A function that passes a tuple as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R((1, 2, 3), 2)

    def PassFrozenSetW(self):
        """A function that passes a frozenset as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(frozenset({1, 2, 3, 1}), 2)

    def PassRangeW(self):
        """A function that passes a range of numbers as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(range(5), 2)

    def PassByteW(self):
        """A function that passes bytes as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(b'Python', 2)

    def PassByteArrayW(self):
        """A function that passes a butearray as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(bytearray(b'abcdefg'), 2)

    def PassMemoryViewW(self):
        """A function that passes a mempryview as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(memoryview(b'abcedfg'), 2)

    def PassInfW(self):
        """A function that passes inf as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(float('inf'), 2)

    def PassNanW(self):
        """A function that passes nan as width argument"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R(float('nan'), 2)

    def PassNegW(self):
        """A function that passes a negative number as width argument"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            R(-1, 2)

    def PassZeroW(self):
        """A function that passes 0 as width argument"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            R(0, 2)


# Class #2
class HeightInstances(unittest.TestCase):
    """A class that defines instances for height attribute"""

    def PassNoneH(self):
        """A function that passes None as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(None, 13)

    def PassStringH(self):
        """A function that passes a string as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R("hannibal", 13)

    def PassFloatH(self):
        """A function that passes a floating point as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(1.3, 3)

    def PassComplexH(self):
        """A function that passes a complex number as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(complex(5), 2)

    def PassDictH(self):
        """A function that passes a dictionary as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R({"a": 1, "b": 2}, 2)

    def PassBooleanH(self):
        """A function that passes a boolean value as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(True, 2)

    def PassListH(self):
        """A function that passes a list as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R([1, 2, 3], 2)

    def PassSetH(self):
        """A function that passes a set as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R({1, 2, 3}, 2)

    def PassTupleH(self):
        """A function that passes a tuple as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R((1, 2, 3), 2)

    def PassFrozenSetH(self):
        """A function that passes a frozenset as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(frozenset({1, 2, 3, 1}), 2)

    def PassRangeH(self):
        """A function that passes a range of numbers as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(range(5), 2)

    def PassByteH(self):
        """A function that passes bytes as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(b'Python', 2)

    def PassByteArrayH(self):
        """A function that passes a butearray as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(bytearray(b'abcdefg'), 2)

    def PassMemoryViewH(self):
        """A function that passes a mempryview as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(memoryview(b'abcedfg'), 2)

    def PassInfH(self):
        """A function that passes inf as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(float('inf'), 2)

    def PassNanH(self):
        """A function that passes nan as height argument"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(float('nan'), 2)

    def PassNegH(self):
        """A function that passes a negative number as height argument"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            R(-1, 2)

    def PassZeroH(self):
        """A function that passes 0 as height argument"""

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            R(0, 2)


# Class #3
class XInstances(unittest.TestCase):
    """A class that defines instances for x attribute"""

    def PassNoneX(self):
        """A function that passes None as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(None, 13)

    def PassStringX(self):
        """A function that passes a string as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R("hannibal", 13)

    def PassFloatX(self):
        """A function that passes a floating point as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(1.3, 3)

    def PassComplexX(self):
        """A function that passes a complex number as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(complex(5), 2)

    def PassDictX(self):
        """A function that passes a dictionary as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R({"a": 1, "b": 2}, 2)

    def PassBooleanX(self):
        """A function that passes a boolean value as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(True, 2)

    def PassListX(self):
        """A function that passes a list as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R([1, 2, 3], 2)

    def PassSetX(self):
        """A function that passes a set as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R({1, 2, 3}, 2)

    def PassTupleX(self):
        """A function that passes a tuple as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R((1, 2, 3), 2)

    def PassFrozenSetX(self):
        """A function that passes a frozenset as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(frozenset({1, 2, 3, 1}), 2)

    def PassRangeX(self):
        """A function that passes a range of numbers as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(range(5), 2)

    def PassByteX(self):
        """A function that passes bytes as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(b'Python', 2)

    def PassByteArrayX(self):
        """A function that passes a butearray as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(bytearray(b'abcdefg'), 2)

    def PassMemoryViewX(self):
        """A function that passes a mempryview as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(memoryview(b'abcedfg'), 2)

    def PassInfX(self):
        """A function that passes inf as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(float('inf'), 2)

    def PassNanX(self):
        """A function that passes nan as x argument"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(float('nan'), 2)

    def PassNegX(self):
        """A function that passes a negative number as x argument"""

        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            R(-1, 2)

    def PassZeroX(self):
        """A function that passes 0 as x argument"""

        with self.assertRaisesRegex(ValueError, "x must be > 0"):
            R(0, 2)


# Class #4
class YInstances(unittest.TestCase):
    """A class that defines instances for y attribute"""

    def PassNoneY(self):
        """A function that passes None as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(None, 13)

    def PassStringY(self):
        """A function that passes a string as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R("hannibal", 13)

    def PassFloatY(self):
        """A function that passes a floating point as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(1.3, 3)

    def PassComplexY(self):
        """A function that passes a complex number as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(complex(5), 2)

    def PassDictY(self):
        """A function that passes a dictionary as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R({"a": 1, "b": 2}, 2)

    def PassBooleanY(self):
        """A function that passes a boolean value as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(True, 2)

    def PassListY(self):
        """A function that passes a list as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R([1, 2, 3], 2)

    def PassSetY(self):
        """A function that passes a set as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R({1, 2, 3}, 2)

    def PassTupleY(self):
        """A function that passes a tuple as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R((1, 2, 3), 2)

    def PassFrozenSetY(self):
        """A function that passes a frozenset as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(frozenset({1, 2, 3, 1}), 2)

    def PassRangeY(self):
        """A function that passes a range of numbers as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(range(5), 2)

    def PassByteY(self):
        """A function that passes bytes as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(b'Python', 2)

    def PassByteArrayY(self):
        """A function that passes a butearray as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(bytearray(b'abcdefg'), 2)

    def PassMemoryViewY(self):
        """A function that passes a mempryview as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(memoryview(b'abcedfg'), 2)

    def PassInfY(self):
        """A function that passes inf as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(float('inf'), 2)

    def PassNanY(self):
        """A function that passes nan as y argument"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            R(float('nan'), 2)

    def PassNegY(self):
        """A function that passes a negative number as y argument"""

        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            R(-1, 2)

    def PassZeroY(self):
        """A function that passes 0 as y argument"""

        with self.assertRaisesRegex(ValueError, "y must be > 0"):
            R(0, 2)


# Class #5
class RectangleInitOrder(unittest.TestCase):
    """A class that defines the order of initializing rectabgle instances"""

    def WidthFirstRh(self):
        """A function that passes width before height"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R("invalid width", "invalid height")

    def WidthFirstRx(self):
        """A function that passes width before x"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R("invalid width", 2, "invalid x")

    def WidthFirstRy(self):
        """A function that passes width before y"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R("invalid width", 2, 3, "invalid y")

    def HeightFirstRx(self):
        """A function that passes height before x"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(1, "invalid height", "invalid x")

    def HeightFirstRy(self):
        """A function that passes height before y"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            R(1, "invalid height", 2, "invalid y")

    def XFirstRy(self):
        """A function that passes x before y"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(1, 2, "invalid x", "invalid y")


# Class #6
class RectangleArea(unittest.TestCase):
    """A class that defines area of a rectangle"""

    def SmallAreaR(self):
        """A function that passes a small area"""

        r = R(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def LargeAreaR(self):
        """A function that passes a large area"""

        r = R(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def ChangedAreaR(self):
        """A function that pass changed attributes as area"""

        r = R(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def OneAreaR(self):
        """A function that passes only 1 area"""

        r = R(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


# Class #7
class DisplayMethodsR(unittest.TestCase):
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
    def PrintWidthHeightR(self):
        """A function that prints a rectangle given w & h to stdout"""

        r = R(4, 6)
        capture = DisplayMethodsR.CaptureStdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def PrintWidthHeightXR(self):
        """A function that prints a rectangle given w, h & x to stdout"""

        r = R(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def PrintWidthHeightXYR(self):
        """A function that prints a rectangle given w, h, x & y to stdout"""

        r = R(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def PrintWidthHeightXYIDR(self):
        """A function that prints a rectangle given w,h,x,y,id to stdout"""

        r = R(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def PrintStrChangedAttR(self):
        """A function that prints rectangle with str method changed values"""

        r = R(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def PrintStrOneArgR(self):
        """A function that prints rectangle with only one argument given"""

        r = R(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # display method
    def DisplayWidthHeightR(self):
        """A function taht displays a rectangle given w & h to stdout"""

        r = R(2, 3, 0, 0, 0)
        capture = DisplayMethodsR.CaptureStdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def DisplayWidthHeightXR(self):
        """A function taht displays a rectangle given w,h, x to stdout"""

        r = R(3, 2, 1, 0, 1)
        capture = DisplayMethodsR.CaptureStdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def DisplayWidthHeightYR(self):
        """A function taht displays a rectangle given w,h,y to stdout"""

        r = R(4, 5, 0, 1, 0)
        capture = DisplayMethodsR.CaptureStdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def DisplayWidthHeightXYR(self):
        """A function taht displays a rectangle given w,h,x,y to stdout"""

        r = R(2, 4, 3, 2, 0)
        capture = DisplayMethodsR.CaptureStdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def DisplayOneArgR(self):
        """A function that displays a rectangle given only 1 argument"""

        r = R(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


# Class #8
class RectangleArgs(unittest.TestCase):
    """A class that defines updating *args method for rectangle model"""

    def Pass0RArg(self):
        """A function that passes 0 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def Pass1RArg(self):
        """A function that passes 0 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def Pass2RArg(self):
        """A function that passes 2 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def Pass3RArg(self):
        """A function that passes 3 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def Pass4RArg(self):
        """A function that passes 4 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def Pass5RArg(self):
        """A function that passes 5 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def PassOver5RArg(self):
        """A function that passes over 5 attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def PassNoneRArg(self):
        """A function that passes None as attribute to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def PassNoneIDRArg(self):
        """A function that passes NOne and ID attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def PassUpdated2RArg(self):
        """A function that passes twice updated attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def PassInvalidWidthRArg(self):
        """A function that passes invalid width type attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def PassZeroWidthRArg(self):
        """A function that passes zero width type attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def PassNegWidthRArg(self):
        """A function that passes negative width type attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def PassInvalidHeightRArg(self):
        """A function that passes invalid height type attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def PassZeroHeightRArg(self):
        """A function that passes zero height attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def PassNegHeightRArg(self):
        """A function that passes negative height attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def PassInvalidXRArg(self):
        """A function that passes invalid x type attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def PassNegXRArg(self):
        """A function that passes negative x attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def PassInvalidYRArg(self):
        """A function that passes invalid y type attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def PassNegYRArg(self):
        """A function that passes negative y attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def PassWidthHeightRArg(self):
        """A function that passes width before height attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def PassWidthXRArg(self):
        """A function that passes width before x attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def PassWidthYRArg(self):
        """A function that passes width before y attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def PassHeightXRArg(self):
        """A function that passes height before x attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def PassHeightYRArg(self):
        """A function that passes height before y attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def PassXYRArg(self):
        """A function that passes x before y attributes to *args"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


# Class #9
class RectangleKwargs(unittest.TestCase):
    """A class that defines updating **kwargs method for rectangle model"""

    def Pass1RKwarg(self):
        """A function that passes 1 attribute to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def Pass2RKwarg(self):
        """A function that passes 2 attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def Pass3RKwarg(self):
        """A function that passes 3 attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def Pass4RKwarg(self):
        """A function that passes 4 attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def Pass5RKwarg(self):
        """A function that passes 5 attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def PassNoneRKwarg(self):
        """A function that passes None as attribute to **kwars"""

        r = R(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def PassNoneIDRKwarg(self):
        """A function that passes None and id as attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def PassUpdated2RKwarg(self):
        """A function that passes twice updated attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def PassInvalidWidthRKwarg(self):
        """A function that passes invalid width type attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def PassZeroWidthRKwarg(self):
        """A function that passes zero width attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def PassNegWidthRKwarg(self):
        """A function that passes negative width attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def PassInvalidHeightRKwarg(self):
        """A function that passes invalid height type attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def PassZeroHeightRKwarg(self):
        """A function that passes zero height attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def PassNegHeightRKwarg(self):
        """A function that passes negative height attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def PassInvalidXRKwarg(self):
        """A function that passes invalid x type attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def PassNegXRKwarg(self):
        """A function that passes negative x attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def PassInvalidYRKwarg(self):
        """A function that passes invalid y type attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def PassNegYRKwarg(self):
        """A function that passes negative y attributes to **kwargs"""

        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def PassArgsAndKwargsR(self):
        """A function that passes to *args and **kwargs"""

        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def PassWrongKeysRKwargs(self):
        """A function that passes wrong keys as attributes"""

        r = R(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def PassMoreWrongKeysRKwargs(self):
        """A function that passes wrong keys as attributes"""

        r = R(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


# Class #10
class RectangleTodict(unittest.TestCase):
    """A class that defines dictionary representation of rectangles"""

    def RToDictOutput(self):
        """A function that passes dictionary output"""

        r = R(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def RToDoictNoObj(self):
        """A function that passes dictionary with no object changes"""

        r1 = R(10, 2, 1, 9, 5)
        r2 = R(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def RToDictArgs(self):
        """A function that passes dictionary arguments"""

        r = R(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
