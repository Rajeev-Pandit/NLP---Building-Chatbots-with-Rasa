## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - utter_ask_location
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "599"}
    - slot{"money": "599"}
    - action_search_restaurants
    - slot{"facility_type": "Delhi"}
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* place_price_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny    
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - utter_ask_location
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}        
    - utter_ask_cuisine
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "599"}
    - slot{"money": "599"}
    - action_search_restaurants
    - slot{"facility_type": "Delhi"}
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - utter_ask_location
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}        
    - utter_ask_cuisine
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "599"}
    - slot{"money": "599"}
    - action_search_restaurants
    - slot{"facility_type": "Delhi"}
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant"}
    - slot{"facility_type": "restaurant"}
    - utter_ask_location
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}        
    - utter_We_Do_not_operate
    - utter_goodbye
    - action_restart   

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* place_price_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_cuisine
* place_price_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true} 
    - utter_ask_cuisine
* place_price_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true} 
    - utter_ask_cuisine
* place_price_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}
    - utter_We_Do_not_operate
    - utter_goodbye
    - action_restart       

## interactive_story_11
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}  
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart
    
## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}  
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart    

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_again
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}        
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_again
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}        
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_again
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_wrong_cuisine
    - utter_goodbye
    - action_restart 

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}  
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart
 
## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}  
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart 
 
## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}  
    - utter_ask_location
* place_price_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}  
    - utter_We_Do_not_operate
    - utter_goodbye
    - action_restart

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}    
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": true}    
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": true}
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": false}
    - utter_ask_location_again
* place_price_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"check_location": false}         
    - utter_We_Do_not_operate
    - utter_goodbye
    - action_restart

## interactive_story_24
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_again
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}        
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* email{"emailid": "rajeevpandit6@gmail.com"}
    - slot{"emailid": "rajeevpandit6@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - utter_goodbye
    - action_restart

## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_again
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": true}        
    - utter_ask_price
* place_price_search{"money": "799"}
    - slot{"money": "799"}
    - action_search_restaurants
    - slot{"restaurants_list": "<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th>name</th>\n      <th>location</th>\n      <th>rating</th>\n      <th>avg_cost_for2</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Burger King</td>\n      <td>2nd Floor, Select Citywalk Mall, Saket, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>E-8, Inner Circle, Connaught Place, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n    <tr>\n      <td>Burger King</td>\n      <td>F-15, Vijay Block, Laxmi Nagar, New Delhi</td>\n      <td>4.1</td>\n      <td>500</td>\n    </tr>\n  </tbody>\n</table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_26
* greet
    - utter_greet
* restaurant_search{"facility_type": "restaurant", "location": "Mumbai", "cuisine": "Italian"}
    - slot{"facility_type": "restaurant"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"check_location": true}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"check_cuisine": false}
    - utter_ask_cuisine_again
* place_price_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"check_cuisine": false}  
    - utter_wrong_cuisine
    - utter_goodbye
    - action_restart