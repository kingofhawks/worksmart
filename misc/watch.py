#pip install watchdog
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print 'hello'
if __name__ == "__main__":
   print 'begin'
   logging.basicConfig(level=logging.INFO,
                       format='%(asctime)s - %(message)s',
                       datefmt='%Y-%m-%d %H:%M:%S')
   path = sys.argv[1] if len(sys.argv) > 1 else '.'
   event_handler = LoggingEventHandler()
   observer = Observer()
   observer.schedule(event_handler, "E:\workspace", recursive=True)
   observer.start()
   try:
       while True:
           time.sleep(1)
   except KeyboardInterrupt:
       observer.stop()
   observer.join()
   print 'finish'
