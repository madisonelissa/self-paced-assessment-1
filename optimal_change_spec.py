from optimal_change import optimal_change
import unittest

class change(unittest.TestCase):
    def test_func(self):
        pass
    
    def test_returns_val(self):
        """Tests func returns value"""
        self.assertIsNotNone(optimal_change(0, 0))
        
    def test_change1(self):
        """Tests func returns correct change on test value 1"""
        self.assertEqual(optimal_change(62.13, 100), 'The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, 2 pennies.')
        
    def test_change2(self):
        """Tests func returns correct change on test value 2"""
        self.assertEqual(optimal_change(31.51, 50), 'The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, 4 pennies.')
        
    def test_change3(self):
         """Tests func returns "No change necessary" on test value 3"""
         self.assertEqual(optimal_change(100.25, 100.25), 'No change necessary.')
         
    def test_change3(self):
         """Tests func returns correct change on test value 4"""
         self.assertEqual(optimal_change(8.56, 10), 'The optimal change for an item that costs $8.56 with an amount paid of $10 is 1 $1 bill, 1 quarter, 1 dime, 1 nickel, 4 pennies.')
         
    def test_change3(self):
         """Tests func returns correct change on test value 5"""
         self.assertEqual(optimal_change(1.25, 2), 'The optimal change for an item that costs $1.25 with an amount paid of $2 is 3 quarters.')

if __name__ == "__main__":
    unittest.main()