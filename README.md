
# UNITEX
	a simple library for simple unix test 
![Unitex logo](https://sun9-27.userapi.com/impg/4hwGOqPYZtY-Bgb3mPf1h5G82kJ09iqPN7Qbng/EpvF9TF-32Y.jpg?size=500x500&quality=95&sign=e9ed9a228245be8e99f80312a66d83d1&type=album)
---
### Classes:
* **Container**
* **Comparison**
___
## Container
**args:**
*accepts a single mandatory argument, which must be of the type `function`*
* *func* - function for testing

**testing methods:**
> add the *test* to the *list of tests* for further work
* *equal(...)*
* *more(...)*
* *less(...)*
* *notequal(...)*
	 * comparison_thing
	 * *args
	 * \**kwargs

*all **testing methods** take as the first argument the value with which the result of the execution of the function under test will be compared. the remaining arguments will be accepted by the function under test*

**other testing methods:**
* *execution_time(~~self,~~ exact, *\*args, \*\*kwargs)** - calls the function under test and outputs its execution time
	* exact : boolean - if `True` then the time will be output in *microseconds*, otherwise the time will be output in *seconds rounded to one decimal place*
	* *args, \**kwargs - arguments of the function under test

**other methods:**
* *remove(index)* - removes a *test* from the *list of tests* by its index (it is important that the numbering in the ***list*** **starts with 1**, not 0)
* *start_testing(~~self,~~ show_results=`True`)* - starts testing by going through the current *list of tests*
	* show_results (*optional*) - if `True"`, the ***test_results*** method will be called at the end
* *test_results(~~self~~)* - displays the current test result, showing the number of: tests, passed tests and failed tests

### example of using the *Container* class:

    from container import Container

	def test(a, b):  # function for testing
    return a + b  # return of the sum of a and b

	tester = Container(test)  # creating instance of Container class
	tester.equal(5, 2, 3)  # comparison of 5 and sums of 2 and 3
	tester.more(12, 4, 5)  # checking whether the sum of 4 and 5 is greater than 12
	tester.notequal(5, 2, 2)  # checking whether the sum of 2 and 2 is not equal 12
	tester.start_testing()  # running the test

### output:
![test results](https://i.ibb.co/ykWDxsc/test-results.png)
## Comparison
**args:**
*does not require any arguments*

**testing decorators:**
> a function wrapped in a decorator at the end of its execution will output the result of comparing the function operation with the comparison argument
* *equal(...)*
* *more(...)*
* *less(...)*
* *notequal(...)*
	 * comparison_thing
	 * note (*optional*)

*all **decorators** take as the first mandatory argument the value with which the result of the function execution will be compared. The second optional argument takes a string to formalize the output of the test result*

### example of using the *Comparison* class:

    from comparison import Comparison  

	tester = Comparison()  # creating instance of Comparison class
    
	@tester.equal(4)  # function for testing
	def test1(a, b):  
	    return a + b  

	@tester.more(5, "test ???2: ")  # function for testing
	def test2(c, d):  
	    return c - d

	@tester.notequal(23)  # function for testing
	def test3(e, f, g):  
	    e + f - g  
    
    # comparisons:
	test1(2, 3)  
	test2(12, 4)  
	test3(16, 17, 10)
### output:
![enter image description here](https://i.ibb.co/nPztKjt/test2.png)
![4DCube logo](https://sun9-67.userapi.com/impg/6PWraq8KL-5xGN6ykSFxD69mG9V0yT0jfDlg5Q/DTcageIy3rU.jpg?size=667x627&quality=95&sign=30127eac716e0a741413334ae366b888&type=album)
