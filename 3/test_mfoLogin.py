from seleniumbase import BaseCase


class LoginTest(BaseCase):

    # def test_getInMensClothes(self):
    #     self.open("https://www.zalando.pl/mezczyzni-home/")
    #     self.click_xpath(
    #         "//*[@id=\"z-navicat-header-root\"]/header/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/nav/ul/li["
    #         "3]/span/a/span")
    #     self.assertEqual(self.get_current_url(), "https://www.zalando.pl/odziez-meska/")
    #
    # def test_getInMensClothesAndSelectMark(self):
    #     self.open("https://www.zalando.pl/mezczyzni-home/")
    #     self.click_xpath(
    #         "//*[@id=\"z-navicat-header-root\"]/header/div[1]/div/div/div/div[1]/div/div/div/div[2]/div[2]/nav/ul/li["
    #         "3]/span/a/span")
    #     self.click_xpath("//*[@id=\"collection_view_catalog-filters\"]/div[2]/div[2]/div/button/span")
    #     self.select_option_by_index("//*[@id=\"collection_view_catalog-filters\"]/div[2]/div[2]/div/button/span", 2)
    #     clown = self.click_xpath("/html/body/div[11]/div/div[3]/div/form/div/div[1]/div/div/div[1]")
    #     self.click("/html/body/div[12]/div/div[3]/div/form/div/div[1]/div/div/div[1]")
    #     self.assertNotEqual("/html/body/div[11]/div/div[3]/div/form/div/div[1]/div/div/div[1]", clown)

    def test_loginOnly(self):
        self.open("https://old.my-fantasy.net/start/")
        # self.click_xpath()
        # self.input()
        self.send_keys(
            "body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > form > input[type=text]:nth-child(2)",
            "adi")
        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/input[2]")
        text = self.get_text("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td")
        self.assertEqual(text, "Nieprawidłowy login lub hasło")

    def test_passwordOnly(self):
        self.open("https://old.my-fantasy.net/start/")
        # self.click_xpath()
        # self.input()
        self.send_keys(
            "body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > form > input[type=password]:nth-child(5)",
            "adi")

        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/input[2]")
        text = self.get_text("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td")
        self.assertEqual(text, "Nieprawidłowy login lub hasło")

    def test_passwordAndLogin(self):
        self.open("https://old.my-fantasy.net/start/")
        # self.click_xpath()
        # self.input()
        self.send_keys(
            "body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > form > input[type=password]:nth-child(5)",
            "adi")
        self.send_keys(
            "body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > form > input[type=text]:nth-child(2)",
            "adix")

        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/input[2]")
        text = self.get_text("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td")
        self.assertEqual(text, "Nieprawidłowy login lub hasło")

    def test_passwordAndLoginWithRememberButton(self):
        self.open("https://old.my-fantasy.net/start/")
        # self.click_xpath()
        # self.input()
        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/input[1]")
        self.send_keys(
            "body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > form > input[type=password]:nth-child(5)",
            "adi")
        self.send_keys(
            "body > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(2) > td > form > input[type=text]:nth-child(2)",
            "adix")
        val = self.get_property_value("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/input[1]", 1)
        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/input[2]")
        self.assertEqual("", val)

    def test_forgotPassword(self):
        self.open("https://old.my-fantasy.net/start/")

        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/a[1]")
        url = self.get_current_url()
        self.assertEqual("https://old.my-fantasy.net/start/lost_password.php", url)

    def test_forgotPasswordWithWrongEmailFormat(self):
        self.open("https://old.my-fantasy.net/start/")

        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/a[1]")
        self.send_keys("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/input[1]", "aaaa")
        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/input[2]")
        text = self.get_text("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]")
        text2 = "Przypomnienie hasła\n\nPodany e-mail jest nieprawidłowy.\n \n \n \n \n \n \n \n \n" \
                " "
        self.assertEqual(text, text2)

    def test_forgotPasswordWithWrongEmail(self):
        self.open("https://old.my-fantasy.net/start/")

        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td/form/center/a[1]")
        self.send_keys("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/input[1]", "aaaa@gmail.com")
        self.click_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/form/input[2]")
        text = self.get_text("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]")
        text2 = "Przypomnienie hasła\n\nNie znaleziono takiego adresu e-mail w bazie danych.\n \n \n \n \n \n \n \n \n" \
                " "
        self.assertEqual(text, text2)
