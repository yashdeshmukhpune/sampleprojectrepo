import pytest

class Test_dependency:

    @pytest.mark.dependency()
    def test_testcase1(self):
        print("This is testcase 1")
        assert False

    @pytest.mark.dependency(depends=['Test_dependency::test_testcase1'])
    def test_testcase2(self):
        print("This is testcase 2")

    @pytest.mark.dependency()
    def test_add_product_to_cart(self):
        assert False
        print("Product is added to cart successfully")

class Test_BuyProduct:

    @pytest.mark.dependency(depends=['Test_dependency::test_add_product_to_cart'])
    def test_buy_product(self):
        print("Product is ready for shipment")