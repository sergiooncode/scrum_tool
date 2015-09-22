from selenium import webdriver
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_sprint_board_and_retrieve_it_later(self):
        # Johnny has heard about a cool new agile scrum tool. He goes
        # to check out its Index Page
        self.browser.get('http://localhost:8000/')

        # He notices the page title mentions "Agile Scrum"
        # which the methodology he was looking for.
        self.assertIn('Agile Scrum', self.browser.title)

        # On the Login Page (also Index Page) he is invited to
        # submit valid username and password to login and access his own
        # Board Homepage.
        usernamebox = self.browser.find_element_by_id('id_username')
        passwordbox = self.browser.find_element_by_id('id_password')
        self.assertEqual(
            usernamebox.get_attribute('name'), 'username'
        )
        self.assertEqual(
            passwordbox.get_attribute('name'), 'password'
        )

        # He logs in with a valid username and password and clicks
        # the submit button
        submitbutton = self.browser.find_element_by_id('id_submit')
        usernamebox.send_keys('demo')
        passwordbox.send_keys('test')
        submitbutton.click()
        # time.sleep(5)

        # Once he is logged in appropriately and he is shown the Board
        # Page with the message showing "Welcome to your Agile Scrum Board!"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to your Agile Scrum Board!', header_text)

# Also he is invited to create a sprint straight away by
# showing an "Add Sprint" button which upon hitting shows a
# form with 3 text boxes to enter Sprint name, Description and
# End Date respectively

# He types "User login", "As a user I want to login to get
# access to my AS board" and "2015-03-10" into the 3 text
# boxes respectively.

# When he hits the "Create" button shown below the 3-text-box
# form, that form disappears and a box with the Sprint details
# is shown below the "Add Sprint" button which reappears.

# More sprints can be created using that same procedure.

# Johnny wonders whether the site will remember his sprints. Then he sees
# that the site has generated a unique URL for him -- there is some explanatory
# text to that effect somewhere on the page.

# A while later he visits that URL and his sprints are still there.

if __name__ == 'main':
    unittest.main(warnings='ignore')