# coding=utf-8
##赫根添加

from __future__ import division


def convertLtoml(L):
    return L * 1000


def addHAGEN(totalWater, GH):  # set total body of water volume in liter and the purpose of GH as argument
    # In the manual, adding 14ml HAGEN in 100L water and then the General hardness (GH) will
    oneGH = (totalWater / 100) * 14
    HAGEN = GH * oneGH
    return HAGEN
    # return the value of HAGEN we have to dissolve in RO water.


print "Please add ", addHAGEN(11, 8), " ml HAGEN to get 8 GH in 11L body of water."
print "Please add ", addHAGEN(11, 6), " ml HAGEN to get 6 GH in 11L body of water."


def demoDictionaries():
    eng2sp = {}
    eng2sp["one"] = 'uno'
    eng2sp["two"] = 'dos'

    print eng2sp
    eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
    print eng2sp
    print eng2sp['two']

    inventory = {'apple': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
    print inventory
    # inventory | ˈinvənˌtôrē | a complete list items such as property

    del inventory['pears']
    print inventory

    print len(inventory)

    # A method call is called an invocation; in this case, we would say that we are
    # invoking keys on the object eng2sp
    print "the keys method returns", eng2sp.keys()
    print "the values method returns", eng2sp.values()
    print "the items method returns ", eng2sp.items()
    # The items return in the form of a list of tuples - one for each key-value pair.
    """The parentheses indicate that the elements of the list are tuples."""
    # invocation: the action of invoking something or someone for assistance or as an authority

    print "Does the key, pears,appears in the dict? ", eng2sp.has_key("four")
    print "Does the key, apple,appears in the dict? ", eng2sp.has_key("one")

    opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
    alias = opposites
    copy = opposites.copy()

    alias['right'] = 'left'
    print "the element of key['right'] is ", opposites['right']
    copy['right'] = 'privilege'  # privilege: a special right
    print "the element of key['right'] is ", opposites['right']

    """A sparse matrix is a matrix that is comprised of mostly zero value"""
    matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
    print "matrix[0,3] is ", matrix[0, 3]
    try:
        print "matrix[1,3] is ", matrix[1, 3]
    except Exception:
        print "We get an error"

    print "matrix[1.3] by using get method ", matrix.get((1, 3), 0)
    """if we specify an element that is zero, the get method will return the second argument as given"""


# demoDictionaries()

def main():
    totalWater = raw_input("Please input the total water (L): ")
    purpose_GH = raw_input("Please input the GH that you want to set:")
    # print addHAGEN(64,7)
    print "Please add  %d  ml HAGEN to get %s GH in %s L body of water." % (
    addHAGEN(int(totalWater), int(purpose_GH)), purpose_GH, totalWater)


if __name__ == '__main__':
    main()
