from __future__ import print_function, division
import numpy as np

def test_task2_part2_a():
    assert 2/8 == 0.25
    print("Test 1 Success!")

def test_task2_part2_b():
    a = np.array([2])
    b = np.array([8])
    assert a.shape == (1,)
    assert b.shape == (1,)
    assert a/b == 0.25
    print("Test 2 Success!")

test_task2_part2_a()
test_task2_part2_b()
