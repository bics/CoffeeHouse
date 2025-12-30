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
    1. Removed aria-labelledby.
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

### Reset password workflow pages:
1. Reset password page:
    * During validation 1 error was flagged:
        * Action attribute on form was empty.

    Steps taken:
    1. Removed unused action attribute.

2. Password reset done page:
    * During validation there were no errors present.

3. Password reset from key page:
    * During validation a couple error were flagged:
        * Bad value for attribute action on element form: Must be non-empty.
        * End tag p implied, but there were open elements.
        * Unclosed element span.
        * Stray end tag span.
        * No p element in scope but a p end tag seen.

    Steps taken:
    1. Action element was populated from the input element action attribute.
    2. Orphaned elements were rendered incorrectly by Django default output. Updated form to be displayed with divs instead.

4. Password reset from key done page:
    * During validation there were no errors present.

### (A) Conversation page:
* During validation a couple error were flagged:
    * Couple errors were flagged for aria-labelledby attribute multiple times
    * Bad value for attribute action on element form: Must be non-empty.
    * Bad value button for attribute type on element a: Subtype missing.

    Steps taken:
    1. Removed aria-labelledby.
    2. Removed unused action attribute.
    3. Removed incorrect type attribute from a element.

### HTML validation

### CSS validation 

### JS validation