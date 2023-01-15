import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import AttachmentType


@allure.tag("test")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kkozhevnikov")
@allure.feature("Задачи в репозитории")
@allure.story("Тест без шагов")
@allure.link("https://github.com", name="Testing")
def test_git():
    browser.open("https://github.com")
    browser.driver.maximize_window()
    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    s(by.partial_text("#76")).should(be.visible)


@allure.tag("test")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "kkozhevnikov")
@allure.feature("Задачи в репозитории")
@allure.story("Тест с лямбда шагами")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()
    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)
    with allure.step("Делаем финальный скриншот"):
        allure.attach(browser.driver.get_screenshot_as_png(), name="Final_step", attachment_type=AttachmentType.PNG)


@allure.tag("test")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "kkozhevnikov")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста с декоратором")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
