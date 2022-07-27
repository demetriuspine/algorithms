def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0

    try:

        for start_period, end_period in permanence_period:
            if start_period <= target_time <= end_period:
                counter += 1

        return counter

    except TypeError:
        return None
