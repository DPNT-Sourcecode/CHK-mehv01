from solutions.CHK import checkout_solution


class TestCHK():
    def test_chk(self):
        assert checkout_solution.checkout('AAA') == 3

