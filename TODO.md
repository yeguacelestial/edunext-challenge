TODO List
========================
* [X] 001_challenge_stack
* [ ] 002_fun_coding_time
  * [ ] Service to interact between customers API and PayPal services
    * [X] Django REST Framework - initial setup
    * [ ] Handling requests for creating/updating data on the Customer API from the Service API
      * IF all fields are available on the POST request:
        * IF payment_status value is "Completed":
          * Update info on the Customer API.