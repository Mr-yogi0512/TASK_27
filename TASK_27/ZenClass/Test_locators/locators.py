class test_locators:
   url = 'https://www.zenclass.in/login'
   Email = 'email'
   Password = 'password'
   Login_button = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'
   Profile_image = '//*[@id="root"]/nav/div/div/div/span/img'
   Logout_button = '//*[@id="root"]/nav/div/div/div/div/button[2]'
   No_user = '//form/div[text()="No User Available with this credentials"]' 
   valid_email = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/div/div/p'
   Wrong_password = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[3]/span'
   No_valid_email_expected = ' Enter a valid Email'