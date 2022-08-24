class TestBrowser(unittest.TestCase):
    def setUp(self) -> None:
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test05_adding_favorite_movie(self) -> None:
        self.driver.get('https://tmd_b')
        self.assertEqual(self.driver.title, 'TMD_B')
        self.driver.find_element(By.XPATH, 'movie_element').click()
        self.driver.find_element(By.XPATH, 'star_favorite_element').click()
        alert = self.driver.switchTo().alert()
        actual_result_message = self.driver.switchTo().alert().getText()
        self.assertEqual('TMDB Name of Movie added to favorites', actual_result_message)
        alert.accept()
        self.driver.find_element(By.XPATH, 'Favorite_tag').click()
        actual_result_movie_name = self.driver.find_element(By.XPATH, 'movie_element').getText()
        self.assertEqual('TMDB Name of Movie', actual_result_movie_name)




        actual_result = self.driver.find_element(By.XPATH, "//div[@class='main-header']").text
        expected_result = 'Elements'
        self.assertEqual(expected_result, actual_result)

    def tearDown(self) -> None:
        """
        Closing driver after each test
        """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()