from seleniumbase import BaseCase
from decimal import Decimal


class CheckoutTest(BaseCase):

    def test_addOneItemToCheckout(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")

        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        text = self.get_text("//*[@id=\"sc-buy-box-ptc-button-announce\"]/div/div[1]")
        self.assertEqual("Przejdź do finalizacji zakupu (1 produkt)", text)

    def test_addTwoItemsToCheckout(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")

        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        text = self.get_text("//*[@id=\"sc-buy-box-ptc-button-announce\"]/div/div[1]")
        self.assertEqual("Przejdź do finalizacji zakupu (produktów: 2)", text)

    def test_addThreeItemsToCheckoutAndGoToCart(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")

        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath("//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/div["
                         "1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.click_xpath("//*[@id=\"nav-cart\"]")
        text = self.get_text("//*[@id=\"sc-subtotal-label-buybox\"]")
        self.assertEqual("Suma (liczba produktów: 3):", text)

    def test_addTheeItemsToCheckoutAndDeleteOneItem(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")

        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.click_xpath("//*[@id=\"nav-cart\"]")
        self.wait(0.5)
        self.click_xpath("//*[starts-with(@name,'submit.delete')]")
        self.wait(5)
        text = self.get_text("//*[@id=\"sc-subtotal-label-buybox\"]")

        self.assertEqual("Suma (liczba produktów: 2):", text)

    def test_addTheeItemsToCheckoutAndDeleteTwoItems(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")

        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.click_xpath("//*[@id=\"nav-cart\"]")
        self.wait(0.5)
        self.click_xpath("//*[starts-with(@name,'submit.delete')]")
        self.click_xpath("//*[starts-with(@name,'submit.delete')]")
        text = self.get_text("//*[@id=\"sc-subtotal-label-buybox\"]")

        self.assertEqual("Suma (1 przedmiot):", text)

    def test_addOneItemAndCheckCartAmount(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        money = self.get_text(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[3]/div[3]/div[2]/a/span")
        money = money.replace("\n", ",")
        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.click_xpath("//*[@id=\"nav-cart\"]")
        money2 = self.get_text("//*[@id=\"sc-subtotal-amount-buybox\"]/span")
        money2 = money2.replace(" ", "")

        self.assertEqual(money, money2)

    # sometimes it can take another book so cart amount can be different
    def test_addTwoItemsAndCheckCartAmount(self):
        self.open(
            "https://www.amazon.pl/s?k=harry+potter+ksi%C4%85%C5%BCka&__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid"
            "=2B55D694JRHNQ&sprefix=harry+potter+ksi%C4%85%C5%BCka%2Caps%2C117&ref=nb_sb_noss_1")
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        money = self.get_text(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[3]/div[3]/div[2]/a/span")
        money = money.replace("\n", ",")
        money = money.replace("zł", "")
        money = money.replace(",", ".")

        self.click_xpath(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/div/div/div[2]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.go_back()
        self.go_back()
        self.wait(0.5)
        self.click_xpath("//*[@id=\"sp-cc-rejectall-link\"]")
        self.wait(0.5)
        money2 = self.get_text(
            "//*[@id=\"search\"]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[2]/div[3]/div["
            "2]/a/span/span[2]")
        money2 = money2.replace("\n", ",")
        money2 = money2.replace("zł", "")
        money2 = money2.replace(",", ".")

        wholemoney = float(money) + float(money2)
        wholemoney = format(wholemoney, '.2f')
        wholemoney = str(wholemoney) + " zł"
        wholemoney = wholemoney.replace(".", ",")
        print(wholemoney)
        self.wait(0.5)
        self.click_xpath(
            "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div[1]/span/a/div/img")
        self.click_xpath("//*[@id=\"add-to-cart-button\"]")
        self.click_xpath("//*[@id=\"nav-cart\"]")
        money3 = self.get_text("//*[@id=\"sc-subtotal-amount-buybox\"]/span")
        self.assertEqual(money3, wholemoney)
