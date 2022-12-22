import ampule, socketpool, wifi, microcontroller

from scripts import wifistealer

WLAN = "home"

if __name__ == "__main__":
  try:
    from secrets import secrets
  except ImportError:
    print("WiFi secrets not found in secrets.py")
    raise

  try:
    print("Connecting to %s..." % secrets[WLAN]["ssid"])
    wifi.radio.connect(secrets[WLAN]["ssid"], secrets[WLAN]["password"])
  except:
    print("Error connecting to WiFi")
    raise

  pool = socketpool.SocketPool(wifi.radio)
  socket = pool.socket()
  
  try:
    socket.bind(["0.0.0.0", 80])
  except:
    print("Wifi binding failed, resetting the Pi Cow")
    microcontroller.reset()

  socket.listen(1)
  print("Connected to %s, IPv4 Addr: " % secrets[WLAN]["ssid"], wifi.radio.ipv4_address)

  while True:
    ampule.listen(socket)