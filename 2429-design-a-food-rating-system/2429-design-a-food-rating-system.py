class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = defaultdict(int)
        self.food_cuisine = defaultdict(str)
        self.topFood = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating[food] = rating
            self.food_cuisine[food] = cuisine
            heappush(self.topFood[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating[food] = newRating
        cuisine = self.food_cuisine[food]
        heappush(self.topFood[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        highestRated = self.topFood[cuisine][0]
        while -highestRated[0] != self.food_rating[highestRated[1]]:
            heappop(self.topFood[cuisine])
            highestRated = self.topFood[cuisine][0]
        return self.topFood[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)