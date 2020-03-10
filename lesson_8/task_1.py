class Date:
    def __init__(self, date):
        Date._date = date

    @classmethod
    def get_int_date(cls):
        try:
            return list(map(int, cls._date.split("-")))
        except ValueError:
            print("Error format. Use: «day-month-year»")
            return [0, 0, 0]

    @staticmethod
    def is_valid(day, month, year):
        is_valid = True

        if not 0 < day <= 31:
            is_valid = False
        if not 0 < month <= 12:
            is_valid = False
        if not 0 < year:
            is_valid = False

        return is_valid


date = Date("12-11-2333")
day, month, year = date.get_int_date()
print(f"""
day:   {day}
month: {month}
year:  {year}
""")
print(f"Validation data: {date.is_valid(day, month, year)}")
