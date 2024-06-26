from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, then, when

# Define the path to the feature file and init any module variables
scenarios('../Features/user_verdict.feature')


@given('the user opens the url')
def open_url(page: Page):
    URL = 'https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a'
    yield page.goto(URL)


@given('the user clicks the start button')
def clicks_start_button(page: Page):
    page.click('text="START"')


@given('the user clicks a case study')
def clicks_case_study(page: Page):
    case1 = 'a#pa_5c9126fe3f4fb_p179d7b273e1-link--imgCard-1'
    page.click(case1)


@given('the user is ready to judge')
def is_ready_to_judge(page: Page):
    page.click('text="JUDGE THIS"')


@given('the user selects guilty')
def guilty_verdict(page: Page):
    verdict = '#pa_5c9126fe47260_p15515116385-answer-1'
    page.click(verdict)


@given('the user selects not guilty')
def guilty_verdict(page: Page):
    verdict = '#pa_5c9126fe47260_p15515116385-answer-2'
    page.click(verdict)


@when('the user votes')
def user_votes(page: Page):
    page.click('text="VOTE"')


@then('the verdict modal should display with the result "Guilty" via text on the modal.')
def verdict_modal_displays_guilty(page: Page):
    verdict_modal = '#pa_5c9126fe47260_p1554e607d21-modal__container'
    page.wait_for_selector(verdict_modal)
    expect(page.locator(verdict_modal)).to_contain_text('Guilty')


@then('the vote button is disabled')
def vote_btn_disabled(page: Page):
    button = '#pa_5c9126fe47260_p15515116385-save_button'
    expect(page.locator(button)).to_be_disabled()


@then('the vote button is enabled')
def vote_btn_enabled(page: Page):
    button = '#pa_5c9126fe47260_p15515116385-save_button'
    expect(page.locator(button)).to_be_enabled()


@then('the verdict modal should display with the result "Not Guilty" via text on the modal.')
def verdict_modal_displays_not_guilty(page: Page):
    verdict_modal = '#pa_5c9126fe47260_p1554e606f5f-modal__container'
    page.wait_for_selector(verdict_modal)
    expect(page.locator(verdict_modal)).to_contain_text('Not Guilty')

