"""Create a class describing any company. For example, Toshiba or Apple"""


class Company:
    def __init__(self, name: str, offices: list, departments: list, employees: list, products: list, turnover: int):
        self.__name = name
        self.__offices = offices
        self.__departments = departments
        self.__employees = employees
        self.__products = products
        self.__turnover = turnover

    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 10:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be a string pf length less than 10: {type(new_name)} : {len(new_name)}')

    # departmants
    @property
    def department(self):
        return self.__departments

    def add_new_department(self, new_department: str):
        self.__departments.append(new_department)

    def remove_department(self, department: str):
        if department in self.__departments:
            self.__departments.remove(department)
        else:
            raise TypeError(f'The {department} does not exist in list of departments')

    # offices
    @property
    def office(self):
        return self.__offices

    def add_new_office(self, new_office: str):
        self.__offices.append(new_office)

    def remove_office(self, office: str):
        if office in self.offices:
            self.__offices.remove(office)
        else:
            raise TypeError(f'The {office} does not exist in list of offices')

    # employees
    @property
    def employees(self):
        return self.__employees

    def add_new_employee(self, new_employee):
        if isinstance(new_employee, str):
            self.__employees.append(new_employee)
        else:
            raise TypeError(f'Name should be a string, not a {type(new_employee)}')

    def remove_employee(self, employee: str):
        if employee in self.__employees:
            self.__employees.remove(employee)
        else:
            raise TypeError(f'The {employee} does not exist in list of employees')

    # products
    @property
    def product(self):
        return self.__products

    def add_new_product(self, new_product: str):
        self.__products.append(new_product)

    def remove_products(self, product):
        if product in self.__products:
            self.__products.remove(product)
        else:
            raise TypeError(f'The {product}does not exist in list of products')

    # turnover
    @property
    def turnover(self):
        return self.__turnover

    @turnover.setter
    def turnover(self, new_turnover):
        if isinstance(new_turnover, int) and new_turnover > 0:
            self.__turnover = new_turnover
        else:
            raise TypeError(f'It is not a turnover if it is not an integer {type(new_turnover)} and less than 0')

    def find_revenue(self, taxes: int):
        return self.__turnover - ((self.__turnover * taxes) / 100)

    @classmethod
    def create_company_with_revenue(cls, name, offices, departments, employees, products, turnover, taxes):
        revenue = turnover - ((turnover * taxes) / 100)
        return cls(name, offices, departments, employees, products, revenue)

    @staticmethod
    def show_work_days():
        print('The company is open from Monday to Friday')
