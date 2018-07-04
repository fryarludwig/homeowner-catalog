import dateparser


class DateConverter:
    regex = r'[0-9]{4}[-/][0-9]{2}[-/][0-9]{2}'

    def to_python(self, value):
        return dateparser.parse(value)

    def to_url(self, value):
        return '%04d-%02d-%02d' % value
