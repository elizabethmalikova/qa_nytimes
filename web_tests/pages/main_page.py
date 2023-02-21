from playwright.sync_api import Page, expect, TimeoutError

community_options = "//a[contains(text(),'Community')]"
tools_button = "//a[@data-testid='ToolsClick']"
tools = "//span[@id='service-name-trending']"
more_button = "//a[@class='trending-tab-load-more-services btn btn-ss-alt btn-lg']"
description_button = "text=Description"


class MainPage:

    def __init__(self, page: Page):
        self.page = page

    def check_tool(self, name_tool):
        self.page.click(community_options)
        self.page.click(tools_button)
        expect(self.page.locator(tools, has_text=name_tool)).to_be_visible(timeout=5000)
        self.page.locator(tools, has_text=name_tool).click()
        return self
