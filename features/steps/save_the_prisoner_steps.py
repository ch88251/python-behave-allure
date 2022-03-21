from behave import given, when, then
from algorithms.save_the_prisoner import save_the_prisoner
from hamcrest import assert_that, equal_to


@given('there are {num_prisoners} prisoners, {num_sweets} sweets and I start with chair {chair_num}')
def step_impl(context, num_prisoners, num_sweets, chair_num):
    context.num_prisoners = int(num_prisoners)
    context.num_sweets = int(num_sweets)
    context.chair_num = int(chair_num)


@when('the prison guard distributes the sweets')
def step_impl(context):
    context.result = save_the_prisoner(
        context.num_prisoners, context.num_sweets, context.chair_num)


@then('the prisoner at chair {chair_num} will receive the bad sweet')
def step_impl(context, chair_num):
    assert_that(context.result, equal_to(int(chair_num)))