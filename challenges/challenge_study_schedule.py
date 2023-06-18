def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    # raise NotImplementedError
    if not target_time:
        return None

    student_counter = 0

    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None

        if period[0] <= target_time <= period[1]:
            student_counter += 1
    return student_counter
