# Lab: 42 - Pythonisms

### Project: Pythonisms
### Author: Alejandro Rivera

---

* Implements the following generators on a linked list: 
  * overwrites the dunder `__iter__` method
  * adds the ability to use a `for in` loop to iterate through a linked list.
  * overwrites the dunder `__len__` method
  * adds the ability to check the length of a linked list. 
  
* Creates the following decorators: 
  * `display_result` renders text to indicate the result of a function
  * `function_timer` calculates the time spent in a function
    
#### Setup
* Install dependencies in a venv
  * run: pip install -r requirements.txt
* Dependencies:
  * [requirements.txt](requirements.txt) 

#### Run Decorators 

* **run:** python3 decorators.py

#### Tests

* [test_generators.py](test_generators.py)
* **run:** pytest test_generators.py
