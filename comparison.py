"""a module that stores only a class with decorators for comparison"""

from misc import output


class Comparison:
    """the class contains decorators for comparing
     the result of the function execution"""

    @staticmethod
    def equal(comparison_thing, note="test: "):
        """=="""

        def wrapper(function):
            def subwrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                output(result.__eq__(comparison_thing), result, note)

            return subwrapper

        return wrapper

    @staticmethod
    def more(comparison_thing, note="test: "):
        """>"""

        def wrapper(function):
            def subwrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                output(result.__gt__(comparison_thing), result, note)

            return subwrapper

        return wrapper

    @staticmethod
    def less(comparison_thing, note="test: "):
        """<"""

        def wrapper(function):
            def subwrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                output(result.__lt__(comparison_thing), result, note)

            return subwrapper

        return wrapper

    @staticmethod
    def notequal(comparison_thing, note="test: "):
        """!="""

        def wrapper(function):
            def subwrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                output(result.__ne__(comparison_thing), result, note)

            return subwrapper

        return wrapper
