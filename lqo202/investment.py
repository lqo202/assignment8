"""
ASSIGNMENT 8: CLASS
This script contains the class and the functions (as static methods) used to solve the Assignment.
The investment class is a subclass of numpy, because the functions work with arrays in most cases.
A new class Exception is created to handle input validation.
Details of each function can be found in the beginning of them
"""

__author__ = 'Luisa Quispe O.: lqo202'

import numpy as np
import matplotlib.pyplot as plt
import functools

class ExceptionInvestment:
    def __init__(self, msg):
        self.msg = msg

class investment():

    def __init__(self):
        self._array

    #This part of the code was modified from the original in stackoverflow#
    def __getattr__(self, attributematrix):
        try:
            return getattr(self._array, attributematrix)
        except AttributeError:
            f = getattr(np, attributematrix, None)
            if hasattr(f, '__call__'):
                return functools.partial(f, self._array)
            else:
                raise AttributeError(attributematrix)


    @staticmethod
    def calculatesimulation(position, numtrials):
        """
        This function gives as result the simulation of one position
        THe logic used was the following:
            First it calculates the position value of the investment.After that generates the random numbers and the
            gains in each of the simulations and for each position (in a loop).This considering that if the user decides to buy 10 'actions' then the procedures generates one probability for each action in
            each trial. Finally it gives as a result a list of two arrays: the cumulative gain (cumu_ret) and the daily percentage of earnings(daily_ret)
            for each trial
        The parameters needed:
        :param position: One value (integer) which is the number of 'actions' to invest in
        :param numtrials: number of simulations to be run
        :return: a list with the two arrays mentioned above
        """
        position_value=1000/position
        cumu_ret=np.zeros(numtrials)
        daily_ret=np.zeros(numtrials)
        for trial in range(numtrials):
            for numposition in range(position):
                probabilitiesrandom = np.random.rand(position,)
                valuesgain = probabilitiesrandom.copy()
                valuesgain[valuesgain >= 0.49] = 2
                valuesgain[valuesgain < 0.49] = 0
                gain = valuesgain*position_value
            cumu_ret[trial] = gain.sum()
            daily_ret[trial] = (cumu_ret[trial]/1000) - 1
        return [cumu_ret, daily_ret]

    @staticmethod
    def calculatepositionssimulation(positions, numtrials):
        """
        The function is pretty similar to the other one, but this works whith multiple positions. It actually calls the
        other function.
        :param positions: A 4 element list indicating the number of positions to buy
        :param numtrials: numbe of simulations to be run
        :return: a list of two arrays, with 4 values corresponding to each position bought
        """
        positionpossiblevalues = np.array([1,10,100,1000])
        positionscopy = np.array(positions).copy()
        for i in range(len(positionscopy)):
            if np.any(np.in1d(positionpossiblevalues, positions[i])== True):
                positionscopy[i] = True
            else:
                positionscopy[i] = False
        if len(positionscopy) != 4:
            print 'Insert only 4 values'
        else:
            if np.any(positionscopy == False):
                raise ExceptionInvestment
                print 'Values are not the ones indicated, they must be 1,10,10 or 100'
            else:
                cumu_ret=[]
                daily_ret=[]
                for numpos in range(4):
                    value = investment.calculatesimulation(positions[numpos], numtrials)
                    cumu_ret.append(value[0])
                    daily_ret.append(value[1])
        return [cumu_ret, daily_ret]

    @staticmethod
    def generategraphicsandstats():
        """
        This function gives as a result the graphs and txt asked in the last question. It uses the function calculatesimulation
        The inputs are the ones established in the prompt of the problem.
        The logic followed is similar to the function calculatesimulation. It is added a mean and std along with the grahs.
        Each value of the position (4) is evaluated in a loop, and then the mean, sd and graph are computed
        :return: It returns the pdf (one for each value) and the txt
        """
        positions = np.array([1,10,100,1000])
        numtrials = 10000
        meanloop = np.zeros(4)
        stdloop = np.zeros(4)
        results = open('results.txt','w')
        for numpos in range(4):
            value = investment.calculatesimulation(positions[numpos], numtrials)
            cumu_ret = value[0]
            daily_ret = value[1]
            plt.show()
            plt.hist(daily_ret,100, range=[-1, 1])
            plt.xlim(-1,1)
            meanloop[numpos] = np.mean(np.array(cumu_ret))
            stdloop[numpos] = np.std(np.array(cumu_ret))
            valueprint = '%04d' % positions[numpos]
            plt.savefig('histogram_'+valueprint+'_pos.pdf')
            plt.close()
            results.write("Mean for position %i = %f \n" %(positions[numpos],np.mean(np.array(daily_ret))))
            results.write("Std for position %i = %f \n\n" %(positions[numpos],np.std(np.array(daily_ret))))
        statstotal=[meanloop,stdloop]
        return statstotal

