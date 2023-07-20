from collections import UserDict

class Field:
    pass


class Phone(Field):
    def __init__(self, phone_number: str):
        self.value = phone_number


class Name(Field):
    def __init__(self, name: str):
        self.value = name


class Record(Field):
    def __init__(self, name: Name, phones: Phone):
        self.phones = list(phones)
        self.name = name

    def add_phone(self, phone: Phone) -> None:
        self.phones.append(phone)

    def del_phone(self, phone: Phone) -> None:
        try:
            self.phones.remove(phone)

        except ValueError:
            print("You try to delete number that is absent in the list!")

    def edit_phone(self, current_phone: Phone, new_phone: Phone) -> None:
        try:
            index = self.phones.index(current_phone)
            self.phones[index] = new_phone
        except ValueError:
            print("You try to edit number that is absent in the list!")

    def show_phones(self) -> None:
        header = "|     The phone list     |"
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for phone in self.phones:
            print(f'|{phone.value:^24}|')
        print("-" * len(header))


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
