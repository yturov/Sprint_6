from selenium.webdriver.common.by import By


class StartPageLocators:
    INSCRIPTION_QUESTION_IMPORTANT = (By.XPATH, "//div[text()='Вопросы о важном']")  # Надпись "Вопросы о важном"
    QUESTION = (By.ID, "accordion__heading-{}")  # Вопрос
    ANSWER = (By.ID, "accordion__panel-{}")  # Ответ

