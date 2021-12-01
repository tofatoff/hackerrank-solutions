

    # Add your code here
    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = self.__elements[len(self.__elements)-1] - self.__elements[0]

