home = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5, p {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 20%;}
.button2 {background-color: #474747;}
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Remote Pi Cow</h1></center>
<form><center>
<h5>Scripts:</h5>
<center> <a class="button" href="/wifistealer">Wifi stealer</a>
<center> <a class="button" href="/keylogger">Keylogger</a>
<center> <a class="button" href="/remotecontrol">Remote control</a>
<h5>Else:</h5>
<center> <a class="button2" href="/results">Results</a>
<center> <a class="button2" href="/quit">Quit</a>
</center></form></body></html>
"""

wifistealer_html = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5 {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 20%;}
.button2 {background-color: #474747;}
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1 href="/">Remote Pi Cow</h1></center>
<form><center>
<h5>Wifi stealer os options:</h5>
<center> <a class="button" href="/wifistealer/windows">Windows</a>
<center> <a class="button" href="/wifistealer/macos">MacOS</a>
<h5>Else:</h5>
<center> <a class="button2" href="/">Home</a>
</center></form></body></html>
"""

keylogger_html = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5, p {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 20%;}
.button2 {background-color: #474747;}
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Remote Pi Cow</h1></center>
<form><center>
<h5>Scripts:</h5>
<center> <a class="button" href="/wifistealer">Wifi stealer</a>
<center> <a class="button" href="/keylogger">Keylogger</a>
<center> <a class="button" href="/keyboard">Remote keyboard</a>
<h5>Else:</h5>
<center> <a class="button2" href="/">Home</a>
</center></form></body></html>
"""

remote_control_html = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5, p {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 20%;}
.button2 {background-color: #474747}
.codeblock {background-color: #1c1c1c; display: inline-block; padding: 40px; border-radius: 20px;}
</style></head>
<body><center><h1>Remote Pi Cow</h1></center>
<form><center>
<form action="" name="" method="post">
    <center><textarea id="payload" class="text" cols="40" rows ="20" name="payload" style="font-size: 30px;"></textarea>
    <center><input type="submit" value="Submit" class="button">
</form>
<h5>Else:
</h5>
<center> <a class="button2" href="/">Home</a>
</center></form></body></html>
"""

results_html = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5, p {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 20%;}
.button2 {background-color: #474747;}
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Remote Pi Cow</h1></center>
<form><center>
<h5>Scripts:</h5>
<center> <a class="button" href="/results/wifistealer">Wifi profiles</a>
<h5>Else:</h5>
<center> <a class="button2" href="/">Home</a>
</center></form></body></html>
"""

results_wifistealer = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5, p {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 20%;}
.button2 {background-color: #474747; display: inline-block; margin: 0px auto; text-align: center;}
.codeblock {background-color: #1c1c1c; display: inline-block; padding: 40px; border-radius: 20px;}
hr {color: #474747;}
</style></head>
<body><center><h1>Remote Pi Cow</h1></center>
<form><center>
<h5>Results:</h5>
<div class="codeblock">
"""
results_wifistealer2 = """
</div>
<h5>Else:</h5>
<center> <a class="button2" href="/">Home</a>
</center></form></body></html>
"""

notfound_html = """
<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html {background-color: #222222; font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
h1, h5 {color: white;}
.button, .button2 {background-color: #32c528; border: 2px solid #000000; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; min-width: 100px;}
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1 href="/">Remote Pi Cow</h1></center>
<form><center>
<h5>Page not found</h5>
<center> <a class="button" href="/">Home</a>
</center></form></body></html>
"""