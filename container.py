"""a module that stores only a class for
comparing the result of executing a certain function with different arguments"""

import datetime
from types import BuiltinFunctionType
from misc import F, output


class Container:
    """a class for comparing the result of executing
    a certain function with different arguments"""

    def __init__(self, func):
        if isinstance(func, BuiltinFunctionType):
            raise TypeError("the constructor accepts only functions")
        self._func = func
        self._tests = []
        self._passed = 0
        self._failed = 0
        self._count = 1

    def _progress(self, passed: bool):
        """a private method that increases the
        indicators of the number of tests,
        tests passed and failed indicators"""
        if passed:
            self._passed += 1
        else:
            self._failed += 1
        self._count += 1

    def equal(self, comparison_thing, *args, **kwargs):
        """=="""
        self._tests.append(["==", comparison_thing, args, kwargs])

    def more(self, comparison_thing, *args, **kwargs):
        """>"""
        self._tests.append([">", comparison_thing, args, kwargs])

    def less(self, comparison_thing, *args, **kwargs):
        """<"""
        self._tests.append(["<", comparison_thing, args, kwargs])

    def notequal(self, comparison_thing, *args, **kwargs):
        """!="""
        self._tests.append(["!=", comparison_thing, args, kwargs])

    def remove(self, index: int):
        """a method that removes a test from the list of scheduled tests"""
        try:
            del self._tests[index - 1]
        except IndexError as range_out:
            raise IndexError("index outside the range of the test list") from range_out

    def execution_time(self, exact: bool, *args, **kwargs):
        """shows the execution time of the function"""
        self._tests.append(["time", exact, args, kwargs])

    def test_results(self):
        """displays the current test results"""
        print(f"number of tests: {self._count - 1}")
        print(F.GREEN + f"passed: {self._passed}")
        if self._failed > 0:
            print(F.RED + f"failed: {self._failed}")
        else:
            print(f"failed: {self._failed}")
        print(F.RESET, end='')

    def start_testing(self, show_results=True):
        """runs testing on the current list and outputs the results (optional)"""
        if len(self._tests) > 0:
            for test in self._tests:
                before = datetime.datetime.now()
                result = self._func(*test[2], **test[3])
                after = datetime.datetime.now()
                match test[0]:
                    case "==":
                        output(result.__eq__(test[1]), test[1], f"test {self._count}: ")
                        self._progress(result.__eq__(test[1]))
                    case ">":
                        output(result.__gt__(test[1]), test[1], f"test {self._count}: ")
                        self._progress(result.__gt__(test[1]))
                    case "<":
                        output(result.__lt__(test[1]), test[1], f"test {self._count}: ")
                        self._progress(result.__lt__(test[1]))
                    case "!=":
                        output(result.__ne__(test[1]), test[1], f"test {self._count}: ")
                        self._progress(result.__ne__(test[1]))
                    case "time":
                        sec = (after - before).total_seconds()
                        if test[1]:
                            print(F.YELLOW + f"execution time: {int(sec * 1000000)} microseconds")
                        else:
                            print(F.YELLOW + f"execution time: {round(sec, 1)} seconds")
                        print(F.RESET, end='')

        if show_results:
            self.test_results()
