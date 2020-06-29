import apriori


sample_data_1 = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

for rule in apriori.generate_rules(sample_data_1, min_support=0.5):
    msg = (f'{rule.format_rule():20s}\t\t'
           f'(support={rule.support:0.4f}, confidence={rule.confidence:0.4f}, lift={rule.lift:0.4f})')
    print(msg)


print("Example with string info. Note that everyone has a cat (lots of support, but lift is 1 as cat has no info)")
sample_data_2 = [['cat', 'dog'], ['cat', 'fish'], ['cat', 'dog', 'fish'], ['cat', 'fish', 'horse'],
                 ['cat', 'horse', 'dog'], ['cat', 'horse', 'dog'], ['cat', 'horse', 'dog']]

for rule in apriori.generate_rules(sample_data_2, min_support=0.2, min_lift=1.05):
    msg = (f'{rule.format_rule():20s}\t\t'
           f'(support={rule.support:0.4f}, confidence={rule.confidence:0.4f}, lift={rule.lift:0.4f})')
    print(msg)
