# Testing

## Manual testing

## Automated testing

Used [W3C](https://www.w3.org) validator for both [html](https://validator.w3.org) and [css](https://jigsaw.w3.org/css-validator/) validation.\

### Landing page (login and tables)
1. Login page:
    * During validation there were no errors present.

2. Tables page:
    * Couple errors were flagged for aria-labelledby attribute.
    * Action attribute on form was empty.

    Steps taken:
    1. Updated aria-labelledby to point to an actual element, and added a role to the parent element.
    2. Removed unused action attribute.

### Signup page:
* During validation a couple error were flagged:
    * Action attribute on form was empty.
    * End tag p implied, but there were open elements.ű
    * Unclosed element span.
    * Stray end tag span.
    * No p element in scope but a p end tag seen.
    * Attribute action not allowed on element input at this point.

    Steps taken:
    1. Action element was populated from the input element action attribute.
    2. Orphaned elements were rendered incorrectly by Django default output. Updated form to be displayed with divs instead.




### HTML validation

### CSS validation 

### JS validation