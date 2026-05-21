
https://drive.google.com/file/d/1pjibav6rwfRMwzTGor2xMCAWsABWJN4q/view?usp=drive_link
VIDEO ^^^^^^^
Blueprint 
How I implemented it:  
I created an abstract base class HotelOffering using Python’s abc module. It defines two abstract methods
Specialization 
How I implemented it 
Two subclasses extend the blueprint:
HotelRoom = adds bed_size and smoking_allowed
SpaService = adds duration_minutes
Data Protection
How I implemented it
Sensitive fields like base_price are stored as private attributes (self._base_price)
Access is controlled through getter/setter methods
How I implemented it
Each subclass overrides calculate_item_cost() differently
HotelRoom = adds 15% hospitality tax
SpaService = adds 20% gratuity fee
