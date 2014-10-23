from selenium import webdriver
import time
import psutil

# Entry point: captures web-site as a PNG
def PNGCapture(url, filename, settleTime = 0):
	driver = webdriver.PhantomJS() # or add to your PATH

	# you can resize your PNG here, with this command but I found it wasn't accurate in my testing
	#driver.set_window_size(1280, 960) # optional
	
	# loads the page
	driver.get(url)

	# waits for the page to "settle", useful in case of an animation
	timeout = time.time() + settleTime
	while True:
		if time.time() > timeout:
			break

	# takes a screenshot as a PNG file			
	driver.save_screenshot(filename)

	# kills any lingering processes 
	_killPhantomJS()

# the PhantomJS process will stay in the server process queue. This will kill all the phantom processes
def _killPhantomJS():
	for proc in psutil.process_iter():
    		if  proc.name() == "phantomjs": 
				proc.kill()

if __name__ == "__main__":
	# debug/test code goes here
	PNGCapture('http://www.equitybot.org/sentiments_render.html',"screenshot.png",5)
	#killPhantomJS()
	
