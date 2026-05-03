def agent_plan(marks):
    plan = {}

    if 2 in marks:
        plan["PART A (2 marks each)"] = 5

    if 5 in marks:
        plan["PART B (5 marks each)"] = 3

    if 10 in marks:
        plan["PART C (10 marks each)"] = 2

    return plan