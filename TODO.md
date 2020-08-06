TODO List
========================
* [X] 001_challenge_stack
* [ ] 002_fun_coding_time
  * [ ] Service to interact between customers API and PayPal services
    * [X] Django REST Framework - initial setup
    * [X] Creating view for manipulating and validating POST request of IPN Notification (JSON object) received on the database
    * [X] Handling requests for creating/updating data on the Customer API from the Service API
    * [ ] Add or update: DOWNGRADE_DATE and UPGRADE_DATE to the JSON objects -- Either ADD or UPDATE can be handled with HTTP PUT requests.
  <br/>
  <br/>
  <br/>
  
Pseudocode
========================
  * IF all fields are available on the POST request:
    * IF payment_status value IS "Completed":
      * IF ___item_name___ in ___['free','basic','premium']___ :
        * Update info on the Customer API.
      * ELSE:
        * Return error, notifying that the item name is not valid.
    * ELSE IF ___payment_status___ IS NOT "Completed":
      * On **CustomerAPI[payer_id]**: 
        * Update **SUBSCRIPTION** field of to ***free***
        * Update all elements of **ENABLED_FEATURES** to false
      
  * ELSE:
    * Return error, notifying that the data body is not correct