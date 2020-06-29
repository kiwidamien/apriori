import itertools
# from pydantic import BaseModel

# from typing import List, Set, Iterable, FrozenSet, Union, Dict
from apriori.apriori_types import *


class Transactions:
    def __init__(self, transactions: Iterable[Iterable[ItemLabel]]):
        self.individual_items = set()
        self._transaction_count = {}
        self.total_transactions = 0
        self.add_bulk_transactions(transactions)

    def add_bulk_transactions(self, transactions :Iterable[Iterable[ItemLabel]]):
        for transaction in transactions:
            immutable_items = frozenset(transaction)
            self.total_transactions += 1
            self._transaction_count[immutable_items] = self._transaction_count.get(immutable_items, 0) + 1
        new_items = set(itertools.chain.from_iterable(transactions))
        self.individual_items = self.individual_items.union(new_items)

    def __repr__(self):
        return f'<Transactions ({self.total_transactions} transactions with {len(self.individual_items)} items)>'

    def initial_candidates(self):
        return [frozenset({element}) for element in self.individual_items]

    def calc_support(self, candidate_sets: Iterable[SetLike], min_support=0.0) -> Dict[Transaction, float]:
        """Returns the support of each Transaction (Iterable[ItemLabel]) A.

        Support = Prob a random transaction has A as a subset = P(A)
        """
        ssCnt = {}
        for candidate in candidate_sets:
            for transaction_items, transaction_count in self._transaction_count.items():
                if candidate.issubset(transaction_items):
                    candidate = frozenset(candidate)
                    ssCnt[candidate] = ssCnt.get(candidate, 0) + transaction_count
        min_count = min_support * self.total_transactions
        return {candidate: counts/self.total_transactions for candidate, counts in ssCnt.items()
                if counts >= min_count}

    @staticmethod
    def _apriori_generate(Lk: Iterable[SetLike], k: int) -> Iterable[Transaction]:
        """Takes a list of sets of size k, and returns a list of sets of size k+1 that can be generated by merging two

        Examples:
            Lk = [{1,2,3}, {2,3,4}, {9, 10, 1}], k=3
            By union of {1,2,3} and {2,3,4} we get {1,2,3,4} which is 4 units long
            By union of {1,2,3} and {9, 10, 1} we get {1,2,3,9,10} which is 5 units long
            By union of {2,3,4} and {9, 10, 1} we get {1,2,3,4,9,10} which is 6 units long
            So aprioriGen(Lk, 3) would return [{1,2,3,4}]
        """
        candidate_with_k_plus_one = set()
        for L1, L2 in itertools.combinations(Lk, 2):
            # By set principle |L1 U L2| = |L1| + |L2| - |L1 n L2| = k + k - |L1 n L2|
            # If we want |L1 U L2| to have size k+1, we need |L1 n L2| = k-1
            if len(frozenset.intersection(L1, L2)) == (k - 1):
                candidate_with_k_plus_one.add(frozenset.union(L1, L2))
        return candidate_with_k_plus_one


def apriori(data, min_support=0.5):
    transactions = Transactions(data)
    support = transactions.calc_support(transactions.initial_candidates(), min_support)
    L = [list(support.keys())]
    items_in_candidate_set = 1
    while (len(L[items_in_candidate_set - 1]) > 0):
        list_items_with_k_minus_1_items = L[items_in_candidate_set - 1]
        candidates_with_k_items = Transactions._apriori_generate(list_items_with_k_minus_1_items, items_in_candidate_set)
        support_k = transactions.calc_support(candidates_with_k_items, min_support)
        Lk = list(support_k.keys())
        support.update(support_k)
        L.append(Lk)
        items_in_candidate_set += 1
    return L, support


def apriori_from_transaction(transactions: Transactions, min_support=0.5):
    support = transactions.calc_support(transactions.initial_candidates(), min_support)
    L = [list(support.keys())]
    items_in_candidate_set = 1
    while (len(L[items_in_candidate_set - 1]) > 0):
        list_items_with_k_minus_1_items = L[items_in_candidate_set - 1]
        candidates_with_k_items = Transactions._apriori_generate(list_items_with_k_minus_1_items, items_in_candidate_set)
        support_k = transactions.calc_support(candidates_with_k_items, min_support)
        support.update(support_k)
        for candidate in support_k.keys():
            yield candidate, support
        Lk = list(support_k.keys())
        # print('Lk us', Lk)
        L.append(Lk)
        # print('L is',L)
        items_in_candidate_set += 1