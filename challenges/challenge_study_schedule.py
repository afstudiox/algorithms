def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not isinstance(target_time, int) or not isinstance(target_time, int):
        return None
    students = 0

    for init, end in permanence_period:
        if not isinstance(init, int) or not isinstance(end, int):
            return None
        elif init <= target_time <= end:
            students += 1
    return students
    # raise NotImplementedError
