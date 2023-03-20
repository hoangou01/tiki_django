from datetime import  date , datetime
class RegexConverter:
    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


class CodeConverter(RegexConverter):
    regex = f'[A-Za-z0-9]'
class StringAndNumberPathConverter(RegexConverter):
    regex = '^[a-zA-Z0-9_.-]'

class StringPathConverter(RegexConverter):
    regex = '[^/]+'
class IntPathConverter(RegexConverter):
    regex = '[0-9]+'


class DateConverter:
    regex = r"\d{4}-\d{1,2}-\d{1,2}"
    format = "%Y-%m-%d"

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: date) -> str:
        return value.strftime(self.format)