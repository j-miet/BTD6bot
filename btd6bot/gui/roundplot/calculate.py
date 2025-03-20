"""Calculates round income and monkey cost data for gui_roundplot."""

def get_costs(plan_str: str, round_labels: list[str], rounds: list[str] | list[list[str]]) -> list[int]:
    """Calculates values of cash spend each round and returns these as a round-ordered list.
    
    Commands of each round are checked, and if commands require cash, get cost value from a json dictionary and add it 
    to total sum. Then append this sum to a list, yielding a list of all cash spend values of each round, ordered from 
    first round to last: index + 1 corresponds to same round e.g. costs[10] contains total cost value of round 11.

    Monkey, hero and upgrade costs depend on selected difficulty:
        easy = 0.85
        medium = 1.0 (<- base value, these are stored in costs.json)
        hard = 1.08
        hard (impoppable) = 1.25
    
    Args:
        plan_str: Plan name; needed for matching to right difficulty: easy, medium, hard, impoppable.
        round_labels: All rounds in current plan.
        rounds: All round commands of each round. Is a list of strings for single round plans; if multiple rounds, 
            returns a list of string lists.

    Returns:
        A list of all cost values. List is ordered i.e. index 0 points to first rounds, index -1 points to final round.
    """
    return [0]

def get_incomes(round_labels: list[str], rounds: list[str] | list[list[str]]) -> list[int]:
    """Returns a round-ordered list of round incomes.

    Match round label to a json dictionary round value and append this to a list. This gives a list where index + 1 
    points to corresponding round e.g. incomes[89] contains round 90 total income value.

    Args:
        round_labels: All rounds in current plan.
        rounds: All round commands of each round. Is a list of strings for single round plans; if multiple rounds, 
            returns a list of string lists.
            
    Returns:
        A list of all income values. List is ordered i.e. index 0 points to first rounds, index -1 points to final 
        round.
    """
    return [0]