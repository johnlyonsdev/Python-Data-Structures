"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()
    text = open(filename)
    for line in text:
      line = line.rstrip()
      line = line.split("|")
      if line[2] != '':
        houses.add(line[2])

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    text = open(filename)
    for line in text:
      line = line.rstrip()
      first, last, house, advisor, s_cohort = line.split("|")
      name = first+" "+last
      if len(s_cohort) > 1:
        if cohort == 'All':
            students.append(name)
        elif cohort == s_cohort:
          students.append(name)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    text = open(filename)
    for line in text:
      line = line.rstrip()
      first, last, house, advisor, s_cohort = line.split("|")
      name = first+" "+last

      if house == 'Gryffindor':
        gryffindor.append(name)
      elif house == 'Hufflepuff':
        hufflepuff.append(name)
      elif house == 'Ravenclaw':
        ravenclaw.append(name)
      elif house == 'Slytherin':
        slytherin.append(name)
      elif house == "Dumbledore's Army":
        dumbledores_army.append(name)
      elif s_cohort == 'G':
        ghosts.append(name)
      elif s_cohort == 'I':
        instructors.append(name)
 
    list = []
    list.append(sorted(dumbledores_army))
    list.append(sorted(gryffindor))
    list.append(sorted(hufflepuff))
    list.append(sorted(ravenclaw))
    list.append(sorted(slytherin)) 
    list.append(sorted(ghosts))
    list.append(sorted(instructors))
    return list

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    text = open(filename)
    for line in text:
      line = line.rstrip()
      first, last, house, advisor, s_cohort = line.split("|")
      name = first+" "+last
      tuple = (name, house, advisor, s_cohort)
      all_data.append(tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    text = open(filename)
    for line in text:
      line = line.rstrip()
      first, last, house, advisor, s_cohort = line.split("|")
      full_name = first+" "+last
      if name == full_name:
        return s_cohort
    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    dupe = set()
    names = []
    text = open(filename)
    for line in text:
      line = line.rstrip()
      first, last, house, advisor, s_cohort = line.split("|")
      if last in names:
        dupe.add(last) 
      else:
        names.append(last)
    return dupe




def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    housemates = set()
    for person in all_data(filename):
      full_name, house, advisor, cohort = person
      if full_name == name:
        theHouse = house
        theCohort = cohort
    for person in all_data(filename):
      full_name, house, advisor, cohort = person
      if full_name != name:
        if (house, cohort) == (theHouse, theCohort):
          housemates.add(full_name)

    return housemates


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
