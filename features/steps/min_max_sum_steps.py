from algorithms import min_max_sum
from behave import given, when, then


@given(u'I have an array with integers 1, 3, 5, 7 and 9')
def step_impl(context):
    context.arr = [1,3,5,7,9]


@when(u'I calculate the minimum sum of 4 numbers')
def step_impl(context):
    context.minSum = min_max_sum.mini_max_sum(context.arr)


@then(u'I should get a result of 16')
def step_impl(context):
    assert context.minSum[0] == 16


@when(u'I calculate the maximum sum of 4 numbers')
def step_impl(context):
    context.maxSum = min_max_sum.mini_max_sum(context.arr)


@then(u'I should get a result of 24')
def step_impl(context):
    assert context.minSum[1] == 24