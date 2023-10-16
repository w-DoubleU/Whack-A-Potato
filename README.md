Python auto-whacker for the game 'Farmer Against Potatoes Idle'

I've harnessed the magic of advanced image recognition using pyautogui to deliver an automated Whack-A-Potato.

To ensure the smooth operation of this bot, it's crucial to have identical display settings to mine. This is essential because I'm referencing specific RGB values within particular pixels. When the bot detects the precise RGB value at the specified x and y coordinates, it triggers the clicking action.

Settings I use to get this to work: 

I have 2 - 27" Monitors - Display Resolution 2560x 1440

Game resolution is in 1280 x 720

Things you'll need for script to run:
Main Bot Script, 
topright.png, 
tstart.png, 
end.png


What happens after you press Run & click in the game:

Clicks-> topright.png 
Clicks-> tstart.png 
then the code loops for 60 seconds searching specific b values for 7 within the designated x, y coordinates.  

Video : https://youtu.be/Y4CDGh74zJ8

Next Steps to improve bot:
Have it auto click to keep attack speed at 1.5x, have it auto recycle, have it click the yellow potatoes which give a higher token bonus. (Currently its only clicking green potatoes)

______________________________________________________



