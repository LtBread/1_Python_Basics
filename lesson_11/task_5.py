class Storage:
    def __init__(self):
        self._adopted = []

    def __str__(self):
        return f'{self._adopted}'

    def reception(self, *equipments):
        for equipment in equipments:
            self._adopted.append(equipment)
        return self._adopted

    def transfer(self, subdivision, *equipments):
        for equipment in equipments:
            if not equipment in self._adopted:
                raise Exception('запрашиваемой техники нет на складе')
            subdivision.equipment_list.append(equipment)
            self._adopted.remove(equipment)
        return self._adopted


class Subdivisions:
    def __init__(self):
        self._equipment = []

    def __str__(self):
        return f'{self._equipment}'

    @property
    def equipment_list(self):
        return self._equipment


class Ofm(Subdivisions):
    pass


class Pro(Subdivisions):
    pass


class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f'{self.brand} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, brand, model, printer_type, format_print):
        super().__init__(brand, model)
        self.printer_type = printer_type
        self.format_print = format_print


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, optical_density):
        super().__init__(brand, model)
        self.optical_density = optical_density


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, copy_speed):
        super().__init__(brand, model)
        self.copy_speed = copy_speed


if __name__ == '__main__':
    printer = Printer('HP', 'LaserJet Pro p1102', 'Laser', 'A4')
    scanner = Scanner('Canon', 'Canonscan LIDE400', '4800x4800dpi')
    xerox = Xerox('Xerox', 'WorkCentre B205NI', '30 page/min')
    storage = Storage()
    storage.reception(xerox, printer, scanner)
    print(storage)
    pro = Pro()
    storage.transfer(pro, xerox)
    print(storage)
    print(pro)
    ofm = Ofm()
    storage.transfer(ofm, scanner, printer)
    print(storage)
    print(ofm)
