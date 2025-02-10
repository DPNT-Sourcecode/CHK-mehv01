from solutions.CHK import checkout_solution


class TestCHK():
    def test_chk_3a(self):
        assert checkout_solution.checkout('AAA') == 130
    
    def test_chk_6a(self):
        assert checkout_solution.checkout('AAAAAA') == 260
    
    def test_chk_5a(self):
        assert checkout_solution.checkout('AAAAA') == 230
    
    def test_chk_abcd(self):
        assert checkout_solution.checkout('ABCD') == 115
    
    def test_chk_bbaaabbc(self):
        assert checkout_solution.checkout('BBAAABBC') == 240

    def test_chk_err(self):
        assert checkout_solution.checkout('Z') == -1

    

