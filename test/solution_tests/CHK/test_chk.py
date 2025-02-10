from solutions.CHK import checkout_solution


class TestCHK():
    #CHK_R1
    def test_chk_err(self):
        assert checkout_solution.checkout('z') == -1

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

    #CHK_R2
    def test_chk_abcde(self):
        assert checkout_solution.checkout('ABCDE') == 155
    
    def test_chk_eb(self):
        assert checkout_solution.checkout('EB') == 70

    def test_chk_eeb(self):
        assert checkout_solution.checkout('EEB') == 80
    
    def test_chk_eebb(self):
        assert checkout_solution.checkout('EEBB') == 110
    
    def test_chk_bbeebb(self):
        assert checkout_solution.checkout('BBEEBB') == 155

    def test_chk_EEEEBB(self):
        assert checkout_solution.checkout('EEEEBB') == 160
        
    #CHK_R3
    def test_chk_F(self):
        assert checkout_solution.checkout('F') == 10
    
    def test_chk_FF(self):
        assert checkout_solution.checkout('FF') == 20
    
    def test_chk_FFF(self):
        assert checkout_solution.checkout('FFF') == 20
    
    def test_chk_FFFFFF(self):
        assert checkout_solution.checkout('FFFFFF') == 40
    
    def test_chk_ABCDEFF(self):
        assert checkout_solution.checkout('ABCDEFF') == 175

    #CHK_R4
    def test_chk_P(self):
        assert checkout_solution.checkout('P') == 50

    def test_chk_PPPPP(self):
        assert checkout_solution.checkout('PPPPP') == 200

    def test_chk_UUU(self):
        assert checkout_solution.checkout('UUU') == 120
    
    def test_chk_UUUU(self):
        assert checkout_solution.checkout('UUUU') == 120

    #CHK_R5
    def test_chk_STX(self):
        assert checkout_solution.checkout('STXXX') == 45