"""
Unit testing module for MergeSort. Run from command line to determine passing tests.
"""
import Merge
import unittest

class TestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.acceptType = list(range(0,3))
        self.rangeType = range(0,4)
        self.stringType = 'a'*5
        self.listType = ['a']
        self.noneType = [None]

    def test_MergeType(self):
        with self.assertRaises(TypeError,msg="TypeError exception raise fail"):
            Merge.merge(self.acceptType,self.rangeType)
            Merge.merge(self.stringType,self.stringType)
        print('TypeError exception raised in merge() with incorrect iterable')

    def test_SortType(self):
        with self.assertRaises(TypeError,msg="TypeError exception raise fail"):
            Merge.Sort(self.stringType)
            Merge.Sort(self.rangeType)
            Merge.Sort(self.listType)
            Merge.Sort(self.noneType)
        print('TypeError exception raised in Sort() with incorrect iterable')

    def test_SortAscending(self):
        response = Merge.Sort(self.acceptType)
        conditions = []
        for i in range(1,len(self.acceptType)):
            conditions.append(response[i] >= response[i-1])
        self.assertTrue(all(conditions),msg="Sorted lists not ascending")
        print("Data list passes ascending sort")
    
    def test_SortDescending(self):
        response = Merge.Sort(self.acceptType)
        conditions = []
        for i in range(1,len(self.acceptType)):
            conditions.append(response[i] <= response[i-1])
        self.assertTrue(all(conditions),msg="Sorted lists not descending")
        print("Data list passes descending sort")        
    
    def test_NoneType(self):
        with self.assertRaises(IndexError,msg="Attempted to compare NoneType"):
            Merge.Sort(self.noneType)
        print("Sort() passes check for None type in list argument")
    
    def test_StrType(self):
        with self.assertRaises((IndexError,TypeError),msg="Attempted to compared string values"):
            Merge.Sort(self.stringType)
            Merge.Sort(self.listType)
        print("Sort() passes check for string types in list arguments")

if __name__=="__main__":
    unittest.main()