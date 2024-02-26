class Employee: 

  def __init__(self, name: str, salary_per_day: int):
        self.name = name
        self.salary_per_day = salary_per_day
    
  def __str__(self) -> str:
     return f'Employee: {self.name}'

  def work(self) -> str:
   return 'I come to the office'

  def dict_my(self) -> dict:
    dict_my1 = {self.name: self.salary_per_day}
    return dict_my1


class Recruiter(Employee):
  def __init__(self, name: str, salary_per_day: int):
   return super().__init__(name, salary_per_day)

  def __str__(self) -> str:
   return f'Recruiter: {self.name}'


  def work(self) -> str :
   return super().work() + f' and start to hiring'


class Developer(Employee):
  def __init__(self, name: str, salary_per_day: int):
     return super().__init__(name, salary_per_day)

  def work(self) -> str:
   return super().work() + f' and start to coding'

  def __str__(self) -> str:
   return f'Developer: {self.name}'

#creation of objects 
developer1 = Developer('Max', 1000)
developer2 = Developer('Vasya', 2)
recruiter2 = Recruiter('Bob', 10)

dict_common = Developer.dict_my(developer1) | Recruiter.dict_my(recruiter2) | Developer.dict_my(developer2)


print(developer1.work())
print(recruiter2.work())
print(developer2.work())
print(developer1)
print(developer2)
print(recruiter2)

employee_with_max_salary = max(dict_common, key = dict_common.get)
max_salary = max(dict_common.values()) 

print(f'The biggest salary in this company is {max_salary}')
print(f'{employee_with_max_salary} has the biggest salary  in this company. If you develop your skills your salary also will rise! Good luck.')
