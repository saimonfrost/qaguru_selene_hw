from selene import browser, have, be


def test_fill_all_form():
    browser.open('/')

    browser.element('#firstName').should(be.blank).type('Semen')
    browser.element('#lastName').should(be.blank).type('Fedorov')
    browser.element('#userEmail-wrapper #userEmail').should(be.blank).type('fedorovedorov@gmail.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').should(be.blank).type('8811656731')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').should(be.visible).element('option[value="10"]').click()
    browser.element('[class="react-datepicker__year-select"]').should(be.visible).element('option[value="2023"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--009"]').click()
    browser.element('#subjectsInput').type('Ma').press_enter()
    browser.element('[class="css-12jo7m5 subjects-auto-complete__multi-value__label"]').should(have.text('Maths'))



