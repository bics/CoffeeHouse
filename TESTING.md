# Testing

## Manual testing

### Landing page (login and tables)

* Visually tested all elements are in place.
* Devtools were used to simulate different devices and ensure page is responsive.
* Tested all links on page.
* Tested account login with both email and username.

Issues found and steps taken:

* Login was not working with email address.
    * Updated login method in settings, added core authentication services.

## Automated testing

### HTML validation

Used [W3C](https://www.w3.org) validator for both [html](https://validator.w3.org) and [css](https://jigsaw.w3.org/css-validator/) validation.

### Landing page (login and tables)
1. Login page:
    * During validation there were no errors present.

2. Tables page:
    * A couple of errors were flagged for aria-labelledby attribute.
    * Action attribute on form was empty.

    Steps taken:
    1. Removed aria-labelledby.
    2. Removed unused action attribute.

### Signup page:
* During validation a couple of errors were flagged:
    * Action attribute on form was empty.
    * End tag p implied, but there were open elements.
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
    * During validation, a couple of errors were flagged:
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
* During validation, a couple of errors were flagged:
    * A couple of errors were flagged for aria-labelledby attribute multiple times.
    * Bad value for attribute action on element form: Must be non-empty.
    * Bad value button for attribute type on element a: Subtype missing.

    Steps taken:
    1. Removed aria-labelledby.
    2. Removed unused action attribute.
    3. Removed incorrect type attribute from a element.

### Account management page:
* During validation, a couple of errors were flagged:
    * Bad value for attribute action on element form: Must be non-empty.
    * The value of the for attribute of the label element must be the ID of a non-hidden form control.
    * The aria-describedby attribute must point to an element in the same document.

    Steps taken:
    1. Removed unused action attribute.
    2. Using correct ID for label.
    3. Removed aria-describedby from form.

### User deletion page:
* During validation, a couple of errors were flagged:
    * Element p not allowed as child of element strong in this context. (Suppressing further errors from this subtree.)
    * Bad value for attribute action on element form: Must be non-empty.

    Steps taken:
    1. Removed unused action attribute.
    2. Inverted p and strong elements.

### CSS validation

Style (style.css) testing:
* During validation there were no errors present.

### Python validation

Used [Pycodestyle](https://pycodestyle.pycqa.org/en/latest/) validator.\
Used [Black](https://black.readthedocs.io/en/stable/?utm_source=chatgpt.com) linter to beautify code.\
During validation, a couple of errors were flagged:
* .\members\forms.py:24:89: E501 line too long (119 > 88 characters)
* .\members\forms.py:39:89: E501 line too long (115 > 88 characters)
As I used an industry-standard linter with Pycodestyle correctly set up to match Black’s line length, I chose to ignore the above errors.


