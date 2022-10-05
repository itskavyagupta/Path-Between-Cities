# path-between-cities

Considering a rectangular city (let’s say star_city) partitioned into a grid of square cells as shown in the image-

![Screenshot (990)](https://user-images.githubusercontent.com/75752026/194089760-c5ce28a8-1512-4a26-b56a-7b9e044e26d3.png)

- Each of the borders of the star_city are surrounded by different cities- Greendale at top, Smallville at right, Duckburg at bottom and Blue Valley at left.
- Each square cell represents the altitude of the land area (1 lowest and 10 highest). A person can climb down from a higher altitude area to a lower altitude area. So, a person from a particular cell can reach to its adjacent cell (up, left, right, bottom) only if the adjacent cell is of equal or lower altitude.
- Also, all the cells on the border are connected to the respective border city. That means a person can reach a particular neighboring city from any of the cells lying on the border for that city.

We find two paths in this code-

1.	Any 1 route (if exists) from the cell marked Source to the cell marked Destination. 
2.	Any 1 route (if exists) from Blue Valley to Smallville
