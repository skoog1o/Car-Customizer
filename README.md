OOP Enhancements
Prinicliples applied
Abstraction – The Car class is abstract, defining the structure and behavior of all cars while hiding implementation details.
Inheritance – Brand-specific classes (Porsche, BMW, Audi, Mercedes) inherit from Car, reusing common properties and methods.
Polymorphism – Each brand class overrides the display_info() method to show brand-specific car information.
Encapsulation – Key attributes like _brand, _model, _trim, _wheels, and _color are protected, and getters/setters manage access safely.
Where they appear
Abstraction: The Car class uses @abstractmethod for display_info().
Inheritance: Classes like Porsche and BMW extend the Car class.
Polymorphism: Calling display_info() on a Car instance executes the brand-specific version.
Encapsulation: _wheels and _color are accessed and modified through set_wheels(), get_wheels(), set_color(), and get_color() methods.
Why they improve
The project’s design benefits from reusability, as shared attributes and methods in the Car class reduce code duplication. It is also highly flexible, allowing new brands to be added easily by creating a new subclass. Encapsulation ensures that internal data is protected from unintended changes, improving maintainability. Finally, abstraction and polymorphism provide clear structure and organization, making the code easier to read, understand, and extend.
