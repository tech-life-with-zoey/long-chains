from behave import given, when, then
from lambda_function import compute_short_chain

@given(u'a {number}')
def set_the_given_integer(context, number):
    context.given_number = int(number)

@when(u'the short chain is computed')
def go_compute_the_short_chain(context):
    context.short_chain_value = compute_short_chain(context.given_number)

@when(u'the long chain is computed')
def go_compute_the_long_chain(context):
    context.long_chain_value = compute_long_chain(context.given_number)

@then(u'the expected product {product} of the number and itself should be returned')
def assert_given_squared_is_returned(context, product):
    assert int(product) == context.short_chain_value
    assert context.short_chain_value == context.given_number ** 2

@then(u'the expected result {cube} is the cube created when each side is the number and should be returned')
def assert_given_cube_is_returned(context, cube):
    assert int(cube) == context.long_chain_value
    assert context.long_chain_value == contex.given_number ** 3
