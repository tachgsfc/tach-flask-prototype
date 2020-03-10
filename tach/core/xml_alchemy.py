import lxml.etree
from sqlalchemy.types import UserDefinedType


class XMLType(UserDefinedType):

    def get_col_spec(self, **kw):
        return 'XML'

    def process_bind_param(self, value, dialect):
        return lxml.etree.tostring(value)

    def process_result_value(self, value, dialect):
        return lxml.etree.fromstring(value)
