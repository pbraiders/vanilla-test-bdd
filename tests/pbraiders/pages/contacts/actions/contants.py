# coding=utf-8
"""Constants - fields names."""

__all__ = ['BUTTON_CANCEL', 'BUTTON_CONFIRM', 'BUTTON_CREATE', 'BUTTON_DELETE', 'BUTTON_UPDATE', 'FIELD_LASTNAME', 'FIELD_FIRSTNAME', 'FIELD_PHONE',
           'FIELD_EMAIL', 'FIELD_ADDRESS', 'FIELD_ADDRESS_MORE', 'FIELD_CITY', 'FIELD_ZIP', 'FIELD_COMMENT', 'MESSAGE_FAILURE', 'MESSAGE_SUCCESS']

BUTTON_CANCEL = 'can'
BUTTON_CONFIRM = 'con'
BUTTON_CREATE = 'new'
BUTTON_DELETE = 'del'
BUTTON_UPDATE = 'upd'

FIELD_LASTNAME = 'ctl'
FIELD_FIRSTNAME = 'ctf'
FIELD_PHONE = 'ctp'
FIELD_EMAIL = 'cte'
FIELD_ADDRESS = 'cta'
FIELD_ADDRESS_MORE = 'ctm'
FIELD_CITY = 'ctc'
FIELD_ZIP = 'ctz'
FIELD_COMMENT = 'ctk'

MESSAGE_FAILURE = "Le nom,le prénom et le numéro de téléphone doivent être renseignés."
MESSAGE_SUCCESS = "Enregistrement réussi."
