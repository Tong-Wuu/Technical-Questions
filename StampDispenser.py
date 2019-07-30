
# Facilitates dispensing stamps for a postage stamp machine.


class StampDispenser:
    '''
    Constructs a new StampDispenser that will be able to dispense the given
    types of stamps.

    :param stampDenominations: The values of the types of stamps that the
                               machine should have.  Should be sorted in descending order and
                               contain at least a 1.

    '''

    def __init__(self, denominations):
        self.stampDenominations = denominations

    def calcMinNumStampsToFillRequest(self, request):
        '''
        Returns the minimum number of stamps that the machine can dipsense to
        fill the given request.

        :param request: The total value of the stamps to be dispensed.
        '''
        maximum = request + 1  # Create a maximum filler for the bottom up list
        bottom_up = [maximum] * (request + 1)  # Initialize list with max value
        bottom_up[0] = 0  # Initialize 0 request with 0 minimum

        for req in range(1, request + 1):  # Find minimum stamp for each request
            for index in range(0, len(self.stampDenominations)):
                if self.stampDenominations[index] <= req:  # Find the denomination less that request
                    bottom_up[req] = min(  # find the minimum based on previous requests
                        bottom_up[req],
                        bottom_up[req - self.stampDenominations[index]] + 1)
        return bottom_up[request]  # Return the minimum value of the target request


def main():
        denominations = [90, 30, 24, 10, 6, 2, 1]
        stampDispenser = StampDispenser(denominations)

        denominations2 = [1]
        stampDispenser2 = StampDispenser(denominations2)

        try:
            test_1 = stampDispenser.calcMinNumStampsToFillRequest(0)
            test_2 = stampDispenser.calcMinNumStampsToFillRequest(18)
            test_3 = stampDispenser.calcMinNumStampsToFillRequest(10)
            test_4 = stampDispenser.calcMinNumStampsToFillRequest(23)
            test_5 = stampDispenser.calcMinNumStampsToFillRequest(26)
            test_6 = stampDispenser2.calcMinNumStampsToFillRequest(18)

            assert test_1 == 0, "Request: 0, {} is not the minimum".format(test_1)
            assert test_2 == 3, "Request: 18, {} is not the minimum".format(test_2)
            assert test_3 == 1, "Request: 10, {} is not the minimum".format(test_3)
            assert test_4 == 4, "Request: 23, {} is not the minimum".format(test_4)
            assert test_5 == 2, "Request: 26, {} is not the minimum".format(test_5)
            assert test_6 == 18, "Request: 18, {} is not the minimum".format(test_6)
            print("All testcases passed!")
        except AssertionError as error:
            print(error)


if __name__ == '__main__':
    main()
