from behave import given, when, then
from lambda_function import compute_short_chain

@given(u'a {number}')
def set_the_given_integer(context, number):
    context.given_number = int(number)

@when(u'the short chain is computed')
def go_compute_the_short_chain(context):
    context.short_chain_value = compute_short_chain(context.given_number)

@then(u'the expected product {product} of the number and itself should be returned')
def assert_given_squared_is_returned(context, product):
    assert int(product) == context.short_chain_value
    assert context.short_chain_value == context.given_number ** 2
