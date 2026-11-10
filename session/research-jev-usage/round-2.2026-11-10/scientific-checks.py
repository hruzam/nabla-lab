"""Bounded research calculations; no application implementation or model calls.

Run from any directory with Python's standard library. Writes one receipt beside
this file. No private evidence, imports outside stdlib, randomness or networking.
"""
from datetime import datetime, timezone
from decimal import Decimal
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import platform


def relu(x):
    return max(F(0), x)


def tent_branch(x, a):
    return a * min(x, 1 - x)


def tent_network(x, a):
    return a * relu(x) - 2 * a * relu(x - F(1, 2)) + a * relu(x - 1)


def iterate(x, a, depth, function=tent_branch):
    for _ in range(depth):
        x = function(x, a)
    return x


def main():
    # Explicit full matrices, rather than only substituting the simplified rule.
    w1 = [[F(0) for _ in range(8)] for _ in range(16)]
    b1 = [F(0) for _ in range(16)]
    w2 = [F(0) for _ in range(16)]
    b2 = -F(1, 2)
    w1[0][0] = w2[0] = F(1)
    parameters = sum(map(len, w1)) + len(b1) + len(w2) + 1
    assert parameters == 161
    parity_count = 0
    for x in product((0, 1), repeat=8):
        hidden = [relu(sum(v * z for v, z in zip(row, x)) + bias)
                  for row, bias in zip(w1, b1)]
        score = sum(v * z for v, z in zip(w2, hidden)) + b2
        assert (score > 0) == bool(x[0])
        parity_count += 1

    # Exact comparison at multiple rational parameters, inputs and depths.
    tent_checks = 0
    for a in (F(1, 2), F(1), F(3, 2), F(2)):
        for k in range(129):
            x = F(k, 128)
            for depth in range(1, 11):
                assert iterate(x, a, depth) == iterate(x, a, depth, tent_network)
                tent_checks += 1

    # Endpoints alternate 0 and 1; midpoints and slopes check each predicted branch.
    branches_checked = 0
    for depth in range(1, 11):
        n = 2 ** depth
        for k in range(n):
            left, right = F(k, n), F(k + 1, n)
            yl, yr = iterate(left, F(2), depth), iterate(right, F(2), depth)
            assert yl == k % 2 and yr == (k + 1) % 2
            assert iterate((left + right) / 2, F(2), depth) == F(1, 2)
            assert abs((yr - yl) / (right - left)) == n
            branches_checked += 1

    dyadic_cases, max_steps = 0, 0
    for b in range(1, 9):
        for k in range(2 ** b + 1):
            x, steps = F(k, 2 ** b), 0
            while x != 0 and steps < b + 1:
                x = tent_branch(x, F(2))
                steps += 1
            assert x == 0
            dyadic_cases += 1
            max_steps = max(max_steps, steps)

    # A=.5 contraction bound |T^n(x)| <= .5^n |x|.
    for k in range(129):
        x = F(k, 128)
        assert iterate(x, F(1, 2), 10) <= F(1, 2) ** 10 * x

    # Semantic premise is external: these must be probabilities of the named union.
    group = [Decimal('0.01'), Decimal('0.02')] + [Decimal(0)] * 13
    aggregate = Decimal('0.15')
    lower, upper = max(group), min(Decimal(1), sum(group))
    rounding_upper_sum = sum(p + Decimal('0.005') for p in group)
    rounding_aggregate_lower = aggregate - Decimal('0.005')
    assert (lower, upper) == (Decimal('.02'), Decimal('.03'))
    assert rounding_upper_sum == Decimal('.105')
    assert rounding_aggregate_lower == Decimal('.145')
    assert rounding_upper_sum < rounding_aggregate_lower

    receipt = {
        'kind': 'bounded scientific calculations, not workload/model benchmark',
        'captured_utc': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(),
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'tiny_network': {'parameters': parameters, 'float32_payload_bytes': 4 * parameters,
                         'binary_vectors_checked': parity_count, 'mismatches': 0,
                         'training_performed': False},
        'tent_map': {'arithmetic': 'fractions.Fraction (exact rational)',
                     'parameters': ['1/2', '1', '3/2', '2'],
                     'expression_parity_cases': tent_checks,
                     'branch_endpoint_midpoint_slope_checks': branches_checked,
                     'maximum_depth': 10, 'dyadic_cases': dyadic_cases,
                     'maximum_dyadic_exponent': 8, 'maximum_steps_to_zero': max_steps,
                     'contraction_bound_checks': 129,
                     'general_proof': 'see implementation-substrate.md; finite checks alone are not proof'},
        'conditional_union': {'group_count': 15, 'lower': str(lower), 'upper': str(upper),
                              'aggregate': str(aggregate), 'coherent_if_same_exhaustive_events': False,
                              'hypothetical_rounding': 'nearest .01, convention not established',
                              'rounded_group_upper_sum': str(rounding_upper_sum),
                              'rounded_aggregate_lower': str(rounding_aggregate_lower)},
        'sample_size_illustration': {
            'zero_misses_positive_trials': 59,
            'one_sided_95_upper_miss_rate': 1 - .05 ** (1 / 59),
            'assumptions': 'independent Bernoulli positive trials, fixed rule; not general calibration sufficiency'},
        'limits': ['No Jev/model inference, training or cache replay',
                   'No performance/speedup or host capacity benchmark',
                   'No new theorem or independent empirical accuracy claim'],
        'status': 'PASS'
    }
    target = Path(__file__).with_name('scientific-receipt.json')
    target.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
