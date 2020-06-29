import apriori


sample_transactions = [
    ['fish', 'white wine', 'cheese', 'bread'],
    ['beer', 'nachos', 'cheese', 'peanuts'],
    ['white wine', 'cheese'],
    ['white wine', 'cheese', 'bread']
]

for rule in apriori.generate_rules(sample_transactions, min_support=0.5):
    msg = (f'{rule.format_rule():20s}\t\t'
           f'(support={rule.support:0.4f}, confidence={rule.confidence:0.4f}, lift={rule.lift:0.4f})')
    print(msg)


print("Example with string info. Note that everyone has a cat (lots of support, but lift is 1 as cat has no info)")
pet_ownership = [['cat', 'dog'], ['cat', 'fish'], ['cat', 'dog', 'fish'], ['cat', 'fish', 'horse'],
                 ['cat', 'horse', 'dog'], ['cat', 'horse', 'dog'], ['cat', 'horse', 'dog']]

for rule in apriori.generate_rules(pet_ownership, min_support=0.2, min_lift=1.05):
    msg = (f'{rule.format_rule():20s}\t\t'
           f'(support={rule.support:0.4f}, confidence={rule.confidence:0.4f}, lift={rule.lift:0.4f})')
    print(msg)
