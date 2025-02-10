from solutions.CHK import checkout_solution


class TestCHK():
    def test_chk_3a(self):
        assert checkout_solution.checkout('AAA') == 130
    
    def test_chk_6a(self):
        assert checkout_solution.checkout('AAAAAA') == 250
    
    def test_chk_5a(self):
        assert checkout_solution.checkout('AAAAA') == 200

    def test_chk_8a(self):
        assert checkout_solution.checkout('AAAAAAAA') == 330
    
    def test_chk_abcd(self):
        assert checkout_solution.checkout('ABCD') == 115
    
    def test_chk_bbaaabbc(self):
        assert checkout_solution.checkout('BBAAABBC') == 240

    def test_chk_eb(self):
        assert checkout_solution.checkout('EB') == 70

    def test_chk_eeb(self):
        assert checkout_solution.checkout('EEB') == 80
    
    def test_chk_eebb(self):
        assert checkout_solution.checkout('EEBB') == 110
    
    def test_chk_bbeebb(self):
        assert checkout_solution.checkout('BBEEBB') == 155

    def test_chk_err(self):
        assert checkout_solution.checkout('Z') == -1

    



