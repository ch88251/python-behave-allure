from behave import given, when, then
from algorithms.repeated_string import repeated_string
from hamcrest import assert_that, equal_to


@given('a string {s} that can repeat indefinitely, and an integer {n} for the number of letters to evaluate')
def step_impl(context, s, n):
    context.s = s
    context.n = int(n)


@when('I execute the repeated_string function')
def step_impl(context):
    context.count = repeated_string(context.s, context.n)


@then('the repeated_string function should return the value {count}')
def step_impl(context,  count):
    assert_that(context.count, equal_to(int(count)))
