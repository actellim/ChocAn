import unittest
from unittest.mock import patch, MagicMock
from src.terminal import Terminal
from src.mainframe import MainScheduler, Billing, ReportGenerator

class TestIntegrationWeekly(unittest.TestCase):
    @patch('src.terminal.ProviderReport')
    def test_friday_night_report(self, MockProviderReport):
        # Simulate Friday 12am
        term = Terminal()
        term.checkProviderTimer()
        
        # Should trigger ProviderReport.sum()
        MockProviderReport.return_value.sum.assert_called()

    @patch('src.mainframe.Billing.weeklyBill')
    def test_saturday_night_billing(self, mock_weekly_bill):
        # Simulate Saturday 12am
        scheduler = MainScheduler()
        scheduler.checkAcmeTimer()
        
        # Should trigger Billing
        mock_weekly_bill.assert_called()

    @patch('src.mainframe.ReportGenerator.generateWeeklyReport')
    def test_billing_triggers_reports(self, mock_gen_report):
        billing = Billing()
        billing.weeklyBill("2023-12-01")
        
        # Should trigger ReportGenerator
        mock_gen_report.assert_called()

if __name__ == '__main__':
    unittest.main()
