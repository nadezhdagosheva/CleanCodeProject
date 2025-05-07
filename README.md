# CleanCodeProject
Clean Code Project -Tutti Frutti group

We created a Python program that allows two people to play the game Battleship, originally created as a university project. We used Tkinter because it is built into the Python standard library, and because displaying an array of clickable buttons to represent the grid Battleship is played on.

Players place their ships on their hidden boards* by selecting a ship from the drop menu, entering into the text-box the letter-and-number coordinates of the closest square to 'A1' that the ship will occupy, and choosing the orientation, either "Row" if the ship occupies squares in a row or "Col" if it occupies squares in a column, by clicking the appropriate radiobutton before clicking the button labelled "Place the ship".

After players have placed their ships, they take turns (starting with player 1) firing torpedoes by clicking on their grid of buttons. When a torpedo hits an opponent's ship the square turns red and has an 'X' inside. When a torpedo misses, the square turns blue and has a 'O' inside.

To view the number of ships a player has remaining, choose the radiobutton for the player whose ships you wish to count and click the button labelled "Show ships". The number of ships will be printed inside that frame.
