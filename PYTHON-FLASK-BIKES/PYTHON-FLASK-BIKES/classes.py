class Bike:
    def __init__(self, _id, model, brand, features, year, size, availability, Price_day):
        self._id = _id
        self.model = model
        self.brand = brand
        self.features = features
        self.year = year
        self.size = size
        self.availability = availability
        self.Price_day = Price_day

    def toDBCollection(self):
        return{
            '_id': self._id,
            'model': self.model,
            'brand': self.brand,
            'features': self.features,
            'year': self.year,
            'size': self.size,
            'availability': self.availability,
            'Price_day': self.Price_day 

        }