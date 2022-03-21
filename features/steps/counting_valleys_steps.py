from behave import given, when, then
from algorithms.counting_valleys import counting_valleys

from models.journey import Journey


@given('a hiker follows the sequence "{sequence}" with {steps} steps')
def step_impl(context, sequence, steps):
    context.journey = Journey(steps, sequence)


@when('the hiker follows the steps')
def step_impl(context):
    result = counting_valleys(context.journey.steps, context.journey.sequence)
    context.journey.num_valleys(result)


@then('the total number of valleys crossed is {valleys}')
def step_impl(context, valleys):
    assert context.journey.valleys == int(valleys)
