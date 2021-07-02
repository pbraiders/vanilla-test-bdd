# coding=utf-8
"""Event page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages.events import EventPageAbstract

TITLE = 'PBRaiders - {date} - {lastname} {firstname}'
HEADER = '{date} - {lastname} {firstname}'
DAY_LIST_LOCATOR = "//*/text()[normalize-space(.)='{date}']/.."
EVENT_LIST_LOCATOR = "//*[contains(text(),'{lastname} {firstname} • {phone}')]/.."


class EventPage(EventPageAbstract):
    """Event page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        if self.event is None:
            raise TypeError("Event is not set!")
        s_date_name = self.event.date.date_name()
        s_title = TITLE.format(date=s_date_name, lastname=self.contact.lastname, firstname=self.contact.firstname)
        s_header = HEADER.format(date=s_date_name, lastname=self.contact.lastname, firstname=self.contact.firstname)
        return (self.page.title.lower() == s_title.lower()) and (self.page.find_by_tag('h1').first.text.lower() == s_header.lower())

    def visit(self) -> bool:
        """Goes to the page."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        if self.event is None:
            raise TypeError("Event is not set!")
        try:
            self.page.visit(urljoin(str(self.config['home']), str(self.config['calendar'])))
            self.page.find_by_xpath(DAY_LIST_LOCATOR.format(date=self.event.date._day)).first.click()
            self.page.find_by_xpath(EVENT_LIST_LOCATOR.format(lastname=self.contact.lastname,
                                                              firstname=self.contact.firstname,
                                                              phone=self.contact.tel)).first.click()
        except Exception:
            return False

        return self.on_page()
