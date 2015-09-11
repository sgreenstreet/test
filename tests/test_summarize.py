from report_MPC_less import summarize_MPC_report

class TestClass:
    def test_1(self):
        lines = ['K6378         C2015 09 03.39479403 16 28.04 +62 22 00.4          15.72R      V37']
        expected_line = ['K6378         C2015 09 03.39479403 16 28.04 +62 22 00.4          15.7 R      V37']
        result = summarize_MPC_report(lines)
        assert result == expected_line
