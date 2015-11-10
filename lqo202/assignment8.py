"""
This part generates the results, it launches an small interfase where the user has to write what to do, whenever a result
is launched, it returns to the main window.
Exception handling and input validation is done for each part.
"""

import investment as s1
from investment import ExceptionInvestment

__author__ = 'lqo202'


##### Previous functions to validate input, handle exceptions and launch the result####
def printingresults1():
    print 'Simulation with user input'
    while True:
        try:
            numtrialsinput = int(raw_input('Enter an integer, number of trials (simulations) if it is a float, integer part will be used: '))
            positionsinput = map(int,raw_input('Enter positions (only 4) separated by commas: ').split(","))
            if (isinstance(positionsinput, list) and len(positionsinput) == 4):
                try:
                    results1 = s1.investment.calculatepositionssimulation(positionsinput, numtrialsinput)
                except:
                    raise AttributeError
                    print "Values not in accepted ones! Just 1,10,100 or 1000"
                else:
                    print 'Processing...'
                    print results1
                    mainwindow()
            elif isinstance(positionsinput, list) and len(positionsinput) !=4:
                raise AttributeError
                print 'Not 4 elements! Just write 4 elements'
            else:
                raise AttributeError
                print "Not a list"
        except ExceptionInvestment:
            print 'Not an investment class'
        except ValueError:
            print "Oops!  That was no valid input.  Try again!"
        except KeyboardInterrupt:
            print 'Keyboard interrupted, try again!'
        except ArithmeticError:
            print 'ArithmeticError ocurred'
        except LookupError:
            print 'LookupError ocurred'
        except AttributeError:
            print 'Attribute error. Values inputted not of the type specified, try again!'

def printingresults2():
    print 'Simulation by default, processing...'
    while True:
        try:
            resultsdefault = s1.investment.generategraphicsandstats()
            print resultsdefault
            print 'Results generated'
            mainwindow()
        except KeyboardInterrupt:
            print 'Keyboard interrupted, try again!'
        except ArithmeticError:
            print 'ArithmeticError ocurred'
        except LookupError:
            print 'LookupError ocurred'

############## Final screening of results #########
def mainwindow():
    print 'Investment Tool: Assignment 8 - Programming for Data Science'
    while True:
        try:
             optionuser = raw_input('Menu: Press 1 to choose values for simulation , press 2 for simulation by default, q for exit   :')
             if optionuser == 'q': break
             else:
                 optionuser = int(optionuser)
                 captureanswernotq(optionuser)
        except ValueError:
            print "Oops!  That was no valid input.  Try again!"
        except KeyboardInterrupt:
            print 'Keyboard interrupted, try again!'


def captureanswernotq(answer):
    try:
        if answer==1:  printingresults1()
        if answer==2:  printingresults2()
        else:
            raise ValueError
    except ValueError:
        print "Oops!  That was no valid input.  Try again!"
    except KeyboardInterrupt:
        print 'Keyboard interrupted, try again!'


if __name__ == "__main__":
    try:
        mainwindow()
    except EOFError:
        pass
