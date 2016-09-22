# tellus-rover

'Tellus Rover' is a project in which I intend to create a WiFi-controlled car, driven by a Raspberry Pi.

## Some notes:

- I made the car (mostly out of cardboard), but didn't write the remote; I just used SSH to control the car using keypresses.
- I can't be bothered to write much up about it, but maybe oneday I'll attach a pretty photo of it.
- The only stuff I was actually writing is in the `experimental` folder. The keypress control stuff is in `motor3.py`.
- Writing this made me wonder why there wasn't a Python library for it somewhere on Github, hence [github.com/jamesevickery/l293d](https://github.com/jamesevickery/l293d) was born. At time of writing, this new repository is still in ongoing development.
