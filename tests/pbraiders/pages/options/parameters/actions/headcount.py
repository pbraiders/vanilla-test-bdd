# coding=utf-8
"""Parameters page - headcount responsability."""

from __future__ import annotations
from pbraiders.pages.options.parameters.actions import ParametersActionAbstract


FIELD_HEADCOUNT = 'pa{}'
BUTTON_MODIFY = 'update'
FAILURE_MESSAGE = "Une des valeurs n'est pas valide."
SUCCESS_MESSAGE = "Enregistrement réussi."


class HeadcountAction(ParametersActionAbstract):
    """Parameters page - headcount responsability."""

    def update(self) -> HeadcountAction:
        """Clicks the update button"""
        self.page.find_by_name(BUTTON_MODIFY).first.click()
        return self

    def fill(self, month: int, value) -> HeadcountAction:
        """Fills the headcount update field."""
        if 1 <= month <= 12:
            self.page.fill(FIELD_HEADCOUNT.format(month), value)
        else:
            raise TypeError("month is not valid!")
        return self

    def fill_all(self) -> HeadcountAction:
        """Fills the max update fields."""
        for i_month in range(1, 13, 1):
            self.page.fill(FIELD_HEADCOUNT.format(i_month), i_month)
        return self

    def check(self) -> bool:
        """Checks the headcount fields."""
        b_return = True
        for i_month in range(1, 13, 1):
            i_value = int(self.page.find_by_name(FIELD_HEADCOUNT.format(i_month)).first.value)
            b_return = (b_return is True) and (i_value == i_month)
        return b_return

    def has_failed(self) -> bool:
        """Test if the headcount update has failed"""
        return self.page.is_text_present(FAILURE_MESSAGE, wait_time=1)

    def has_succeeded(self) -> bool:
        """Test if the max update has succeded"""
        return self.page.is_text_present(SUCCESS_MESSAGE, wait_time=1)
