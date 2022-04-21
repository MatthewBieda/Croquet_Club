#Croquet Club Problem
#Two categories: Senior / Open
#Senior requirements: Age >= 55, Handicap > 7
#Handicap range -2 to +26
#Input [[18,20], [61,2]]
#Index 0 = Age, Index 1 = Handicap
#Output["Open", "Senior"]

def main():

    test_input =  [[18,20], [45,2], [61,12], [37,6], [21,21], [78,9]]

    def assign_category(input):
        '''
        Assigns the person a category by iterating through the input list and 
        creating an output list based on the specified conditions
        '''

        output_list = []

        for pair in input:
            if pair[0] >= 55 and pair[1] > 7:
                output_list.append("Senior")
            else:
                output_list.append("Open")

        return output_list

    print(assign_category(test_input))

if __name__ == "__main__":
    main()