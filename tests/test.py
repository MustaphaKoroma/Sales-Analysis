import unittest
import analysis

class TestSalesAnalysis(unittest.TestCase):

    def testTotalDailySales(self):
        self.assertEqual(analysis.TotalDailySales, [32, 35, 25, 55])

    def testHighestSales(self):
        self.assertEqual(analysis.HighestSales, 55)

    def testLowestSales(self):
        self.assertEqual(analysis.LowestSales, 25)

    def testHighestDay(self):
        self.assertEqual(analysis.HighestDay, 4)

    def testLowestDay(self):
        self.assertEqual(analysis.LowestDay, 3)

    def testOverallAverage(self):
        self.assertEqual(analysis.OverallAverage, 36.75)

    def testTrendingUpward(self):
        self.assertTrue(analysis.TrendingUpward)
      
if __name__ == "__main__":
    unittest.main()
  
