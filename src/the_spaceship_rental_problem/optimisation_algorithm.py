
import logging
from operator import attrgetter, itemgetter
from typing import List, Tuple
from .models import Contract, Solution


def optimize(contracts: List[Contract]):
    contracts = sort_contracts(contracts)
    return find_solution(contracts)


def sort_contracts(contracts: List[Contract]):
    return sorted(contracts, key=attrgetter("start"))


def overlap(previous_contract: Contract, next_contract: Contract):
    return previous_contract.start + previous_contract.duration > next_contract.start


def find_solution(contracts: List[Contract]):
    solutions = []
    for overlap_start, overlap_end in find_overlapping_contracts(contracts):
        overlap_solutions = []
        logging.debug("overlapp " + str(overlap_start) + " to " + str(overlap_end))
        for start in get_branch_starts(overlap_start, contracts):
            logging.debug("start " + str(start))
            new_branch(start, overlap_end, contracts, overlap_solutions, [], 0)
        logging.debug(overlap_solutions)
        solutions.append(max(overlap_solutions, key=itemgetter(1)))
    result = Solution(path=[])
    for solution in solutions:
        result.path.extend(solution[0])
        result.income += solution[1]
    return result

def find_overlapping_contracts(contracts: List[Contract]):
    idx = 1
    overlap_start = 0
    while idx < len(contracts):
        contract = contracts[idx - 1]
        next_contract = contracts[idx]
        if not overlap(contract, next_contract):
            yield (overlap_start, idx)
            overlap_start = idx
        idx += 1
    yield (overlap_start, idx)

def get_branch_starts(idx, contracts: List[Contract]):
    first_contract = contracts[idx]
    yield idx
    idx += 1
    while idx < len(contracts):
        next_contract = contracts[idx]
        if overlap(first_contract, next_contract):
            yield idx
        else:
            break
        idx += 1

def new_branch(idx: int, end: int, contracts: List[Contract], solutions: List[Tuple[List[str], int]], current_path: List[str], current_income: int):
    logging.debug(f"branch on {idx}")
    contract = contracts[idx]
    logging.debug("add " + str(contract))
    current_path.append(contract.name)
    current_income += contract.price
    idx += 1
    last = True
    while idx < end:
        next_contract = contracts[idx]
        if not overlap(contract, next_contract):
            logging.debug("go " + str(next_contract))
            new_branch(idx, end, contracts, solutions, current_path.copy(), current_income)
            last = False
        idx += 1
    if last:
        solutions.append((current_path, current_income))
