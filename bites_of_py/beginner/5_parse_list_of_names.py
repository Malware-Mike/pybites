NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    """ 
        names = list(set(NAMES))
        return [i.title() for i in names]
    """
    dedup = set(names)
    new_list =[]

    for name in dedup:
        new_list.append(name.title())


    return new_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # ...
    desc_order = sorted(names, reverse=True, key=lambda x: x.split(" ")[-1])

    return desc_order

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # ...
    first_names = [name.split(' ')[0] for name in names]

    return min(first_names, key=len)

