# new features suspended due to bot verification tests

from zpackage.web import Web 

tracker = Web();
tracker.open_page();
tracker.search();
try:
    tracker.first_time_pop_up_preferences()
except:
    print("First time preferences have been ignored. Rerouting...")
# tracker.close_page();