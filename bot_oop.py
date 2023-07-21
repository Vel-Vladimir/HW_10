from collections import UserDict


class Phone:
    def __init__(self, phone_number: str):
        self.value = phone_number

    def __str__(self):
        return self.value


class Name:
    def __init__(self, name: str):
        self.value = name

    def __str__(self):
        return self.value


class Record:
    def __init__(self, name: Name, *phones: Phone):
        self.phones = list(set(phones))
        self.name = name

    def __str__(self):
        return f'Record({self.name}, {[ph.value for ph in self.phones]})'

    def add_phone(self, phone_to_add: Phone):
        for exist_phone in self.phones:
            if phone_to_add.value == exist_phone.value:
                return f"You try to add phone {phone_to_add} that already exists"
        self.phones.append(phone_to_add)

    def del_phone(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f"You try to delete number {phone} that is absent in the list!"

    def edit_phone(self, current_phone: Phone, new_phone: Phone):
        try:
            index = self.phones.index(current_phone)
            self.phones[index] = new_phone
        except ValueError:
            return f"You try to edit number {current_phone} that is absent in the list!"


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
