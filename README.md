PNGWebCapture
=============

#### Description
pngwebcapture.py is a Python script that uses PhantomJS to capture a PNG to a file.

**PhantomJS** is is a headless WebKit and a great tool for server-side solutions. Although it doesn't support Python, using the **Selenium** module, you can accomplish this

I added a couple of useful things to this sample script, which I found online:
(1) A "settle time" optional parameter, which will let the webpage render data-visualizations or other graphics.

(2) Kills the phantomJS process

#### Installing
Install for PhantomJS is here:
http://phantomjs.org/download.html

On the command line, install selenium. 

pip install selenium

The psutil Python module may also need to be installed, depending on your system.


#### Web Fonts
It's a well-documented issue that webfonts dont'render properly with PhantomJS. I've worked around the problem by installing the Google Fonts on my server. **Some** of the webfonts will work properly, others do not.



by Scott Kildall  
[www.kildall.com](http://www.kildall.com)


