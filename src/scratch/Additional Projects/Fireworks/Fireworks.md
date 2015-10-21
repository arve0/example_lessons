---
title: Fireworks
level: 1
language: en-GB
stylesheet: scratch
embeds: "*.png"
materials: ["*.sb2","Resources/*.wav", "Resources/*.png"]
---

# Introduction { .intro }

In this project, we’ll create a fireworks display over a city.

![screenshot](fireworks_screenshot.png)

# Step 1: Create a rocket that flies towards the mouse { .activity }

Let’s import the different pictures for the game

## Activity Checklist { .check }

+ Start a new Scratch project. Delete the cat by right clicking it and clicking **Delete**.
+ Replace the backdrop with **outdoor/city-with-water**.
+ Use the `Upload sprite from file` button to add a Rocket sprite to the project (use the **Resources/Rocket.png** costume).
+ Make the rocket hide when the green flag is clicked.
```blocks
	when FLAG clicked
		hide
```
+ Now we want to make the rocket move towards the mouse when the mouse is clicked. Add a `when space key pressed` control block, and under this make the rocket appear and glide towards the mouse.
```blocks
	when [space v] key pressed
		show
		glide (1) secs to x: (mouse x) y: (mouse y)
```

## Test Your Project { .flag }

Click the green flag, place your mouse over the stage and press the space bar.

+ Does the rocket appear and move to the mouse?
+ What happens if you move the mouse and press space again?

## Activity Checklist { .check }

+ Fireworks don’t tend to fly from side to side, so lets make sure it always glides towards the mouse from the bottom of the screen. Before we show the rocket, use the `go to` block to tell it to move to below the bottom of the screen, but stay in the same place horizontally.
```blocks
	when FLAG clicked
		hide

	when [space v] key pressed
		go to x: (mouse x) y: (-200)
		show
		glide (1) secs to x: (mouse x) y: (mouse y)
```

## Test Your Project { .flag }

Click the green flag, place your mouse over the stage and press the space bar.

+ Does the rocket fly towards the mouse from the bottom of the screen?
+ What happens if you move the mouse and press space again?

## Activity Checklist { .check }

+ Finally, let’s make this work by using the mouse button instead of the space bar. To do this, we can wrap our script in a `forever if mouse down` block, then swap the `when space key pressed` control block for `when flag clicked`. And last but not least make sure the rocket is hidden when everything starts up.
```blocks
	when FLAG clicked
		hide
		forever
			if <mouse down?> then
				go to x: (mouse x) y: (-200)
				show
				glide (1) secs to x: (mouse x) y: (mouse y)
```

## Test Your Project { .flag }

Click the green flag, and then press the mouse button over the stage. Click again at another point.

## Things to try { .try }

+ Try making some rockets a little slower or faster than others.
+ Try changing where the rocket moves to before gliding towards the mouse to make it arc a little.

## Save your project { .save }

# Step 2: Make the rocket explode { .activity .new-page }

## Activity Checklist { .check }

+ The first step to make the rocket explode is to make it play a ‘bang’ sound (**Resources/bang.wav**) before it starts moving, and then hide itself once it reaches the mouse. To import a sound go to the Sounds tab and click the `Upload sound from file` button.
```blocks
	when FLAG clicked
		hide
		forever
			if <mouse down?> then
				go to x: (mouse x) y: (-200)
				play sound [bang v]
				show
				glide (1) secs to x: (mouse x) y: (mouse y)
				hide
```

+ Next, make the rocket broadcast a new message when it explodes. We’ll listen for this message later on.
```blocks
	when FLAG clicked
		hide
		forever
			if <mouse down?> then
				go to x: (mouse x) y: (-200)
				play sound [bang v]
				show
				glide (1) secs to x: (mouse x) y: (mouse y)
				hide
				broadcast [explode v]
```

## Test Your Project { .flag }

Click the green flag. Make sure the rocket plays a noise and hides when it reaches the mouse.

## Activity Checklist { .check }

+ Create new sprite from File, **Resources/firework1.png**
+ When it receives the explode message, it should hide itself and then move to the position of the rocket using the go to block, show itself, and then vanish again a second later.
```blocks
	when I receive [explode v]
		hide
		go to [rocket v]
		show
		wait (1) secs
		hide
```

## Test Your Project { .flag }

Send another rocket flying.

+ Does it get replaced with the explosion graphic when it explodes?
+ What happens if you hold the mouse button down whilst moving the mouse? (Don’t worry, we’ll fix this later on).

## Save your project { .save }

# Step 3: Make each explosion unique { .activity .new-page }

+ Now we can make each explosion even more unique by using the `set color effect` { .blockpurple } block, and have it pick a random colour between **1** and **200** before showing it.
```blocks
	when I receive [explode v]
		hide
		set [color v] effect to (pick random (1) to (200))
		go to [rocket v]
		show
		wait (1) secs
		hide
```

## Test Your Project { .flag }

Click the green flag. Does each explosion have a different colour?

## Activity Checklist { .check }

+ Lets add a number of different possible explosion graphics as costumes, using __Resources/firework2.png__ and __Resources/firework3.png__, and switch between them for each rocket, again before showing it.
```blocks
	when I receive [explode v]
		hide
		switch costume to (pick random (1) to (3))
		set [color v] effect to (pick random (1) to (200))
		go to [rocket v]
		show
		wait (1) secs
		hide
```

##Test Your Project { .flag}
__Click the green flag.__

Does each rocket have a different explosion graphic?

## Activity Checklist { .check}

+ Finally, Let's make the explosion get bigger after the rocket explodes! Instead of waiting a second, set the size of the sprite to **5%** before we show it, and then once it’s shown, increase the size by **2 fifty times**, using a `repeat` { .blockorange } block.
```blocks
	when I receive [explode v]
		hide
		switch costume to (pick random (1) to (3))		
		set [color v] effect to (pick random (1) to (200))
		go to [rocket v]
		show
		set size to (5) %
		repeat (50)
			change size by (2)
		end
		hide
```

## Test Your Project { .flag }

Click the green flag.

+ Does the explosion graphic spread out from the centre of the rocket and slowly grow?

## Things to try { .try }

+ Why not try making each explosion more unique by altering the size and speed of growth for the explosion.

## Save your project { .save }

# Step 4: Fixing the Broadcast Bug { .activity .new-page }

Remember earlier we had a bug involving holding down the mouse button? This occurs because when the rocket broadcasts its explosion, it will immediately repeat the if loop and move the rocket back to the bottom of the stage. This happens before the explosion has moved to the position of the rocket.

## Activity Checklist { .check }

+ To fix this, we can replace the broadcast block with a broadcast and `wait` block. This way, the loop will not repeat until the explosion finishes exploding.
```blocks
	when FLAG clicked
		hide
		forever
			if <mouse down?> then
				go to x: (mouse x) y: (-200)
				play sound [bang v]
				show
				glide (1) secs to x: (mouse x) y: (mouse y)
				hide
				broadcast [explode v] and wait
```

## Test Your Project { .flag }

Click the green flag, hold down the mouse button and move the mouse around the stage.

+ Does the explosion graphic appear in the right place and at the right time?

## Save your project { .save }

Well done, you’ve finished! Now you can enjoy your game!

Don’t forget you can share your game with all your friends and family by clicking on **Share** on the menu bar!
