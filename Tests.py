from Page import Downloads


def test_check_message(browser):
    main_page = Downloads(browser)
    main_page.go_to_site()
    assert browser.current_url == 'https://demoqa.com/', 'Сайт https://demoqa.com/ не открыт'
    main_page.click_on_the_elements()
    assert browser.current_url == 'https://demoqa.com/elements', 'Страница https://demoqa.com/elements не открыта'
    main_page.click_on_the_checkbox()
    assert browser.current_url == 'https://demoqa.com/checkbox', 'Страница https://demoqa.com/checkbox не открыта'
    check_box = main_page.click_on_the_home_directory()
    assert check_box == True, 'Директория Home не раскрыта'
    check_box1 = main_page.click_on_the_downloads_directory()
    assert check_box1 == True, 'Директория Downloads не раскрыта'
    main_page.click_on_the_downloads()
    main_page.click_on_the_wordfile()
    message = main_page.check_message()
    assert message == True, 'message is`not true'
