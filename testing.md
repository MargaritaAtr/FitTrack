
# Testing documentation for Fit Track website.
<br>

![Alt text](docs/readme/homepage.png)

# Contents

* [Validation](#validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JS Validation](#js-validation)
    * [CI Python Linter](#ci-python-linter)
    * [Lighthouse](#lighthouse)
* [User Story Testing](#user-story-testing)
    * [General](#general)
    * [Logged Out](#logged-out)
    * [User Logged In](#user-logged-in)
* [Manual Testing](#manual-testing)
* [Responsiveness](#responsiveness)
* [Fixed Bugs](#fixed-bugs)
* [Unfixed Bugs](#unfixed-bugs)

<br><br>

# Validation

## HTML Validation

* All pages successfully passed the HTML validator check, except for a warning regarding a duplicate ID, dropdownMenuButton2. I have resolved this by updating the IDs to dropdownMenuButton1, dropdownMenuButton2, dropdownMenuButton3, and dropdownMenuButton4 respectively. This change eliminated the warning, and now all pages are error-free according to the HTML validator.

* On the contact page, an error was indicated concerning the for attribute of a label, which should specify the ID of a form control that the label is associated with. To address this, I made modifications to the contact form to rectify the error.

<details>
<summary>Homepage</summary>
<br>

![Alt text](docs/validation-images/homepage.png)
</details>

<details>
<summary> Sign in page </summary>
<br>

![Alt text](docs/validation-images/sign-in.png)
</details>


<details>
<summary> My profile page </summary>
<br>

![Alt text](docs/validation-images/my-profile.png)
</details>

<details>
<summary> Add product page </summary>
<br>

![Alt text](docs/validation-images/add-product.png)
</details>

<details>
<summary> Bag page </summary>
<br>

![Alt text](docs/validation-images/bag.png)
</details>

<details>
<summary> Check out page </summary>
<br>

![Alt text](docs/validation-images/checkout.png)
</details>

<details>
<summary>All Products page </summary>
<br>

![Alt text](docs/validation-images/all-products.png)
</details>

<details>
<summary>Product detail page </summary>
<br>
![Alt text](docs/validation-images/product-detail.png)
</details>
<details>
<summary> Contact page </summary>
<br>
![Alt text](docs/validation-images/contact.png)
</details>

<br>

## CSS Validation

* CSS files passed W3C validator with no errors.

<details>
<summary> Bace css </summary>
<br>

![Alt text](docs/validation-images/base-css.png)
</details>

<details>
<summary> Checkout css </summary>
<br>

![Alt text](docs/validation-images/checkout-css.png)
</details>

<details>
<summary> Product css </summary>
<br>

![Alt text](docs/validation-images/product-css.png)
</details>

<details>
<summary> Profile css </summary>
<br>

![Alt text](docs/validation-images/profile-css.png)
</details>

<br>

## JS Validation

* The JS file passed the test with two warnings. It can be ignored as code works as expected.

<details>
<summary> Stripe js file </summary>
<br>

![Alt text](docs/validation-images/js-validator.png)
</details>