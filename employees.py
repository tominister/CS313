"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Haoran Fang and Kevin Yu, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: hf5829
UT EID 2: kjy355
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """
    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = max(0, min(INITIAL_PERFORMANCE, 100))
        self.happiness = max(0, min(INITIAL_HAPPINESS, 100))
        self.salary = salary
    @property
    def name(self):
        """
        name?
        """
        return self.__name

    @property
    def manager(self):
        """
        manager?
        """
        return self.__manager
    def interact(self, other):
        """
        Employee interacts with another employee
        """
        if other.name in self.relationships and self.relationships[other.name]\
            >=RELATIONSHIP_THRESHOLD:
            self.happiness+=1                
        else:
            self.relationships[other.name]=0
            if self.happiness>=HAPPINESS_THRESHOLD and other.happiness>=HAPPINESS_THRESHOLD:
                self.relationships[other.name]+=1
            else:
                self.relationships[other.name]-=1
                self.happiness-=1
        self.happiness = max(0, min(self.happiness, 100))
    def daily_expense(self):
        """
        Daily expense
        """
        self.happiness-=1
        self.savings-=DAILY_EXPENSE
    def __str__(self):
        return (f"{self.__name}\n"
            f"\tSalary: ${self.salary}\n"
            f"\tSavings: ${self.savings}\n"
            f"\tHappiness: {self.happiness}%\n"
            f"\tPerformance: {self.performance}%")
    @abstractmethod
    def work(self):
        """
        missy elliot-work it
        """
        pass


class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """
    def work(self):
        performance_change=random.randint(-5,5)
        if self.performance+performance_change<0:
            self.performance=0
        elif self.performance+performance_change>100:
            self.performance=100
        else:
            self.performance+=performance_change
        self.performance = max(0, min(self.performance, 100))
        if performance_change<=0:
            self.happiness-=1
            for name in self.relationships:
                self.relationships[name]-=1
        else:
            self.happiness+=1
        self.happiness = max(0, min(self.happiness, 100))


class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """
    def work(self):
        performance_change=random.randint(-15,15)
        if self.performance+performance_change<0:
            self.performance=0
        elif self.performance+performance_change>100:
            self.performance=100
        else:
            self.performance+=performance_change
        if performance_change<=0:
            self.happiness-=2
        else:
            self.happiness+=1
        self.happiness = max(0, min(self.happiness, 100))
    def interact(self, other):
        super().interact(other)
        if other==self.manager:
            if other.happiness>=HAPPINESS_THRESHOLD and self.performance\
                >=TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD:
                self.savings+=MANAGER_BONUS
            elif other.happiness<=HAPPINESS_THRESHOLD:
                self.salary=self.salary//2
                self.happiness-=5
                if self.salary==0:
                    self.is_employed=False
        self.happiness = max(0, min(self.happiness, 100))


class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
    def work(self):
        performance_change=random.randint(-10,10)
        if self.performance+performance_change<0:
            self.performance=0
        elif self.performance+performance_change>100:
            self.performance=100
        else:
            self.performance+=performance_change
        if performance_change>=0:
            self.happiness+=1
        self.happiness = max(0, min(self.happiness, 100))
    def interact(self, other):
        super().interact(other)
        if other==self.manager:
            if other.happiness>=HAPPINESS_THRESHOLD and self.performance\
                >PERM_EMPLOYEE_PERFORMANCE_THRESHOLD:
                self.savings+=MANAGER_BONUS
            elif other.happiness<=HAPPINESS_THRESHOLD:
                self.happiness-=1
        self.happiness = max(0, min(self.happiness, 100))
